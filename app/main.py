from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.rotas import cliente


app = FastAPI(
    title="Techlog Solutions API",
    description="CRM para Techlog Solutions",
    version="1.0.0",
)

app.include_router(cliente.router)

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def health_check():
    return {"status": "ok"}


@app.get("/front", response_class=HTMLResponse)
async def front_page(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="front.html",
    context={"status": "Operacional"}
)