from backend.models.suprimentos import Suprimento


def criar_suprimento(db, dados):
    novo = Suprimento(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def listar_suprimentos(db):
    return db.query(Suprimento).all()