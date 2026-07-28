import cv2

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
        
        cv2.imshow("webcame",frame)
    
    cap.release()
    cap.destroyAllWindowes()
        
video_stream()   