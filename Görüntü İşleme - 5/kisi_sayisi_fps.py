import cv2
from ultralytics import YOLO
import time

model = YOLO("yolov5s.pt")
cv2.namedWindow("Insan Tespiti",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Insan Tespiti", 640,480)
cap = cv2.VideoCapture("video.mp4")
prev_time = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time else 0
    prev_time = current_time

    results = model(frame, stream=True)
    person_count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if model.names[cls] == 'person':
                x1,y1,x2,y2 = map(int,box.xyxy[0])
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(frame, 'Person', (x1,y1-10), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                person_count += 1
    
    cv2.putText(frame, f"People: {person_count}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(123,210,75),2)
    cv2.putText(frame, f"FPS: {int(fps)}",(20,70),cv2.FONT_HERSHEY_SIMPLEX,1,(123,210,75),2)
    cv2.imshow("Insan Tespiti",cv2.resize(frame,(640,480)))
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()