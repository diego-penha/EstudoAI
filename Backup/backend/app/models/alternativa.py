from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class Alternativa(Base):
    __tablename__ = "alternativas"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    questao_id = Column(
        Integer,
        ForeignKey("questoes.id"),
        nullable=False
    )

    codigo = Column(
        String,
        nullable=False
    )

    texto = Column(
        String,
        nullable=False
    )