import cv2

''' Thresholding
- Segmentação de imagens
- A partir de imagens em cinza, criamos imagens binárias
- Melhores condições:
    -> Ruído baixo
    -> Pixels de um mesmo grupo tem intensidades mais proximas entre si do que pixels de outro grupo
    -> Luz homogênea
'''

img = cv2.imread(r'assets\fotos\cats.jpg')
cv2.imshow('gatos', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('cinza gatinhos', gray)

'''
    Para os threshs simples, usaremos a função cv2.threshold()
    cv2.threshold(imagem, valor_de_thresh, max_val, metodo_de_thresholding)

metodo_de_thresholding:
    cv2.THRESH_BINARY: <- trabalharemos principalmente com esses dois *
    cv2.THRESH_BINARY_INV: <- trabalharemos principalmente com esses dois * 
    cv2.THRESH_TOZERO: 
    cv2.THRESH_TOZERO_INV: 

    
    Checar 'assets/didaticas/thresholding_methods' *
'''

# Thresholding simples
# É como uma linha divisória: tudo acima de 150 vira branco, tudo abaixo vira preto
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # O valor 150 é o limiar (threshold): pixels > 150 se tornam brancos (255), pixels <= 150 se tornam pretos (0)
# cv2.imshow('thresholding simples', thresh)

# Thresholding simples invertido (uso em casos específicos)
threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)  
# cv2.imshow('thresholding simples invertido', thresh_inv)


''' Adaptative Thresholding
cv2.adaptiveThreshold(imagem, valor_maximo, metodo_adaptativo, metodo_thresholding, tamanho_da_visinhança, constante_C)

metodo_adaptativo:
    cv2.ADAPTIVE_THRESH_MEAN_C: O valor limite é a média da área da vizinhança menos a constante C.
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C: O valor limite é uma soma ponderada gaussiana dos valores da vizinhança menos a constante C.
'''

# Thresholding adaptativo
adaptive_thresh_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
cv2.imshow('eita', adaptive_thresh_gaussian)

adaptive_thresh_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 9)
cv2.imshow('eita', adaptive_thresh_mean)




cv2.waitKey(0)