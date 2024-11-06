import openai
from typing import List, Any
import numpy as np
import tiktoken
import pandas as pd

def get_embedding(text: str, model: str) -> List[float]:
    """
    Fetches the embedding vector for a given text chunk.

    Parameters:
        text (str): A string representing a text chunk.
        model (str): The OpenAI embedding model name.

    Returns:
        List[float]: The embedding vector for the text.
    """
    response = openai.embeddings.create(model=model, input=[text])
    return response.data[0].embedding

def join_top_chunks(df_chunks: pd.DataFrame, indices: Any, encoding, max_token_size=600) -> str:
    """
    Combines the top retrieved chunks into a single context.

    Parameters:
        df_chunks (pd.DataFrame): DataFrame containing document chunks.
        indices (Any): Indices of top chunks from FAISS index search.
        encoding: Encoding object from tiktoken library.
        max_token_size (int): Maximum allowable tokens in the final context.

    Returns:
        str: A single string containing the combined context text.
    """
    top_chunks = [df_chunks.iloc[idx]["chunk_text"] for idx in indices[0]]
    context = "\n\n".join(top_chunks)
    context_tokens = encoding.encode(context)
    if len(context_tokens) > max_token_size:
        context = encoding.decode(context_tokens[:max_token_size])
    return context

def complete(user_prompt: str, max_tokens=500) -> Any:
    """
    Uses the OpenAI API to generate a response based on a user prompt.

    Parameters:
        user_prompt (str): The prompt with query and retrieved context.
        max_tokens (int): Maximum tokens for the response.

    Returns:
        Any: Completion object from OpenAI API.
    """
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_prompt}],
        max_tokens=max_tokens,
        temperature=0,
    )
    return completion

def get_response(completion: Any) -> str:
    """
    Extracts the final text response from OpenAI's completion object.

    Parameters:
        completion (Any): Completion object returned by complete().

    Returns:
        str: The generated response text.
    """
    return completion.choices[0].message["content"]
