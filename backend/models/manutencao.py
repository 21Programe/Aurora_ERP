from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from backend.database import Base

class Manutencao(Base):
    __tablename__ = "manutencoes"

    id = Column(Integer, primary_key=True, index=True)
    veiculo_id = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    km = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)