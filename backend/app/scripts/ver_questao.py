import re

ARQUIVO = "aws_saa_texto.txt"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:
    texto = f.read()

blocos = re.split(
    r"Answer:\s*([A-D])",
    texto
)

bloco = blocos[0]

print(bloco[:5000])