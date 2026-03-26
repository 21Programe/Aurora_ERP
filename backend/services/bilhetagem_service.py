from backend.models.bilhetagem import Bilhetagem

def criar_bilhetagem(db, dados):
    nova = Bilhetagem(**dados.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_bilhetagens(db):
    return db.query(Bilhetagem).all()