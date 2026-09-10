import pytest
from fastapi.responses import RedirectResponse

from app.modelos.usuario import Usuario
from app.rotas.login import login


@pytest.mark.asyncio
async def test_login_com_credenciais_validas_redireciona(
    self, mock_usuario_repositorio, mock_request
):
    usuario_mock = Usuario(
        id=1,
        nome="João Silva",
        email="joao@example.com"
    )
    mock_usuario_repositorio.buscar_usuario_por_email_senha.return_value = usuario_mock
    resultado = await login.login(
        mock_usuario_repositorio,
        mock_request,
        email="joao@example.com",
        senha="senha123"
    )

    assert isinstance(resultado, RedirectResponse)
    assert resultado.status_code == 303
    assert resultado.headers["location"] == "/"
    assert "session_token" in resultado.headers.get("set-cookie", "")