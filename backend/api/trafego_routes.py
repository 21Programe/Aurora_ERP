from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas import TrafegoCreate
from backend.services.trafego_service import (
    criar_trafego,
    listar_trafegos,
)

router = APIRouter(prefix="/trafego", tags=["Tráfego"])


@router.post("/")
def criar(dados: TrafegoCreate, db: Session = Depends(get_db)):
    try:
        novo_trafego = criar_trafego(db, dados)
        return {
            "status": "sucesso",
            "mensagem": "Registro de tráfego criado com sucesso.",
            "dados": {
                "id": novo_trafego.id,
                "linha": novo_trafego.linha,
                "veiculo_id": novo_trafego.veiculo_id,
                "motorista": novo_trafego.motorista,
                "horario_saida": novo_trafego.horario_saida,
                "horario_chegada": novo_trafego.horario_chegada,
                "atraso_min": novo_trafego.atraso_min,
                "status": novo_trafego.status,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar tráfego: {str(e)}")


@router.get("/")
def listar(db: Session = Depends(get_db)):
    try:
        trafegos = listar_trafegos(db)
        return {
            "status": "sucesso",
            "total": len(trafegos),
            "dados": trafegos,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar tráfego: {str(e)}")