import cv2
import numpy as np

cap = cv2.VideoCapture(r'assets\videos\dog.mp4')

# Rescale e Resize são utilizados para nao perder qualidade da imagem

# Função que faz o rescale para cada frame individualmente
def rescale_frame(frame: np.array,
                  scale: float = 0.75):
    largura = int(frame.shape[1] * scale) # 'shape' retora uma tupla com largura e altura (x,y)
    altura = int(frame.shape[0] * scale) # [1] = largura  [0] = altura

    return cv2.resize(frame, (largura,altura), interpolation=cv2.INTER_AREA) # INTER_AREA é o tipo de interpolação que para manter a qualidade quando você precisa redimensionar uma imagem

def resize_frame(frame: np.array,
                 width: int, 
                 height: int):
    # Redimensiona o frame para as dimensões especificadas
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

# IMAGEM - scale resize +==============================================
img = cv2.imread(r'assets\fotos\cat_large.jpg')
cv2.imshow('not_resized_cat', img) # mostrando a imagem sem redimensionar

resized_img = rescale_frame(img,0.2) #enviando a imagem, e o scale é 0.2, que é a porcentagem de redução da imagem
cv2.imshow('resized_cat', resized_img) # mostrando a imagem redimensionada

# cv2.waitKey(0)

# LIVE VIDEO - scale resize +==============================================
while True:
    _, frame = cap.read() # lendo o video especificado na linha 4

    cv2.imshow('dog_not_resized', frame)
    
    # frame -> frame_resized
    frame_resized = rescale_frame(frame,0.5) 
    # frame_resized = resize_frame(frame, 100, 100)  # Agora você pode usar esta função para redimensionar para dimensões específicas

    cv2.imshow('dog_resized', frame_resized)

    if cv2.waitKey(20) & 0xFF == ord('q'): 
        break