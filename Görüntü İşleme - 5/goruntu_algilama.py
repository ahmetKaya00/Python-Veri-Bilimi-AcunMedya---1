import cv2
from ultralytics import YOLO

model = YOLO("yolov5s.pt")

cap = cv2.VideoCapture("video.mp4")

cv2.namedWindow('Insan Tespiti',cv2.WINDOW_NORMAL)
cv2.resizeWindow("Insan Tespiti",640,480)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, stream=True)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if model.names[cls] == 'person':
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(frame, 'Person',(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.imshow("Insan Tespiti",cv2.resize(frame,(640,480)))
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()