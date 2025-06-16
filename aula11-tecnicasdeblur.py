import cv2
import numpy as np


img = cv2.imread(r'assets\fotos\cats.jpg')
cv2.imshow('img padrao', img)

# Blur por media
average = cv2.blur(img, (6,6)) # cv2.blur(imagem, kernel_size) -ver aula5, breve anotação-  Neste caso, ele faz a média das cores dos 6 pixels no eixo x e y 
cv2.imshow('blur por media', average)

# Gaussian Blur
'''
    A aplicação de uma funçã matemática a uma imagem para borrá-la
    É como colocar um material translúcido como pergaminho sobre a imagem
    Pegar um papel manteiga e tentar enchergar a imagem
'''
gauss = cv2.GaussianBlur(img, (7,7), 0) # Não deixa de ser uma função matemática
cv2.imshow('gaussian blur', gauss)

# Blur por mediana
'''
    A média é a soma dos valores dividida pelo número de observações, enquanto a mediana é o valor central quando os dados são ordenados
    A média é sensível a valores extremos, já a mediana não.
    Segue os principios do blur por media, quanto maior o ksize, maior o blur
    Tem uma pegada de desfoque diferente do blur por média, parece que desfoca em flocos, não como estamos acostumados
'''

median = cv2.medianBlur(img, 9)
cv2.imshow('median blur', median)

# Filtro Bilateral
# Edge preserving denoising filter
'''
    Um filtro bilateral é um filtro de suavização não linear, com preservação de bordas e redução de ruído para imagens.
    Ele substitui a intensidade de cada pixel por uma média ponderada dos valores de intensidade dos pixels proximos.
    Visto que esse efeito reduz o ruído, testaremos com uma imagem com ruído.

    Primeiro temos que entender o que é Sigma, no contexto de processamento de imagem:
    Sigma define a quantidade de desfoque

    cv2.bilateralFilter(imagem, d, sigmaColor, sigmaSpace)
    d -> kernel size ou ksize (que é o diametro de analise do modelo), quanto menor, mais custosa a análise
    sigmaColor -> FIltra o Sigma no ColorSpace(RGB, BGR, YMCK, etc)
        Um valor maior do parâmetro significa que as cores mais distantes dentro da vizinhança do pixel serão misturadas, resultando em áreas maiores de cor semi-igual
    sigmaSpace -> Filtra o Sigma no espaço de coordenadas.
        Um valor maior do parâmetro significa que os pixels mais distantes influenciarão uns anos outros (desde que suas cores sejam proximas o suficiente)
'''

img_noisy = cv2.imread(r'assets\fotos\noisy_image.jpg')
cv2.imshow('img com ruido', img_noisy)

bilateral = cv2.bilateralFilter(img_noisy, 15, 75, 75)
cv2.imshow('FiltroBilateral', bilateral)





cv2.waitKey(0)