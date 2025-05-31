from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.retrival_genaration import ingestdata, generation, query_rewriting

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

vstore = ingestdata()
chain = generation(vstore)

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

@app.post("/", response_class=HTMLResponse)
async def handle_query(request: Request, user_query: str = Form(...)):
    rewritten = query_rewriting(user_query)
    result = chain.invoke(rewritten)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "response": result,
        "original_query": user_query,
        "rewritten_query": rewritten
    })
