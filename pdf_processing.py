import PyPDF2
import pandas as pd
from typing import List, Dict
import tiktoken

def extract_custom_pages(files, num_pages=3) -> pd.DataFrame:
    """
    Extracts text from the first few pages of each uploaded PDF file.

    Parameters:
        files: List of uploaded PDF files.
        num_pages: Number of pages to extract from each PDF.

    Returns:
        pd.DataFrame: A DataFrame containing the document ID and text.
    """
    data = []
    for file in files:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(min(num_pages, len(reader.pages))):
            page = reader.pages[page_num]
            text += page.extract_text() if page else ""
        data.append({"doc_id": file.name, "text": text})
    return pd.DataFrame(data)

def chunk_text(text: str, encoding, max_chunk_size=500) -> List[str]:
    """
    Splits large text data into manageable chunks.

    Parameters:
        text (str): The text to be chunked.
        encoding: Encoding object from tiktoken library.
        max_chunk_size (int): Maximum tokens per chunk.

    Returns:
        List[str]: List of text chunks.
    """
    tokens = encoding.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_chunk_size):
        chunk = encoding.decode(tokens[i: i + max_chunk_size])
        chunks.append(chunk)
    return chunks
