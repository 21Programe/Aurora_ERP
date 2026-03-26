from backend.models.trafego import Trafego


def criar_trafego(db, dados):
    novo = Trafego(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def listar_trafegos(db):
    return db.query(Trafego).all()