import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:

    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            print("Kamera görüntüsü alınamadı!")
            break

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = face_detection.process(rgb_frame)

        if result.detections:
            for detection in result.detections:
                mp_drawing.draw_detection(frame, detection)
        
        cv2.imshow("Mediapipe ile Yuz Algilama",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()