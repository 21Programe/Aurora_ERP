from pydantic import BaseModel
from typing import Optional

class ManutencaoCreate(BaseModel):
    veiculo_id: int
    tipo: str
    descricao: str
    km: float

class TripulacaoCreate(BaseModel):
    nome: str
    funcao: str
    status: Optional[str] = "disponivel"

class TrafegoCreate(BaseModel):
    linha: str
    veiculo_id: int
    motorista: str

class SuprimentoCreate(BaseModel):
    veiculo_id: int
    tipo: str
    litros: float
    valor_total: float
    km_referencia: float

class BilhetagemCreate(BaseModel):
    tipo: str
    quantidade: int
    valor_total: float