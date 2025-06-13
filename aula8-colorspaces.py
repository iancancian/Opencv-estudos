import cv2
import numpy as np

## Aula de transição do básico para o avançado ##
# O que é: BGR, RGB, CMYK, LAB, HSV e etc. Quais são os usos do colos spaces, por que existem espaços de cores diferentes. #
# CMYK : Cyan, Magenta, Yellow, Black
# Cada pixel do computador tem 3 representações, Red Green Blue
# RGB -> Normalmente é o padrão de uso
# BGR -> Padrão de uso do OpenCV

img = cv2.imread(r'assets\fotos\cat.jpg')

# BGR para grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('cinza', gray)


# BGR para HSV --- Muito usado para visão noturna
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)


# BGR para L*a*b --- Outro tipo de esquema de cores (pesquisar 'esquema de cor l*a*b')
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('L*a*b', lab)


# BGR para RGB --- Pega a tupla que esta em BGR e converte diretamente para RGB   ex: BGR(255,0,0) -> RGB(0,0,255)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)


# Possivel fazer a operação inversa tmb, por exemplo, LAB para BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('lab -> bgr', lab_bgr)


cv2.waitKey(0)