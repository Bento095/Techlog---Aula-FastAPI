from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from app.rotas import cliente, login, registro
from app.autenticacao_middleware import AuthenticationToken


app = FastAPI(
    title="Techlog Solutions API",
    description="CRM para Techlog Solutions",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(AuthenticationToken)

app.include_router(cliente.router)
app.include_router(cliente.front_router)

app.include_router(login.router)
app.include_router(registro.router)

templates = Jinja2Templates(directory="templates")

@app.get("/health-check")
async def health_check():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
async def front_page(request: Request):
    return templates.TemplateResponse(
        request,  
        "index.html", 
        {  "titulo": "Techlog Solutions CRM",
            "versao": "1.0.0",
            "descricao": "CRM para Techlog Solutions",
        },
    )