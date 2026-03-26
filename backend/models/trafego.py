from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.database import Base

class Trafego(Base):
    __tablename__ = "trafegos"

    id = Column(Integer, primary_key=True, index=True)
    linha = Column(String, nullable=False)
    veiculo_id = Column(Integer, nullable=False)
    motorista = Column(String, nullable=False)
    horario_saida = Column(DateTime, default=datetime.utcnow)
    horario_chegada = Column(DateTime, nullable=True)
    atraso_min = Column(Integer, default=0)
    status = Column(String, default="em_operacao")