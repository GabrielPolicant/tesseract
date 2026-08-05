from arquivos.controller.configs import *
from arquivos.controller.tratamento import pdf_para_imagem, tratando_imagem, extrair_texto
from arquivos.controller.mover import mover_backup

def main():

    print("[I] Iniciando o programa de extração de texto de documentos PDF.")

    try:

        caminho_documentos = os.listdir(pasta_atual / "docs")
        if not caminho_documentos:
            print("[E] Nenhum arquivo encontrado na pasta 'docs'.")
            raise FileNotFoundError("Nenhum arquivo encontrado na pasta 'docs'.")

        for item in caminho_documentos:
            caminho_documento = pasta_atual / "docs" / item

            if not caminho_documento.exists():
                print(f"[E] Arquivo não encontrado: {caminho_documento}")
                raise FileNotFoundError(f"Nenhum arquivo encontrado: {caminho_documento}.")

            pergunta = input(f"[I] Deseja processar o documento {caminho_documento.name}? (S/N) ").strip().upper()
            if pergunta != "S":
                break

            print(f"[I] Processando o documento: {caminho_documento}")
            print("[I] Tratando o documento para melhorar a extração de texto.")

            imagem = pdf_para_imagem(caminho_documento)
            imagem_tratada = tratando_imagem(imagem)
            texto = extrair_texto(imagem_tratada)

            print(texto)

            question = input("[I] Deseja mover o documento para a pasta de backup? (S/N) ").strip().upper()
            if question == "S":
                mover_backup(caminho_documento)

    except Exception as e:
        print(f'[E] Erro na hora de executar o programam, erro: {e}.')

if __name__ == "__main__":
    main()