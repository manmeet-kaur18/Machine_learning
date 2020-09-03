import cv2
import sys
import os

if len(sys.argv) != 3:
	raise Exception('Invariant Number of Arguments passed.Please pass one video path and one compress percentage')

t = str(sys.argv[1]).split(".")
if t[1] not in ["mp4","wav"]:
	raise Exception('Raise Exception incompatible file type only mp4 or wav required')

if not os.path.exists(sys.argv[1]):
	raise Exception('the video file does not exists or the path is incorrect')

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_CUBIC)


cap = cv2.VideoCapture(str(sys.argv[1]))
width  = (cap.get(3) * int(sys.argv[2]))/ 100
height = (cap.get(4) * int(sys.argv[2]))/ 100
# fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out_video = cv2.VideoWriter(t[0]+'_output.mp4',0x7634706d, 20.0, (int(width), int(height)),True)
while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frameX = rescale_frame(frame,int(sys.argv[2]))
            out_video.write(frameX) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()