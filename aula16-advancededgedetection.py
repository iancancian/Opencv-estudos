import cv2
import numpy as np

img = cv2.imread(r'assets\fotos\park.jpg')

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem em cinza', cinza)


# Método LAPLACIANO
# cv2.Laplacian(imagem, data_depth)
laplaciano = cv2.Laplacian(cinza, cv2.CV_64F)
# print(laplaciano) # Gera uma matriz de intensidade de pixels em uma imagem

# calcular o valor absoluto por elemento e converter para uint8 (0 a 255)
laplaciano = np.uint8(np.absolute(laplaciano)) # pega apenas os numeros positivos. refatora a imagem para mostrar no imshow()
cv2.imshow('Laplaciano refatorado', laplaciano)


# Método de SOBEL
# cv2.Sobel(imagem, datadepth, dx, dy) onde dx e dy representam as direcoes x e y]
x = cv2.Sobel(cinza, cv2.CV_64F, 1, 0)
y = cv2.Sobel(cinza, cv2.CV_64F, 0, 1)

# resoltados separados das derivadas com o metodo sobel
cv2.imshow('SOBEL X', x)
cv2.imshow('SOBEL Y', y)

# combinar x e y em uma bitwise operation
combined_sobel = cv2.bitwise_or(x, y)
cv2.imshow('Sobel combinado x+y', combined_sobel)


# Método de CANNY (trazendo apenas por comparação)
canny = cv2.Canny(cinza, 150, 175)
cv2.imshow('Filtro Canny', canny)


# CADA FILTRO É USADO PARA CASOS ESPECÍFICOS


cv2.waitKey(0)