from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import ManutencaoCreate
from backend.services.manutencao_service import criar_manutencao, listar_manutencoes

router = APIRouter(prefix="/manutencao", tags=["Manutenção"])

@router.post("/")
def criar(dados: ManutencaoCreate, db: Session = Depends(get_db)):
    return criar_manutencao(db, dados)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_manutencoes(db)