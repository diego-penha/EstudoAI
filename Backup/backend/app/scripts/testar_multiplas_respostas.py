ARQUIVO = "aws_saa_texto.txt"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:
    texto = f.read()

termos = [
    "Choose TWO",
    "Choose Two",
    "Select TWO",
    "Select Two",
    "Choose THREE",
    "Choose Three",
    "Select THREE",
    "Select Three"
]

for termo in termos:
    print(f"{termo}: {texto.count(termo)}")