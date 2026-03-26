from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas import BilhetagemCreate
from backend.services.bilhetagem_service import (
    criar_bilhetagem,
    listar_bilhetagens,
)

router = APIRouter(prefix="/bilhetagem", tags=["Bilhetagem"])


@router.post("/")
def criar(dados: BilhetagemCreate, db: Session = Depends(get_db)):
    try:
        nova_bilhetagem = criar_bilhetagem(db, dados)
        return {
            "status": "sucesso",
            "mensagem": "Bilhetagem registrada com sucesso.",
            "dados": {
                "id": nova_bilhetagem.id,
                "tipo": nova_bilhetagem.tipo,
                "quantidade": nova_bilhetagem.quantidade,
                "valor_total": nova_bilhetagem.valor_total,
                "data": nova_bilhetagem.data,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar bilhetagem: {str(e)}")


@router.get("/")
def listar(db: Session = Depends(get_db)):
    try:
        bilhetagens = listar_bilhetagens(db)
        return {
            "status": "sucesso",
            "total": len(bilhetagens),
            "dados": bilhetagens,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar bilhetagens: {str(e)}")