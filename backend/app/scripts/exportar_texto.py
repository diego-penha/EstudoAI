from pypdf import PdfReader

ARQUIVO = "uploads/SAA-C03.pdf"

reader = PdfReader(ARQUIVO)

with open(
    "aws_saa_texto.txt",
    "w",
    encoding="utf-8"
) as arquivo:

    for pagina in reader.pages:

        texto = pagina.extract_text()

        if texto:
            arquivo.write(texto)
            arquivo.write("\n\n")

print("Texto exportado com sucesso!")