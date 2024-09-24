# AI Response with Audio Player

This project integrates AI-generated text responses with a simple frontend. The system allows users to query a custom AI model (RAG-based) trained on NCERT content,general knowledge, retrieve text responses, and play the responses as audio.

## Features

- **AI-powered Responses**: Retrieve answers from an AI model based on NCERT content.
- **Differentiation of Responses**: The system distinguishes between general knowledge queries and those requiring deeper context from the RAG.
- **Additional Tools**: The system includes utility tools like a calculator and greeting system integrated with the AI.
- **Text-to-Audio Conversion**: Converts AI text responses into audio (WAV format) using SARVAM API.

## Technology Stack

### Frontend:
- **Next.js**: React framework for server-side rendering and static site generation.
- **shadcn**: Radix UI component library integrated with Tailwind CSS for building accessible and customizable components.
- **Tailwind CSS**: Utility-first CSS framework to style the application efficiently.
- **React**: JavaScript library for building interactive user interfaces.

### Backend:
- **FastAPI**: High-performance backend framework for serving API requests and managing AI model responses.
- **RAG Model (Retrieval-Augmented Generation)**: Custom-trained on NCERT PDFs to provide accurate and contextual responses based on educational content.
  - **NCERT Training**: The RAG model is specifically trained on NCERT PDF, enabling it to provide educationally accurate responses.
  - **Tool Integration**: Includes a variety of additional tools such as a calculator and a greeting generator for a more interactive AI.
  - **General Knowledge vs RAG**: The system distinguishes between general queries (using LLM-based responses) and contextually rich, document-based responses from the RAG model.
- **LLM (Google FLAN-T5)**: Large Language Model via Hugging Face for generating knowledge-based responses.
- **Hugging Face**: Manages embeddings and integrates `google/flan-t5` for the LLM.
- **FAISS**: Vector search library for similarity search across document embeddings.
- **PyPDF**: For parsing and extracting text from PDFs (used to train the RAG on NCERT documents).
- **LangChain**: Orchestrates interactions between the vector database, LLM, and custom business logic.
- **Sarvam API**: Converts text responses into audio (WAV format) for playback.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/ojninja16/RAG_chat.git
```

### 2.Navigate to the project directory:
    
    ```bash
    cd Frontend/
    cd Backend/
    ```

### 3. Install dependencies:

```bash
npm install
```

### 4. Backend setup:
#### Create a Python environment and install dependencies:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
5. Create a env variable file

// Create a .env file in the root directory of the backend add the following variables

```bash
PDF_DIR="path to the directory containing the NCERT PDF"
SARVAM_API_KEY="API key for the Sarvam API"
```
6.Run Frontend and Backend

```bash
npm run dev
uvicorn main:app --reload
```
### Usage:
- Navigate to the frontend URL (usually http://localhost:3000).
- Enter a question in the input field and click the "Ask" button to retrieve an AI-generated response.
-The system will use the RAG model to retrieve answers based on NCERT data, or general knowledge, depending on the query.
-The text response will be converted to audio, which you can play via the integrated audio player.