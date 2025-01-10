import cv2 as cv
from hand_detector import HandDetector

def main():
    # Inicializa a captura de vídeo (Webcam)
    cap = cv.VideoCapture(0)  # Altere o índice para outra câmera ou fonte de vídeo
    
    if not cap.isOpened():
        print("Erro: Não foi possível acessar a câmera.")
        return
    
    # Inicializa o detector de mãos
    hand_detector = HandDetector(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    print("Pressione 'q' para sair.")

    try:
        while True:
            # Lê o frame da câmera
            success, frame = cap.read()
            if not success:
                print("Erro ao capturar o frame.")
                break

            # Detecta mãos no frame
            results = hand_detector.detect_hands(frame)

            # Desenha os landmarks das mãos no frame
            hand_detector.draw_hands(frame, results)

            # Exibe o frame com as detecções
            cv.imshow("Teste Hand Detector", frame)

            # Sai ao pressionar a tecla 'q'
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Libera recursos
        cap.release()
        cv.destroyAllWindows()
        hand_detector.close()

if __name__ == "__main__":
    main()
