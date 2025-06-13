'''
Nessa aula vamos criar funções para que possamos manupular algumas imagens a partir de alguns conceitos básicos

1. Translation(translação): Além de ser o movimento que a terra realiza em torno do sol, também é o ato de movimentar um objeto de um ponto ao outro
2. Rotation: Rotaciona/gira a imagem 
3. Resize: Redimenciona a imagem
4. Flipping: Inverte a imagem, um exemplo clássico são as câmeras de selfie de celulares
5. Cropping: O ato de cortar as imagens a partir de coordenadas

Utilizaremos muito uma função chamada warpAffine do cv2. Há imagens em assets/didaticas - affine_transformation.png e warp_affine_theory.jpg - que explica melhor
Mas em suma, qualquer transformação linear em uma série de pontos pode ser descrita por uma matriz seguida de um vetor de adição
É apenas um conceito algébrico. Referências: https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html

'''

import cv2
import numpy as np


img = cv2.imread(r'assets\fotos\park.jpg')
cv2.imshow('', img)

## Definições de funções ##

# 1. Translation
def translate(img, x, y):         # -x esquerda, x direita, -y cima, y baixo       O eixo principal da imagem, esta no canto superior esquerdo

    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])   # Criandp uma matriz usando numpy, aceitando apenas numeros float de 32 bits

    # coletando as dimensões da imagem
    dimensions = (img.shape[1], img.shape[0])   # tupla onde pega o numero de colunas e linhas, respectivamente

    # retornar a função warpAffine
    return cv2.warpAffine(img, translation_matrix, dimensions)


# Chamando a função translate
# img_tr = translate(img, 100, 250)   # translate(img, -x(esquerda) x(direita), -y(cima) y(baixo))
# cv2.imshow('Imagem Transladada', img_tr)


def rotate(img, angle, rotation_point=None):      # Rotation Point, posso escolher o ponto em que a imagem gira, seja no meio ou no ponto, em qualquer lugar
    height, width = img.shape[:2]  # pega altura e largura da imagem ([:2] pega só os 2 primeiros valores do shape, ignorando os 3 canais de cor RGB)

    if rotation_point is None:
        rotation_point = (width//2, height//2)   # calcula o ponto central da imagem (metade da largura, metade da altura)
        #Floor division, se caso dividir 17//2, vai dar 8.5, mas ela vai retornar 8. Sempre pega o menor numero inteiro

    # Pegar a matriz de rotação 2D(ponto_de_rotação, angulo, escala)
    rotation_matrix = cv2.getRotationMatrix2D(rotation_point, angle, 1.0)   # recomenda-se usar sempre a escala 1.0
    dimensions = (width, height)

    return cv2.warpAffine(img, rotation_matrix, dimensions)


# rotacionada = rotate(img, -45) # girando a imagem em -45°
# cv2.imshow('imagem rotacionada', rotacionada)


# Flipping: Inverte um array 2D     Função já feita na biblioteca cv2
flip = cv2.flip(img, 1)   # horizontal
flip = cv2.flip(img, 0)   # vertical
flip = cv2.flip(img, -1)   # vertical e horizontal

# cv2.imshow('Flipadas', flip)


# Resizing & Cropping: recapitulação     Função já feita na biblioteca cv2
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)     #resize(img, dimensão, tipo de interpolação)   INTER_CUBIC, mais lenta mas trás mais qualidade

# cv2.imshow('resize', resized)

# Cortando a imagem: [altura_inicio:altura_fim, largura_inicio:largura_fim]
cropped = img[100:400, 200:500]  # corta um retângulo da imagem: da linha 100 até 400 e da coluna 200 até 500

# cv2.imshow('cropped', cropped)


cv2.waitKey(0)