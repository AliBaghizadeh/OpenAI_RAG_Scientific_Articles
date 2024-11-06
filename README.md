# OpenAI RAG for Scientific Articles

A Streamlit-based application that leverages OpenAI's API to perform retrieval-augmented question-answering (RAG) on scientific articles in PDF format. This app allows users to upload PDF files, process and extract relevant text, and ask questions based on the content of the PDFs.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [How It Works](#how-it-works)
7. [Contributing](#contributing)
8. [License](#license)

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
   git clone https://github.com/yourusername/OpenAI_RAG_Scientific_Articles.git
   cd OpenAI_RAG_Scientific_Articles
