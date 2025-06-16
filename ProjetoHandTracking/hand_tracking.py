import cv2
import mediapipe as mp
import numpy as np
import time

###

confidence = float
webcam_image = np.ndarray
rgb_tuple = tuple[int, int, int]
# coords_vector = 

# Classe
class Detector:
    def __init__(self, 
                 mode: bool = False,
                 number_hands: int = 2,
                 model_complexity: int = 1,
                 min_detec_confidence: confidence = 0.5,
                 min_tracking_confidence: confidence = 0.5):
        # Parametros necessarios para inicar o hands
        self.mode = mode
        self.max_num_hands = number_hands
        self.complexity = model_complexity
        self.detection_con = min_detec_confidence
        self.tracking_con = min_tracking_confidence

        # Inicializar o hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode,
                                        self.max_num_hands,
                                        self.complexity,
                                        self.detection_con,
                                        self.tracking_con)
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]


    def find_hands(self,
                   img: webcam_image,
                   draw_hands: bool = True):
        # Correção de cor
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Coletar resultados do processo das hands e analisar
        self.results = self.hands.process(img_RGB)  # Conversão feita pois .process() não processa imagens BGR

        if self.results.multi_hand_landmarks and draw_hands:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HAND_CONNECTIONS)
                
        return img    

    def find_position(self,
                      img: webcam_image,
                      hand_number: int = 0):
        self.required_landmark_list = []
        my_hand = None
        if self.results.multi_hand_lardmarks:
            height, width, _ = img.shape
            my_hand = self.results.multi_hand_landmarks[hand_number]
            for id, lm in enumerate(my_hand.landmark):
                center_x, center_y = int(lm.x * width), int(lm.y * height)

                self.required_landmark_list.append([id, center_x, center_y])
                
            
        return my_hand



# Teste de classe #
# Este bloco só executa quando o arquivo é rodado diretamente (python hand_tracking.py)
# Se o arquivo for importado em outro programa, este código não será executado
if __name__ == '__main__': 
    Detec = Detector()  # Cria uma instância da classe Detector para detectar mãos

    capture = cv2.VideoCapture(0)

    while True:
        # Captura do frame
        _, img = capture.read()

        # Manipulação de frame
        img = Detec.find_hands(img)
        landmark_list = Detec.find_position(img)
        if landmark_list:
            print(landmark_list[8])

        # Mostrando o frame
        cv2.imshow('WebCam :O', img)


        if cv2.waitKey(20) & 0xFF==ord('q'):
            break