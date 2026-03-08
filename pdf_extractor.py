import sys
import os
import PyPDF2

def extract(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return '\n'.join(page.extract_text() for page in reader.pages).strip()
    except Exception as e:
        raise ValueError(f"Erro ao ler o PDF: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].lower().endswith('.pdf'):
        print("Erro: informe um arquivo PDF.")
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.exists(path):
        print("Erro: arquivo não encontrado.")
        sys.exit(1)

    try:
        result = extract(path)
        print(result or "Erro: o PDF não contém texto extraível.")
        if not result:
            sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)