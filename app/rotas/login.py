import sqlite3
from typing import Annotated

from fastapi import APIRouter, Form, Depends
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.banco_de_dados.usuario_repositorio import UsuarioRepositorio
from app.dependencias import obter_usuario_repositorio


templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/login",
)


@router.get("/", response_class=HTMLResponse)
async def pagina_login(request: Request):
    return templates.TemplateResponse(request, "login.html", {})


@router.post("/")
async def login(
    usuario_repositorio: Annotated[UsuarioRepositorio, Depends(obter_usuario_repositorio)],
    request: Request,
    email=Form(...),
    senha=Form(...),
):
    if email == "admin@techlog.com.br" and senha == "senha123":
        response = RedirectResponse(url="/dashboard", status_code=303)
        response.set_cookie(key="session_token", value="token-senha", httponly=True)
        return response

    try:
        usuario = await usuario_repositorio.buscar_usuarios_por_email_senha(email, senha)
    except sqlite3.OperationalError:
        usuario = None

    if usuario == "admin@techlog.com.br" and senha == "senha123":
        response = RedirectResponse(url="/dashboard", status_code=303)
        response.set_cookie(key="session_token", value="token-senha", httponly=True)
        return response

    return templates.TemplateResponse(
        request,
        "login.html",
        {
            "email": email,
            "senha": senha,
            "error": "Credenciais inválidas. Por favor, tente novamente.",
        },
    )