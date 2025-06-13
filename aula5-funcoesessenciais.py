import cv2
import numpy as np

#lendo a imagem - lida em 3 canais (RGB)
img = cv2.imread(r'assets\fotos\cat.jpg')
img2 = cv2.imread(r'assets\fotos\park.jpg')

# O openCV trabalha com BGR

# 1. Converter para preto e branco (grayscale) ---------------------------------------------

cv2.imshow('gato normal', img) # mostrando a imagem antes da formatação
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convertColor(imagem, COLOR_BGRPARACINZA)
# cv2.imshow('gato cinza', cinza) # 'cinza' objeto convertido para cinza


# 2. Blur ---------------------------------------------

# cv2.GaussianBlur (imagem, ksize, sigmaX)   mais avançado, ksize - tupla de 2 itens impares, sigmaX - valor default do openCV. Mais avançado, sera explicado melhor em outra aula
blurred = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT) # Quanto maior o ksize, mais borrada imagem fica
# cv2.imshow('blurred', blurred) # nome da janela, e o objeto a ser mostrado

# 3. Edge Cascade - detecção de borda, processamento de imagem para encontrar os limites de objetos dentro da imagem ---------------------------------------------

# cv2.Canny(imagem, threshold1, threshold2) - quanto menor o valor de threshold, mais sensível é a detecção de borda. Mais avançado, sera explicado melhor em outra aula
canny = cv2.Canny(img, 250, 200) # teste (blurred, 20, 50)
# cv2.imshow('canny1', canny)

# para melhorar a detecção de borda, podemos borrar a imagem antes de aplicar o canny
canny_blurred = cv2.Canny(blurred, 250, 200) 
cv2.imshow('canny blurred', canny_blurred)


# 4. Dilating Imagem - Dilatação de imagem, aumentar o tamanho e espessura do objeto ----------------------------

dilatada = cv2.dilate(canny_blurred, (9,9), iterations=3) 
# (9,9) - tupla de 2 tamanhos, mesma ideia do ksize   iterations - quantas vezes a dilatação será aplicada
cv2.imshow('dilatada', dilatada)
# Muito útil para a interpretaçãp das imagens, o computador não precisa ver uma imagem bonitinha


# 5. Eroding Image - Corroendo a imagem, processo contrário da dilatação ----------------------------------
eroded = cv2.erode(dilatada, (9,9), iterations=3)
cv2.imshow('corroida', eroded)


# 6. Resize - Redimensionar a imagem ----------------------------------

resized = cv2.resize(img, (300,300))
cv2.imshow('resized', resized)


#7. Crop - Cortar a imagem ----------------------------------

corte = img[50:200, 200:400]    # primeiro trata da linha, depois da coluna (matriz) 
# Corta do pixel 50 até o 200 da linha, e do pixel 200 até o 400 da coluna
cv2.imshow('corte de matriz', corte)


# 8. é possivel fazer operaçãos direto no imshow() ----------------------------------

cv2.imshow('corte direto', img[50:200, 200:400])




cv2.waitKey(0)