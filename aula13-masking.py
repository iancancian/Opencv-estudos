import cv2
import numpy as np

# Masking é um recorte de região de interesse da imagem

img = cv2.imread(r'assets\fotos\cats.jpg')
cv2.imshow('gatos', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv2.imshow('blank', blank)


# Criando as formas
circle = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) #(setando as coordenadas do circulo)
rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
# cv2.imshow('cir', circle)
# cv2.imshow('rec', rectangle)

# Criando máscaras diferentes
recorte1 = cv2.bitwise_and(circle,rectangle)
recorte2 = cv2.bitwise_or(circle,rectangle)
recorte3 = cv2.bitwise_not(circle)

# cv2.imshow('recorte1', recorte1)
# cv2.imshow('recorte2', recorte2)
# cv2.imshow('recorte3', recorte3)

# Mostrando as mascarasv
mask1 = cv2.bitwise_and(img, img, mask=recorte1)   # por documentação, tem que passar 2x a img, e chama o parametro mask para recortar
mask2 = cv2.bitwise_and(img, img, mask=recorte2)
mask3 = cv2.bitwise_and(img, img, mask=recorte3)

cv2.imshow('mask1', mask1)
cv2.imshow('mask2', mask2)
cv2.imshow('mask3', mask3)


cv2.waitKey(0)