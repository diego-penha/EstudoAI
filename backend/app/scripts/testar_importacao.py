import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

import re

ARQUIVO = "aws_saa_texto.txt"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:
    texto = f.read()

blocos = re.split(
    r"Answer:\s*[A-D]",
    texto
)

respostas = re.findall(
    r"Answer:\s*([A-D])",
    texto
)

print(f"Blocos: {len(blocos)}")
print(f"Respostas: {len(respostas)}")

questoes_validas = 0

for bloco in blocos[1:]:

    if (
        "A." in bloco and
        "B." in bloco and
        "C." in bloco and
        "D." in bloco
    ):
        questoes_validas += 1

print(f"Questões válidas: {questoes_validas}")

from app.database.database import SessionLocal

print("Import OK")