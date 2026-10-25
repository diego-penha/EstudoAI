import sys
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from app.database.database import SessionLocal

from app.models.categoria import Categoria
from app.models.questao import Questao
from app.models.alternativa import Alternativa

ARQUIVO = "aws_saa_texto.txt"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:
    texto = f.read()

partes = re.split(
    r"Answer:\s*([A-D])",
    texto
)

db = SessionLocal()

importadas = 0

# começamos da questão 2 para ignorar a capa
for i in range(3, len(partes), 2):

    resposta = partes[i].strip()
    bloco = partes[i - 1]

    if importadas >= 1016:
        break

    try:

        a = bloco.rfind("A.")
        b = bloco.rfind("B.")
        c = bloco.rfind("C.")
        d = bloco.rfind("D.")

        if min(a, b, c, d) < 0:
            continue

        enunciado = bloco[:a]

        enunciado = re.sub(r"\s+", " ", enunciado)
        enunciado = enunciado.strip()

        alt_a = re.sub(r"\s+", " ", alt_a).strip()
        alt_b = re.sub(r"\s+", " ", alt_b).strip()
        alt_c = re.sub(r"\s+", " ", alt_c).strip()
        alt_d = re.sub(r"\s+", " ", alt_d).strip()

        questao = Questao(
            categoria_id=1,
            tipo="multipla_escolha",
            enunciado=enunciado,
            resposta_correta=resposta,
            explicacao=""
        )

        db.add(questao)
        db.commit()
        db.refresh(questao)

        alternativas = [
            ("A", alt_a),
            ("B", alt_b),
            ("C", alt_c),
            ("D", alt_d)
        ]

        for codigo, texto_alt in alternativas:

            alt = Alternativa(
                questao_id=questao.id,
                codigo=codigo,
                texto=texto_alt
            )

            db.add(alt)

        db.commit()

        importadas += 1

    except Exception as e:
     db.rollback()
     print(f"Erro: {e}")

print(f"\nQuestões importadas: {importadas}")