from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String, unique=True, nullable=False)
    modelo = Column(String, nullable=False)
    km_atual = Column(Float, default=0)
    status = Column(String, default="ativo")