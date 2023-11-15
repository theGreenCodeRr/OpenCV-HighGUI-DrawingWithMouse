#Implement the Undo function in the mouse drawing program
import cv2
import numpy as np

drawing = False
ix,iy = -1,-1
stack = []

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,stack,img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        stack.append(img.copy())
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

img = np.zeros((600,600,3))
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_rectangle)

while True:
    cv2.imshow('my_drawing',img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord('u') or key == cv2.EVENT_RBUTTONDOWN:
        if len(stack) > 0:
            img = stack.pop()
            cv2.imshow('my_drawing', img)

cv2.destroyAllWindows()
