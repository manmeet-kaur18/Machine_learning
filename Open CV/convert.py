import cv2
import sys
import os

#Exception Handling
#Arguments check
if len(sys.argv) != 2:
	raise Exception('Invariant Number of Arguments passed')

#File type check
t = str(sys.argv[1]).split(".")
if t[1] not in ["mp4","wav"]:
	raise Exception('Raise Exception incompatible file type only mp4 or wav required')

# Video existence check
if not os.path.exists(sys.argv[1]):
	raise Exception('the video file does not exists or the path is incorrect')


# getting video file and processing it and saving as filename_output.mp4
cap = cv2.VideoCapture(str(sys.argv[1]))
width  = cap.get(3) 
height = cap.get(4) 
# fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out_video = cv2.VideoWriter(t[0]+'_output.mp4', 0x7634706d, 20.0, (int(width), int(height)), False)
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