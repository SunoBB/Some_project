''': Chuyển màu camera sang màu xám'''

import cv2


camrea_ID = 0
vid = cv2.VideoCapture(camrea_ID)

while True:
    ret, frame = vid.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

'''
import cv2
import imutils
camrea_ID = "/home/suno/Back_Lap/Video_re/2022-07-19 11-15-21.mp4"
vid = cv2.VideoCapture(camrea_ID)
rotate = 0

while True:
    ret, frame = vid.read()
    if ret:
        if rotate != 0:
            frame = imutils.rotate(frame, rotate)
        cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('a'):
        rotate += 90
    
    if key == ord('d'):
        rotate -= 90
'''