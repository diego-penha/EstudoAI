import re

ARQUIVO = "aws_saa_texto.txt"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:
    texto = f.read()

partes = re.split(
    r"(Answer:\s*[A-D])",
    texto
)

print("=" * 80)
print(partes[0][:8000])

print("\n")
print("=" * 80)
print("RESPOSTA")
print("=" * 80)
print(partes[1])