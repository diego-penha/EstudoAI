from pypdf import PdfReader

ARQUIVO = "uploads/SAA-C03.pdf"

reader = PdfReader(ARQUIVO)

print(f"Total de páginas: {len(reader.pages)}")

for pagina in range(5):
    print("\n" + "=" * 80)
    print(f"PÁGINA {pagina + 1}")
    print("=" * 80)

    texto = reader.pages[pagina].extract_text()

    print(texto[:3000])