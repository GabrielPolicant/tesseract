from pathlib import Path
import pytesseract
import cv2  # opencv

path_tesseract = rf'C:\Users\gabri\AppData\Local\Programs\Tesseract-OCR'

# Passo 1: Ler a nossa imagem
pasta_atual = Path(__file__).resolve().parent #Pasta atual que o nosso código se encontra
caminho_imagem = pasta_atual / "img" / "renda_sicredi_2019.jpg"
imagem = cv2.imread(str(caminho_imagem))

# Passo 2: Extrair o texto da imagem

texto_imagem = pytesseract.image_to_string(imagem)
print(texto_imagem)