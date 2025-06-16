import cv2
import numpy as np
import matplotlib.pyplot as plt

# processo padrão de ler a imagem e criar um canva vazio
img = cv2.imread(r'assets\fotos\cats.jpg')
cv2.imshow('gatis', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

# primeiro vamos calculaar o histograma da imagem em cinza
# converter  a imagem para P&B
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('cinza', cinza)

# Histograma de Preto&Branco
# cv2.calcHist(imagem, canais_de_cor(RGB, BGR), mascara, tamanho_do_list, ranges)
cinza_hist = cv2.calcHist([cinza], [0], None, [255], [0, 256])
# plotando a imagem desse nosso histograma baisoc das escalas de cinza


plt.figure()
plt.title('Histograma de escalas de cinza, sem mascara')
plt.xlabel('Intervalos/setores')
plt.ylabel('Numeros de pixels')
plt.plot(cinza_hist)
plt.xlim([0,256])
plt.show()


plt.figure()
plt.title('Histograma de cores, sem mascara')
plt.xlabel('Intervalos/setores')
plt.ylabel('Numeros de pixels')
colors = ['b', 'g', 'r']
for channel, cor in enumerate(colors):    # ver cada canal e cada cor no 'colors'
    hist = cv2.calcHist([img], [channel], None, [256], [0,256])
    plt.plot(hist, color=cor)
    plt.xlim([0,256])

plt.show()




cv2.waitKey(0)