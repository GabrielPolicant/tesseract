from pathlib import Path

import cv2
import pytesseract
import fitz
import numpy as np
import os

path_tesseract = (r"C:\Users\gabri\AppData\Local\Programs\Tesseract-OCR\tesseract.exe")
pytesseract.pytesseract.tesseract_cmd = (path_tesseract)
pasta_atual = Path(__file__).resolve().parent.parent