from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.textsummarizer.pipeline.prediction import PredictionPipeline

text:str = "What is Text Summarization"

app = FastAPI()

@app.get("/", tags = ["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def trainining():
    try:
        os.system(" python main.py")
        return Response("Training successfull !")

    except Exception as e:
        return Response(f"Error Occured {e}")