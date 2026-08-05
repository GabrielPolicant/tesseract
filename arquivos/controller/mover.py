from arquivos.controller.configs import *

def mover_backup(caminho_documento):
    pasta_backup = pasta_atual / "backup"
    pasta_backup.mkdir(exist_ok=True)
    caminho_backup = pasta_backup / caminho_documento.name
    caminho_documento.rename(caminho_backup)
    print(f"[I] Documento movido para backup: {caminho_backup}")