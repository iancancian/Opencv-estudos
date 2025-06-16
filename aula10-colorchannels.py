import cv2
import numpy as np


# Color channels são as componentes individuais de cor que compõem uma imagem digital, permitindo a manipulação e análise separada de cada componente de cor (RGB) para processamento de imagem.. Ela trabalha com os componentes de cor da imagem de forma mais granular.


img =  cv2.imread(r'assets\fotos\park.jpg')
cv2.imshow('fim de semana no parque', img)

# Criando tela preta
blank = np.zeros(img.shape[:2], dtype='uint8') # no uint, quanto menor o numero, menos memória estamos utilizando

# Desintegrando a img #
b, g, r = cv2.split(img)
# cv2.imshow('blue', b)  # cada um, mostra a intensidade de cada cor que tem na imagem
# cv2.imshow('green', g)
# cv2.imshow('red', r)


# Reintegrando os canais de cor

blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

cv2.imshow('blue', blue)  
cv2.imshow('green', green)
cv2.imshow('red', red)
# Aqui conseguimos entender melhor onde cada esquema de cor está presente na img

# print(img.shape) # (linhas, colunas, 3 canais de cor), ou seja, 3 camadas de cor que formam a imagem 
# print(b.shape) # (linhas, colunas)
# print(g.shape) # (linhas, colunas)
# print(r.shape) # (linhas, colunas)


# Reintegrando a img #
merged = cv2.merge([b,g,r]) # Juntando novamente os canais
cv2.imshow('coresjuntasnovamente', merged)
print(merged.shape) # será identico ao img.shape



cv2.waitKey(0)