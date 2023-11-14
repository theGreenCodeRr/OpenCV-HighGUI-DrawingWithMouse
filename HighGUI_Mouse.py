import cv2
# HighGUI function with Mouse events
#Callback function for mouse event 
def print_position(event,x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
img = cv2.imread("img/Pepper.bmp")
cv2.namedWindow('image')

#Mouse Event Settings
cv2.setMouseCallback('image', print_position)
cv2.imshow("image", img)
cv2.waitKey(30000) == 27
cv2.destroyAllWindows()