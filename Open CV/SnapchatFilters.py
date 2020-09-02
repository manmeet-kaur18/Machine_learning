import cv2
import sys
cap = cv2.VideoCapture(str(sys.argv[1]))
width  = cap.get(3) 
height = cap.get(4) 
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out_video = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(width), int(height)), False)
while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            cv2.imshow('frame', gray)
            out_video.write(gray) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()