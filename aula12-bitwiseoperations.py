import cv2
import numpy as np

# Criar um canva preto
blank = np.zeros([400, 400], dtype='uint8')
# cv2.imshow('blank', blank)
 
# IMPORTANTE: utilizar funções copy para não ter problema de alterar duas matrizes simultaneamente

rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1) # blank.copy() -> altera uma copia do quadro preto   (ponto 1 do retangulo), (ponto 2), cor, thickness
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)  # (centro do circulo -como o quadro é 400x400, o circulo vai estar no centro), raio, cor, thickness

cv2.imshow('Ret', rectangle)
cv2.imshow('Cir', circle)


# Bitwise AND (&&) -> intersecção das dias imagens (onde ambos são 1 [brancos])
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('and', bitwise_and)

# Bitwise OR (||) -> intersecção onde há qualquer um dos dois objetos envolvidos
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('or', bitwise_or)

# Bitwise XOR -> intersecção apenas nas areas onde há UM OU OUTRO
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('xor', bitwise_xor)

# Bitwise NOT -> intersecção apenas onde não há nada (que tenha o valor 0)
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow('not', bitwise_not)




cv2.waitKey(0)