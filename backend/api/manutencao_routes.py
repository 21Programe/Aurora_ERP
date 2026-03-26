from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas import ManutencaoCreate
from backend.services.manutencao_service import (
    criar_manutencao,
    listar_manutencoes,
)

router = APIRouter(prefix="/manutencao", tags=["Manutenção"])


@router.post("/")
def criar(dados: ManutencaoCreate, db: Session = Depends(get_db)):
    try:
        nova_manutencao = criar_manutencao(db, dados)
        return {
            "status": "sucesso",
            "mensagem": "Manutenção cadastrada com sucesso.",
            "dados": {
                "id": nova_manutencao.id,
                "veiculo_id": nova_manutencao.veiculo_id,
                "tipo": nova_manutencao.tipo,
                "descricao": nova_manutencao.descricao,
                "km": nova_manutencao.km,
                "data": nova_manutencao.data,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar manutenção: {str(e)}")


@router.get("/")
def listar(db: Session = Depends(get_db)):
    try:
        manutencoes = listar_manutencoes(db)
        return {
            "status": "sucesso",
            "total": len(manutencoes),
            "dados": manutencoes,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar manutenções: {str(e)}")