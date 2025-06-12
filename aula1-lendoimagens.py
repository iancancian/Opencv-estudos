import cv2

# Função imread() # Lê a imagem
img = cv2.imread(r'assets\fotos\cat.jpg')
img_grande = cv2.imread(r'assets\fotos\cat_large.jpg')

# Função imshow() # Mostra a imagem
# cv2.imshow('Gato', img)
cv2.imshow('Janelão do gato', img_grande)  # A tela no windows nao vai se adaptar ao tamanho



# Função waitKey()   # Espera tecla 0 para fechar 
cv2.waitKey(0)