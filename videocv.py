import numpy as np
import cv2 as cv
circle_positions = []

def draw_circles_on_frame(frame):
    for pos in circle_positions:
        x, y = pos
        cv.circle(frame, (x, y), 50, (255, 0, 0), -1)

def draw_circle(event,x,y,flags,param):
 if event == cv.EVENT_LBUTTONDBLCLK:
    circle_positions.append((x, y))

img = cv.imread(cv.samples.findFile("C:/Users/EGT/Downloads/figma.png"))
cap = cv.VideoCapture(0)
if not cap.isOpened():
 print("Cannot open camera")
 exit()
while True:
 # Capture frame-by-frame
 ret, frame = cap.read()
 # if frame is read correctly ret is True
 if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break
 # Our operations on the frame come here
 draw_circles_on_frame(frame)
 # Display the resulting frame
 cv.imshow('frame', frame)
 cv.imshow('frame2', img)
 cv.setMouseCallback('frame',draw_circle)
 print(circle_positions)
 if cv.waitKey(1) == ord('q'):
    break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()