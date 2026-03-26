from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas import SuprimentoCreate
from backend.services.suprimentos_service import (
    criar_suprimento,
    listar_suprimentos,
)

router = APIRouter(prefix="/suprimentos", tags=["Suprimentos"])


@router.post("/")
def criar(dados: SuprimentoCreate, db: Session = Depends(get_db)):
    try:
        novo_suprimento = criar_suprimento(db, dados)
        return {
            "status": "sucesso",
            "mensagem": "Suprimento cadastrado com sucesso.",
            "dados": {
                "id": novo_suprimento.id,
                "veiculo_id": novo_suprimento.veiculo_id,
                "tipo": novo_suprimento.tipo,
                "litros": novo_suprimento.litros,
                "valor_total": novo_suprimento.valor_total,
                "km_referencia": novo_suprimento.km_referencia,
                "data": novo_suprimento.data,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar suprimento: {str(e)}")


@router.get("/")
def listar(db: Session = Depends(get_db)):
    try:
        suprimentos = listar_suprimentos(db)
        return {
            "status": "sucesso",
            "total": len(suprimentos),
            "dados": suprimentos,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar suprimentos: {str(e)}")