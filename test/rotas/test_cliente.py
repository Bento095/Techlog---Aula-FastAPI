import pytest
from app.rotas.cliente import cliente
from app.modelos.cliente import ClienteCriarAtualizar, Cliente

from fastapi import HTTPException
from fastapi.responses import RedirectResponse

class TestRotasClienteAPI:
    @pytest.mark.asyncio
    async def test_listar_clientes_retorna_lista_vazia(self, mock_cliente_repositorio):
        mock_cliente_repositorio.listar_clientes.return_value = []

        resultado = await cliente.listar_clientes(mock_cliente_repositorio)

        assert resultado == []
        mock_cliente_repositorio.listar_clientes.assert_called_once()


@pytest.mark.asyncio
async def test_obter_cliente_inexistente_lanca_excecao(self, mock_cliente_repositorio):
    mock_cliente_repositorio.obter_cliente.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        await cliente.obter_cliente(mock_cliente_repositorio, 999)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Cliente não encontrado!"


