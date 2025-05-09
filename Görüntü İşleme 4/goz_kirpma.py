import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)


BLINK_THRESOLD = 0.25
blink_counter=0
blink_toplam=0

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def calcute_EAR(eye_points,landmarks,image_w,image_h):
    p1= np.array([landmarks[eye_points[1]].x * image_w, landmarks[eye_points[1]].y * image_h])
    p2= np.array([landmarks[eye_points[2]].x * image_w, landmarks[eye_points[2]].y * image_h])
    p3= np.array([landmarks[eye_points[5]].x * image_w, landmarks[eye_points[5]].y * image_h])
    p4= np.array([landmarks[eye_points[4]].x * image_w, landmarks[eye_points[4]].y * image_h])

    p0= np.array([landmarks[eye_points[0]].x * image_w, landmarks[eye_points[0]].y * image_h])
    p3b= np.array([landmarks[eye_points[3]].x * image_w, landmarks[eye_points[3]].y * image_h])

    vertical1 = np.linalg.norm(p2-p4)
    vertical2 = np.linalg.norm(p1-p3)

    horizontal = np.linalg.norm(p0-p3b)

    EAR = (vertical1 + vertical2) / (2.0 * horizontal)
    return EAR

cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    h,w,_ = frame.shape

    if results.multi_face_landmarks:
        landmarks= results.multi_face_landmarks[0].landmark

        left_ear = calcute_EAR(LEFT_EYE,landmarks,w,h)
        right_ear = calcute_EAR(RIGHT_EYE,landmarks,w,h)

        avg_ear = (left_ear + right_ear) / 2.0

        if avg_ear < BLINK_THRESOLD:

            blink_counter += 1
        else:
            if blink_counter > 2:
                blink_toplam += 1
            blink_counter = 0
        
        cv2.putText(frame, f"Kirpma Sayisi: {blink_toplam}",(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("Mediapipe Goz Algilama",frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()