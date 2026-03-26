from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from backend.database import Base

class Bilhetagem(Base):
    __tablename__ = "bilhetagens"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    quantidade = Column(Integer, default=1)
    valor_total = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)