# import cv2
# import sys
# import os

# # Exception handling
# #argument check
# if len(sys.argv) != 3:
# 	raise Exception('Invariant Number of Arguments passed.Please pass one video path and one compress percentage')

# #file type check
# t = str(sys.argv[1]).split(".")
# if t[1] not in ["mp4","wav"]:
# 	raise Exception('Raise Exception incompatible file type only mp4 or wav required')

# #range of compression check
# if int(sys.argv[2]) not in range(1,100):
# 	raise Exception('Compress percent should be in range 1-99')

# # file existence check
# if not os.path.exists(sys.argv[1]):
# 	raise Exception('the video file does not exists or the path is incorrect')

# # getting video and then processing it and saving in filename_ouput.mp4
# cap = cv2.VideoCapture(str(sys.argv[1]))
# # width  = (cap.get(3) * int(sys.argv[2]))/ 100
# # height = (cap.get(4) * int(sys.argv[2]))/ 100
# size = (
#         int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)*int(sys.argv[2])/100),
#         int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)*int(sys.argv[2])/100)
#         )

# fourcc = cv2.VideoWriter_fourcc(*"DIVX")
# output = cv2.VideoWriter(t[0]+'_output.mp4',fourcc, 20.0, size)

# while(True):
#     ret, frame = cap.read()
#     if frame is None:
#         break
#     resize = cv2.resize(frame,size)
#     output.write(resize)

# cap.release()
# cv2.destroyAllWindows()

import cv2
import os 
import sys

if not os.path.exists(sys.argv[1]) :
    raise Exception("File does not exist !")

if len(sys.argv) != 3 :
    raise Exception("Wrong Number of arguments passed !")

resize_factor = int(sys.argv[2])

capture = cv2.VideoCapture(sys.argv[1])
length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

size = (
  int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)*resize_factor/100 ),
  int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)*resize_factor/100 )
)

codec = cv2.VideoWriter_fourcc(*'DIVX')
output = cv2.VideoWriter(sys.argv[1].split('.')[0] + '_output' + '.mp4', codec, 16.0, size)

while(True):
   ret, frame = capture.read()
   if frame is None:
     break
   
   resize = cv2.resize(frame,size)
   output.write(resize)

capture.release()
cv2.destroyAllWindows()