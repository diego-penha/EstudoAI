from pydantic import BaseModel


class RespostaUsuario(BaseModel):
    questao_id: int
    resposta: str