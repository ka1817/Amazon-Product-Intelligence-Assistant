from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.retrival_genaration import retrival_genaration
from src.data_ingestion import data_ingestion
from src.data_preprocess import data_preprocess

app = FastAPI(
    title="Amazon Product QA API",
    description="Query Amazon product data using LangChain, FAISS, and GROQ.",
    version="1.0"
)

# Mount static and template folders
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/query", response_class=HTMLResponse)
async def query(request: Request, query: str = Form(...)):
    try:
        result = retrival_genaration(query)
        answer = result

        return templates.TemplateResponse("index.html", {
            "request": request,
            "query": query,
            "answer": answer,
        })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "query": query,
            "answer": f"An error occurred: {str(e)}",
           
        })

