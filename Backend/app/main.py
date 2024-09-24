from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from app.services.rag_srvc import rag_service
from app.services.agent_service import agent_service
from app.services.text2speech import tts_service
import os

load_dotenv()

app = FastAPI()

class Query(BaseModel):
    text: str
    generate_audio: bool = False
class Response(BaseModel):
    response: str
    used_tool: str
    rag_confidence: float
    audio: str = None

@app.on_event("startup")
async def startup_event():
    pdf_dir = os.getenv("PDF_DIR", "E:\RAG\data")
    print(f"PDF directory loaded: {pdf_dir}")  
    try:
        rag_service.load_documents(pdf_dir)
        print("Documents successfully loaded")  
    except Exception as e:
        print(f"Error during loading documents: {e}")

@app.post("/query")
async def query(query: Query):
    print(f"Received query: {query.text}")
    try:
        results = agent_service.process_query(query.text)
        print(f"Query results: {results}")
        response = Response(**results)
        
        if query.generate_audio:
            audio_content = tts_service.generate_audio(results["response"])
            if audio_content:
                response.audio = audio_content
            else:
                print("Failed to generate audio")
        
        return response
    except Exception as e:
        print(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)