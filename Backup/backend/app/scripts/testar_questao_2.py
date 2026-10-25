import re

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

# Questão 2
bloco = partes[2]
resposta = partes[3]

a = bloco.rfind("A.")
b = bloco.rfind("B.")
c = bloco.rfind("C.")
d = bloco.rfind("D.")

enunciado = bloco[:a].strip()
alt_a = bloco[a:b].strip()
alt_b = bloco[b:c].strip()
alt_c = bloco[c:d].strip()
alt_d = bloco[d:].strip()

print("=" * 80)
print("ENUNCIADO")
print("=" * 80)
print(enunciado)

print("\n" + "=" * 80)
print("ALT A")
print("=" * 80)
print(alt_a)

print("\n" + "=" * 80)
print("ALT B")
print("=" * 80)
print(alt_b)

print("\n" + "=" * 80)
print("ALT C")
print("=" * 80)
print(alt_c)

print("\n" + "=" * 80)
print("ALT D")
print("=" * 80)
print(alt_d)

print("\n" + "=" * 80)
print("RESPOSTA")
print("=" * 80)
print(resposta)