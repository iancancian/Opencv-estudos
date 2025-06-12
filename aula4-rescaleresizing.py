import cv2
import numpy as np

cap = cv2.VideoCapture(r'assets\videos\dog.mp4')

# Rescale e Resize são utilizados para nao perder qualidade da imagem

# Função que faz o rescaçe para cada frame individualmente
def rescale_frame(frame: np.array,
                  scale: float = 0.75):
    largura = int(frame.shape[1] * scale) # 'shape' retora uma tupla com largura e altura (x,y)
    altura = int(frame.shape[0] * scale)

    cv2.resize(frame, (largura,altura), interpolation=cv2.INTER_AREA)