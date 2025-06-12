import cv2

# Para ler os vídeos, temos que criar um objeto de captura 
# Função VideoCapture() 
cap = cv2.VideoCapture(r'assets\videos\dog.mp4')

while True: # Loop para ler todos os frames do video
    _, frame = cap.read() # Lê o vídeo

    cv2.imshow('Video', frame)

    
    # WaitKey para videos
    if cv2.waitKey(20) & 0xFF == ord('q'): #
        break

cap.release() # Libera o vídeo quando acabar
cv2.destroyAllWindows() # Fecha todas as janelas