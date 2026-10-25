import re

ARQUIVO = "aws_saa_texto.txt"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:
    texto = f.read()

primeira = re.split(
    r"Answer:\s*[A-D]",
    texto
)[0]

a = re.search(r"A\.(.*?)B\.", primeira, re.S)
b = re.search(r"B\.(.*?)C\.", primeira, re.S)
c = re.search(r"C\.(.*?)D\.", primeira, re.S)

print("=" * 80)
print("ALTERNATIVA A")
print("=" * 80)

if a:
    print(a.group(1).strip())

print("\n" + "=" * 80)
print("ALTERNATIVA B")
print("=" * 80)

if b:
    print(b.group(1).strip())

print("\n" + "=" * 80)
print("ALTERNATIVA C")
print("=" * 80)

if c:
    print(c.group(1).strip())