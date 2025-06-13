import cv2
import numpy as np

## Processo padrão ##
# ler imagem
img = cv2.imread(r'assets\fotos\cats.jpg')
cv2.imshow('gatos', img) # mostrando a imagem original

# desenhando um quadro em branco do mesmo tamanho que a imagem de trabalho
blank = np.zeros(img.shape, dtype='uint8')
# cv2.imshow('blank', blank)

# transferindo-a para cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gatinhos cinzas', gray)

# 1. Detecção de contornos

# a. Borrar a imagem com o GaussianBlur
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('gatinhos borrados', blur)

#b. Função de Canny
canny = cv2.Canny(blur, 125, 175)
# cv2.imshow('gatinhos bordas canny', canny)

''' 
'For better accuracy, use binary images. So before finding contours, apply threshold or anny edge detection' Direto da documentação do OpenCV 

cv2.findContours(imagem, modo_detecção, metodo_aproximacao_contorno)

Modo de detecção:
  Recomendação -> cv2.RETR_LIST, recomendado pela propria documentação

Metodos de Aproximação de Contorno: 'Armazenam as coordenadas x e y do limite de uma forma'
  cv2.CHAIN_APPROX_NONE: Salva absolutamente todos os pontos de contorno, custoso (ocupa mais memória, mas é mais preciso), imagina se tivessemos uma linha, precisamos de todos os pontos ou apenas seus dois extremos?
  cv2.CHAIN_APPROX_SIMPLE: Ele remove todos os pontos redundantes e comprime o contorno, economizando memória.
  Exemplo em: assets/didaticas/metodo_aproximacao_contorno.jpg - Primeira imagem, precisou de 734 pontos pra detectar o contorno, já na segunda apenas 4.

  O USO DOS MÉTODOS DEPENDE DA APLICAÇÃO
'''

contornos, hier = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)   # (imagem, modo de detecção, método de aprox de cont)
print(f'{len(contornos)} contornos foram encontrados')

cv2.drawContours(blank, contornos, -1, (0, 0, 255), 1)   # nova função, (nosso quadro em branco, contornos, índice do contorno, (BGR), thickness do contorno)
cv2.imshow('contornos desenhados', blank)


cv2.waitKey(0)