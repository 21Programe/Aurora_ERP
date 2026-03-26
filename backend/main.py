from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import Base, engine

from backend.models.veiculo import Veiculo
from backend.models.manutencao import Manutencao
from backend.models.tripulacao import Tripulacao
from backend.models.trafego import Trafego
from backend.models.suprimentos import Suprimento
from backend.models.bilhetagem import Bilhetagem

from backend.api.manutencao_routes import router as manutencao_router
from backend.api.tripulacao_routes import router as tripulacao_router
from backend.api.trafego_routes import router as trafego_router
from backend.api.suprimentos_routes import router as suprimentos_router
from backend.api.bilhetagem_routes import router as bilhetagem_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Aurora ERP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(manutencao_router)
app.include_router(tripulacao_router)
app.include_router(trafego_router)
app.include_router(suprimentos_router)
app.include_router(bilhetagem_router)

@app.get("/")
def home():
    return {"mensagem": "Aurora ERP online"}