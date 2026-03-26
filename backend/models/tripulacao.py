from sqlalchemy import Column, Integer, String, DateTime
from backend.database import Base

class Tripulacao(Base):
    __tablename__ = "tripulacoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    funcao = Column(String, nullable=False)
    inicio_turno = Column(DateTime, nullable=True)
    fim_turno = Column(DateTime, nullable=True)
    status = Column(String, default="disponivel")