import cv2
import numpy as np

# Cores -> BGR
azul = 255, 0, 0
verde = 0, 255, 0
vermelho = 0, 0, 255


# Ler as imagens

blank_img = np.zeros((500,500,3), dtype='uint8') # cria uma matriz de 500x500 com 3 canais de cor, uint8 é o tipo de dado, vai de 0 a 255
cv2.imshow('blank', blank_img) # Mostra a tela preta 500x500

cat = cv2.imread(r'assets\fotos\cat.jpg')

# 1. Pintar o blank por operação matricial

# pintar toda a matriz
# blank_img[:] = vermelho  # Pintando a imagem inteira de vermelho
# blank_img[:] = verde  # Pintando a imagem inteira de verde
# blank_img[:] = azul  # Pintando a imagem inteira de azul

# blank_img[200:300, 300:400] = vermelho # Pintando uma parte especifica da imagem
# blank_img[:100, 50:150] = verde
# blank_img[400:, 200:300] = azul

# 2. Desenhar formas

# Retangulo
# cv2.rectangle(blank_img, (10,10),(250,250), verde, 3) # (imagem, ponto inicial, ponto final, cor, espessura) -1 é cheio

# cv2.rectangle(blank_img, (30,30), (blank_img.shape[1]//2, blank_img.shape[0]//2), vermelho, 3) 
# vértice superior-esquerdo em (30, 30) e vértice inferior-direito no centro da imagem. shape[1] → largura, e shape[0] → altura.

# Circulo
# cv2.circle(blank_img, (blank_img.shape[1]//2, blank_img.shape[0]//2), 200, verde, 3) # (imagem, centro, raio (distancio do centro ate a ponta), cor, espessura)

# Linha
cv2.line(blank_img, (100,100), (blank_img.shape[1], blank_img.shape[0]), vermelho, 3) # (imagem, ponto inicial, ponto final, cor, espessura)

# 5. Escrever texto
cv2.putText(blank_img, "Eita Pega", (3,250), cv2.FONT_ITALIC, 1.5, (255,255,255),2) # (imagem, texto, ponto inicial, fonte, tamanho, cor, espessura)



cv2.imshow('blank', blank_img)



cv2.waitKey(0)