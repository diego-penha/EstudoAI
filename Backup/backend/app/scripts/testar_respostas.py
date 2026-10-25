import re

ARQUIVO = "aws_saa_texto.txt"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:
    texto = f.read()

respostas = re.findall(
    r"Answer:\s*([A-D])",
    texto
)

print(f"Respostas encontradas: {len(respostas)}")

print("\nPrimeiras 20 respostas:")

for i, resposta in enumerate(respostas[:20], start=1):
    print(f"Questão {i}: {resposta}")