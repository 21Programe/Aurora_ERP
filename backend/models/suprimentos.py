from sqlalchemy import Column, Integer, Float, DateTime, String
from datetime import datetime
from backend.database import Base

class Suprimento(Base):
    __tablename__ = "suprimentos"

    id = Column(Integer, primary_key=True, index=True)
    veiculo_id = Column(Integer, nullable=False)
    tipo = Column(String, default="combustivel")
    litros = Column(Float, nullable=False)
    valor_total = Column(Float, nullable=False)
    km_referencia = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)