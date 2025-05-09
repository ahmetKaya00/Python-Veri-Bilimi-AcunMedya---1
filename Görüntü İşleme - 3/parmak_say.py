import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)

while True:
    succes, img = cap.read()
    if not succes:
        continue
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []

            for id, lm in enumerate(hand_landmarks.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id,cx,cy))
            
            fingers = []

            if lm_list[4][1] > lm_list[3][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            
            finger_tips = [8,12,16,20]
            for tip in finger_tips:
                if lm_list[tip][2] < lm_list[tip - 2][2]:
                   fingers.append(1)
                else:
                    fingers.append(0) 
            
            total_fingers = sum(fingers)

            cv2.putText(img, f'Parmak Sayisi: {total_fingers}',(10,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

            mp_draw.draw_landmarks(img,hand_landmarks,mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Parmak Sayisi Tespiti",img)

    if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()
