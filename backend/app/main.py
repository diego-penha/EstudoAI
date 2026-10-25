from app.schemas.correcao import RespostaUsuario
import random
from sqlalchemy import select
from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import os

from app.database.database import (
    Base,
    engine,
    get_db
)

from app.models.categoria import Categoria
from app.models.questao import Questao
from app.models.alternativa import Alternativa

from app.schemas.categoria import (
    CategoriaCreate
)

from app.schemas.questao import (
    QuestaoCreate
)

app = FastAPI(
    title="StudyAI",
    description="Sistema Inteligente de Estudos",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {
        "status": "online",
        "sistema": "StudyAI",
        "versao": "1.0.0"
    }


@app.get("/saude")
def saude():
    return {
        "backend": "ok"
    }


@app.post("/upload-pdf")
async def upload_pdf(
    arquivo: UploadFile = File(...)
):
    caminho = os.path.join(
        UPLOAD_DIR,
        arquivo.filename
    )

    with open(caminho, "wb") as buffer:
        conteudo = await arquivo.read()
        buffer.write(conteudo)

    return {
        "mensagem": "PDF enviado com sucesso",
        "arquivo": arquivo.filename
    }


@app.post("/categorias")
def criar_categoria(
    categoria: CategoriaCreate,
    db: Session = Depends(get_db)
):
    nova_categoria = Categoria(
        nome=categoria.nome
    )

    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)

    return nova_categoria


@app.get("/categorias")
def listar_categorias(
    db: Session = Depends(get_db)
):
    return db.query(Categoria).all()


@app.post("/questoes")
def criar_questao(
    questao: QuestaoCreate,
    db: Session = Depends(get_db)
):

    nova_questao = Questao(
        categoria_id=questao.categoria_id,
        tipo=questao.tipo,
        enunciado=questao.enunciado,
        resposta_correta=questao.resposta_correta,
        explicacao=questao.explicacao
    )

    db.add(nova_questao)
    db.commit()
    db.refresh(nova_questao)

    for alt in questao.alternativas:

        alternativa = Alternativa(
            questao_id=nova_questao.id,
            codigo=alt.codigo,
            texto=alt.texto
        )

        db.add(alternativa)

    db.commit()

    return {
        "mensagem": "Questão criada com sucesso",
        "id": nova_questao.id
    }


@app.get("/questoes")
def listar_questoes(
    db: Session = Depends(get_db)
):
    return db.query(Questao).all()

@app.get("/questao-completa/{questao_id}")
def obter_questao_completa(
    questao_id: int,
    db: Session = Depends(get_db)
):
    questao = db.query(Questao).filter(
        Questao.id == questao_id
    ).first()

    if not questao:
        return {
            "erro": "Questão não encontrada"
        }

    alternativas = db.query(
        Alternativa
    ).filter(
        Alternativa.questao_id == questao_id
    ).all()

    return {
        "id": questao.id,
        "categoria_id": questao.categoria_id,
        "tipo": questao.tipo,
        "enunciado": questao.enunciado,
        "resposta_correta": questao.resposta_correta,
        "explicacao": questao.explicacao,
        "alternativas": [
            {
                "codigo": a.codigo,
                "texto": a.texto
            }
            for a in alternativas
        ]
    }

@app.get("/simulado/{quantidade}")
def gerar_simulado(
    quantidade: int,
    db: Session = Depends(get_db)
):

    questoes = db.query(Questao).all()

    if quantidade > len(questoes):
        quantidade = len(questoes)

    sorteadas = random.sample(
        questoes,
        quantidade
    )

    resultado = []

    for questao in sorteadas:

        alternativas = db.query(
            Alternativa
        ).filter(
            Alternativa.questao_id == questao.id
        ).all()

        resultado.append({
            "id": questao.id,
            "tipo": questao.tipo,
            "enunciado": questao.enunciado,
            "alternativas": [
                {
                    "codigo": a.codigo,
                    "texto": a.texto
                }
                for a in alternativas
            ]
        })

    return resultado

@app.post("/corrigir")
def corrigir_prova(
    respostas: list[RespostaUsuario],
    db: Session = Depends(get_db)
):

    acertos = 0
    erros = 0

    detalhes = []

    for item in respostas:

        questao = db.query(
            Questao
        ).filter(
            Questao.id == item.questao_id
        ).first()

        if not questao:
            continue

        correto = (
            item.resposta.upper()
            == questao.resposta_correta.upper()
        )

        if correto:
            acertos += 1
        else:
            erros += 1

        detalhes.append({
            "questao_id": item.questao_id,
            "resposta_usuario": item.resposta,
            "resposta_correta": questao.resposta_correta,
            "correto": correto
        })

    total = acertos + erros

    nota = 0

    if total > 0:
        nota = round(
            (acertos / total) * 100,
            2
        )

    return {
        "acertos": acertos,
        "erros": erros,
        "nota": nota,
        "detalhes": detalhes
    }