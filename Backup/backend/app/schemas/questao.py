from pydantic import BaseModel


class AlternativaCreate(BaseModel):
    codigo: str
    texto: str


class QuestaoCreate(BaseModel):
    categoria_id: int
    tipo: str
    enunciado: str
    resposta_correta: str
    explicacao: str

    alternativas: list[AlternativaCreate]