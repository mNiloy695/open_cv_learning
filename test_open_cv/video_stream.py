import cv2
from ultralytics import YOLO
def video_stream():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("video not opened")
        return
    
    while True:
        ret,frame=cap.read()
        
        
        if not ret:
            print("frame not found or detected")
            break
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
        
       
        frame=cv2.GaussianBlur(frame,(5,5),0)

        
        model=YOLO("yolo11n.pt")
        results=model(frame)
        result=results[0]
        boxes=result.boxes
        for box in boxes:
            # class_id=int(box.cls[0])
            # name=model.names[class_id]
            # print(name)
            x1,y1,x2,y2=box.xyxy[0]
            width=x2-x1
            height=y2-y1 
            print("width...",float(width))
            print("height..",float(height))
            x1=float(x1)
            y1=float(y1)
            x2=float(x2)
            y2=float(y2)
            print("printing",x1,y1,x2,y2)

        cv2.imshow("webcam", frame)
        
    
    cap.release()
    cv2.destroyAllWindows()
        
video_stream()   