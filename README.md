# OpenAI RAG for Scientific Articles

A Streamlit-based application that leverages OpenAI's API to perform retrieval-augmented question-answering (RAG) on scientific articles in PDF format. This app allows users to upload PDF files, process and extract relevant text, and ask questions based on the content of the PDFs. I learned the foundation of OpenAI in the course, [Generative AI: OpenAI API, ChatGPT, and GPT-4 in Python](https://deeplearningcourses.com/c/genai-openai-chatgpt) by Lazy Programmer, and I do recommend it to whoever likes to learn OpenAI and its applications. 

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [How It Works](#how-it-works)
7. [Contributing](#contributing)

## Project Overview

This application uses a retrieval-augmented generation approach, where content from uploaded PDFs is processed, chunked, and embedded to allow for efficient question-answering. The app is particularly useful for scientific PDFs, enabling users to obtain answers to specific questions about the content of the uploaded files.

The project leverages:
- **OpenAI Embeddings** for content retrieval.
- **FAISS** (Facebook AI Similarity Search) for fast vector search to find relevant content.
- **Streamlit** for building an interactive UI for uploading PDFs, entering queries, and displaying answers.

## Features

- **Upload and Process PDFs**: Upload multiple PDF files and extract text from the first few pages.
- **Content Embedding and Search**: Convert text chunks to embeddings and search for relevant content based on user queries.
- **Question-Answering**: Ask questions based on uploaded content, and receive contextual answers generated using OpenAI's API.
  
## Installation

To set up and run this project locally, follow these steps:

### Prerequisites

- **Python**: Ensure Python 3.7 or later is installed on your system.
- **OpenAI API Key**: Sign up on the [OpenAI website](https://beta.openai.com/signup/) and obtain an API key.

### Installation Steps

1. **Clone the repository**:
   ```bash
    git clone https://github.com/AliBaghizadeh/OpenAI_RAG_Scientific_Articles.git
    cd OpenAI_RAG_Scientific_Articles
   
2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. **Install the dependencies**:
  ```bash
  pip install -r requirements.txt
  ```
4. **Run the Streamlit application**:
  ```bash
  streamlit run main.py
  ```
5. **Access the App**:
   ```bash
  Open your web browser and go to http://localhost:8501
    ```
## Usage
- Enter your OpenAI API key in the sidebar.
- Upload PDF files, and type your question in the text input box.
- View the retrieved context and generated answer.

## Example Workflow
- Upload a scientific PDF or any other document.
- Type a question in the query box, such as "What are the main findings discussed in the paper?".
- View the context retrieved from the document and the generated answer.

## Project Structure
The project is structured as follows:
```
OpenAI_RAG_Scientific_Articles/      
├── main.py                   # Entry point for the Streamlit app    
├── pdf_processing.py         # Functions for extracting and chunking PDF text    
├── embedding.py              # Functions for embedding and querying    
├── requirements.txt          # List of dependencies   
├── pdf_files                 # Examples of some pdf files of scientific articles from my own research    
├── .gitignore                # File to ignore unnecessary files in Git  
└── README.md                 # Project documentation   
```
## Key Files
- **main.py**: The main script for running the Streamlit app.    
- **pdf_processing.py**: Contains functions to process PDF files and extract text.      
- **embedding.py**: Contains functions for generating embeddings, searching content, and querying OpenAI's API.   
- **requirements.txt**: Lists all Python libraries required to run the app.     

## How It Works
- **PDF Extraction**P: The app extracts text from the first few pages of each uploaded PDF to get relevant content.
- **Text Chunking**P: Text is divided into chunks to ensure efficient processing and embedding.
- **Embedding Generation**P: Using OpenAI’s text-embedding-ada-002 model, each text chunk is converted into an embedding vector.
- **Vector Search with FAISS**P: The FAISS library allows for efficient searching through the embedding vectors to find relevant text chunks based on a user's question.
- **Contextual Answer Generation**P: The app uses the context retrieved from FAISS and generates an answer with OpenAI's API.

## Contributing
Contributions are welcome! If you'd like to improve the app, please follow these steps:
```
Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Open a pull request.
Please ensure that your code adheres to the existing style and is well-documented.
```

