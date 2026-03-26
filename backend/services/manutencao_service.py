from backend.models.manutencao import Manutencao

def criar_manutencao(db, dados):
    nova = Manutencao(**dados.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_manutencoes(db):
    return db.query(Manutencao).all()