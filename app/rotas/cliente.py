from fastapi import APIRouter
from app.modelos.cliente import Cliente


router = APIRouter(
    prefix="/clientes",
)

CLIENT_LIST = [Cliente(id_=1, nome="Jubileu", email='jubileu@exemplo.com', telefone="1234569800"), 
                     Cliente(id_=2, nome="Jubileia", email='jubileia@exemplo.com', telefone="12398769800")]

@router.get("/", response_model=list[Cliente])
async def listar_clientes():
    return CLIENT_LIST

@router.get("/{cliente_id}",response_model=Cliente | None)
async def obter_cliente(cliente_id: int):
    for cliente in CLIENT_LIST:
        if cliente.id_ == cliente_id:
            return cliente
    return None