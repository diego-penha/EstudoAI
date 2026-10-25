import re

ARQUIVO = "aws_saa_texto.txt"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:
    texto = f.read()

partes = re.split(r"Answer:\s*[A-D]", texto)

print(f"Blocos encontrados: {len(partes)}")

for i, bloco in enumerate(partes[:3], start=1):
    print("\n" + "=" * 80)
    print(f"QUESTÃO {i}")
    print("=" * 80)

    print(bloco[:1500])