import os
import streamlit as st
import pandas as pd
import numpy as np
import faiss
import openai
import tiktoken
from pdf_processing import extract_custom_pages, chunk_text
from embedding import get_embedding, join_top_chunks, complete, get_response

# Streamlit app setup
st.sidebar.title("OpenAI API Key Required")
user_api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

# Only proceed if the user provides an API key
if user_api_key:
    openai.api_key = user_api_key

    emb_model = "text-embedding-ada-002"
    encoding = tiktoken.encoding_for_model(emb_model)

    st.title("PDF QA with Retrieval-Augmented Generation")
    st.write("Upload PDFs, and ask questions based on their content.")

    # Sidebar for PDF upload
    uploaded_files = st.sidebar.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

    # Extract and chunk text if files are uploaded
    if uploaded_files:
        st.write("Extracting text from PDFs...")
        df = extract_custom_pages(uploaded_files)

        # Chunk text and create DataFrame
        df["chunks"] = df["text"].apply(lambda x: chunk_text(x, encoding))
        chunk_data = []
        for _, row in df.iterrows():
            for i, chunk in enumerate(row["chunks"]):
                chunk_data.append({"doc_id": row["doc_id"], "chunk_id": f"{row['doc_id']}_chunk_{i}", "chunk_text": chunk})
        df_chunks = pd.DataFrame(chunk_data)

        # Generate embeddings
        st.write("Generating embeddings for each chunk...")
        df_chunks["embedding"] = df_chunks["chunk_text"].apply(lambda x: get_embedding(x, emb_model))

        # Initialize FAISS index and add embeddings
        dim = len(df_chunks["embedding"].iloc[0])
        index = faiss.IndexFlatL2(dim)
        embeddings = np.array(df_chunks["embedding"].tolist()).astype("float32")
        index.add(embeddings)

        # Input query
        query = st.text_input("Enter your query:")
        if query:
            # Get query embedding and search index
            query_emb = np.array(get_embedding(query, emb_model)).reshape(1, -1)
            distances, indices = index.search(query_emb, k=5)
            context = join_top_chunks(df_chunks, indices, encoding)

            # Display the context
            st.subheader("Retrieved Context")
            st.write(context)

            # Prompt and answer generation
            prompt = f"""Please answer the question given the provided context.

            question:
            '''
            {query}
            '''
            context:
            '''
            {context}
            '''
            """
            completion = complete(prompt)
            answer = get_response(completion)

            # Display answer
            st.subheader("Answer")
            st.write(answer)
else:
    st.warning("Please enter your OpenAI API key to proceed.")
