from backend.models.tripulacao import Tripulacao


def criar_tripulacao(db, dados):
    novo = Tripulacao(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def listar_tripulacao(db):
    return db.query(Tripulacao).all()