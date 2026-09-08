from typing import Annotated

from fastapi import APIRouter, Depends, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.banco_de_dados.usuario_repositorio import UsuarioRepositorio
from app.dependencias import obter_usuario_repositorio
from app.modelos.usuario import UsuarioCriarAtualizar

router = APIRouter(
    prefix="/registro"
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def pagina_registro(request: Request):
    return templates.TemplateResponse(request, "registro.html", {})

@router.post("/")
async def registrar_usuario(
    usuario_repositorio: Annotated[UsuarioRepositorio, Depends(obter_usuario_repositorio)],
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confirma_senha: str = Form(...),
):
    # Dicionário auxiliar para repovoar o formulário em caso de erro
    data = {
        "nome": nome,
        "email": email,
    }

    # 1. Validar se todos os campos obrigatórios estão preenchidos
    if not all([email, senha, nome, confirma_senha]):
        return templates.TemplateResponse(request, "registro.html", {
            "error": "Campos obrigatórios faltantes",
            **data
        })

    # 2. Validar se as senhas coincidem
    if senha != confirma_senha:
        return templates.TemplateResponse(request, "registro.html", {
            "error": "As senhas não conferem.",
            **data
        })

    # 3. Verificar se o e-mail já está cadastrado no sistema
    usuario_existente = await usuario_repositorio.buscar_usuario_por_email(email)
    if usuario_existente:
        return templates.TemplateResponse(request, "registro.html", {
            "error": "Usuário inválido.",  # Mensagem genérica por segurança contra atacantes
            **data
        })

    # 4. Criar o objeto e persistir no banco de dados via repositório
    usuario_criar = UsuarioCriarAtualizar(nome=nome, email=email, senha=senha)
    usuario = await usuario_repositorio.criar_usuario(usuario_criar)

    # 5. Redirecionar para o login se criado com sucesso, ou retornar erro genérico
    if usuario:
        return RedirectResponse(url="/login", status_code=303)

    return templates.TemplateResponse(request, "registro.html", {
        "error": "Não foi possível criar o usuário, tente novamente mais tarde.",
        **data
    })