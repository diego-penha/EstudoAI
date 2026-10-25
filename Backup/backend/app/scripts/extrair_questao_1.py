import re

ARQUIVO = "aws_saa_texto.txt"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:
    texto = f.read()

match = re.search(
    r"(.*?)Answer:\s*([A-D])",
    texto,
    re.S
)

if match:
    bloco = match.group(1)
    resposta = match.group(2)

    print("=" * 80)
    print("RESPOSTA")
    print("=" * 80)
    print(resposta)

    print("\n")

    print("=" * 80)
    print("BLOCO")
    print("=" * 80)
    print(bloco)