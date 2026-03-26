from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas import TripulacaoCreate
from backend.services.tripulacao_service import (
    criar_tripulacao,
    listar_tripulacao,
)

router = APIRouter(prefix="/tripulacao", tags=["Tripulação"])


@router.post("/")
def criar(dados: TripulacaoCreate, db: Session = Depends(get_db)):
    try:
        nova_tripulacao = criar_tripulacao(db, dados)
        return {
            "status": "sucesso",
            "mensagem": "Tripulante cadastrado com sucesso.",
            "dados": {
                "id": nova_tripulacao.id,
                "nome": nova_tripulacao.nome,
                "funcao": nova_tripulacao.funcao,
                "status": nova_tripulacao.status,
                "inicio_turno": nova_tripulacao.inicio_turno,
                "fim_turno": nova_tripulacao.fim_turno,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar tripulação: {str(e)}")


@router.get("/")
def listar(db: Session = Depends(get_db)):
    try:
        tripulacao = listar_tripulacao(db)
        return {
            "status": "sucesso",
            "total": len(tripulacao),
            "dados": tripulacao,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar tripulação: {str(e)}")