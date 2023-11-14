import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN: # Right click event
        cv2.circle(img,(x,y),100,(0,0,255),-1)

img = np.zeros((600,600,3), np.uint8)

cv2.namedWindow(winname='mouse_drawing')
cv2.setMouseCallback('mouse_drawing',draw_circle)

while True:
    cv2.imshow('mouse_drawing',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()