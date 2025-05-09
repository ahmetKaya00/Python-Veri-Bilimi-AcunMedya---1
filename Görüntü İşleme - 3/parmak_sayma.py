import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)

def parmak_sayisi_al(sure=3):

    parmaklar = []
    baslangic = time.time()
    
    while time.time() - baslangic < sure:
        ret, img = cap.read()

        if not ret:
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
                
                toplam = sum(fingers)
                parmaklar.append(toplam)
    
        cv2.imshow("Parmak Okuma", img)
        if cv2.waitKey(1) & 0xFF == 27:
            return 0
    if parmaklar:
        return round(sum(parmaklar)/len(parmaklar))
    return 0

def mesaj_goster(mesaj, sure=2):
    baslangic = time.time()
    while time.time() - baslangic < sure:
        ret, img = cap.read()
        cv2.putText(img, mesaj,(50,200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                    (0,255,255), 2)
        cv2.imshow("Parmak Okuma",img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

mesaj_goster("1. Parmagi Goster",2)
ilk_parmak = parmak_sayisi_al(3)
mesaj_goster("Tamamdir",2)

mesaj_goster("2. Parmagi Goster",2)
ikinci_parmak = parmak_sayisi_al(3)
mesaj_goster("Tamamdir",2)

toplam = ilk_parmak + ikinci_parmak

while True:
    ret, img = cap.read()

    cv2.putText(img,f"1.Okuma: {ilk_parmak}",(50,100), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
    cv2.putText(img,f"2.Okuma: {ikinci_parmak}",(50,150), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
    cv2.putText(img,f"Toplam Parmak: {toplam}",(50,200), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

    cv2.imshow("Toplam Sonuc",img)
    if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
