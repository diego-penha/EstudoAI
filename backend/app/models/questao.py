from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)

from app.database.database import Base


class Questao(Base):
    __tablename__ = "questoes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id")
    )

    tipo = Column(
        String,
        nullable=False,
        default="multipla_escolha"
    )

    enunciado = Column(
        Text,
        nullable=False
    )

    resposta_correta = Column(
        Text,
        nullable=False
    )

    explicacao = Column(Text)