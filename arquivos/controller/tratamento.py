from arquivos.controller.configs import *

def tratando_imagem(imagem):

    imagem_maior = cv2.resize(imagem, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    imagem_cinza = cv2.cvtColor(imagem_maior, cv2.COLOR_BGR2GRAY)

    return imagem_cinza

def extrair_texto(imagem):

    texto = pytesseract.image_to_string(imagem, lang="por", config="--psm 6")

    return texto

def pdf_para_imagem(caminho_pdf):
    
    documento = fitz.open(caminho_pdf)
    pagina = documento[0]

    pix = pagina.get_pixmap()
    imagem = np.frombuffer(pix.samples, dtype=np.uint8)

    imagem = imagem.reshape(pix.height, pix.width, pix.n)
    imagem = cv2.cvtColor(imagem,cv2.COLOR_RGB2BGR)

    return imagem