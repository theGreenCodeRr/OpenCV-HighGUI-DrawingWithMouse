import cv2
import sys

# Functions for callbacks Using the trackbar
def printing(position):
    print(position)

# Loading Video
cap = cv2.VideoCapture("video/Parrots.mp4")

# Create a window to display the trackbar
cv2.namedWindow("window")    # Trackbar name, window name, initial value, maximum value of trackbar, callback function 
threshold = 150
cv2.createTrackbar("track", "window", threshold, 255, printing)

if cap.isOpened() == False: # Check if it is loaded.
    sys.exit()

# Entering the video loading loop 
while True: # Load only one frame
    ret, frame = cap.read()
    img_gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        # Break when the last read of the video is False. 
    if ret == False:
        break

    # Thresholding : cv2.THRESH_BINARY
    ret, th = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY) 
    threshold = cv2.getTrackbarPos("track", "window")

    # Display the loaded frame 
    cv2.imshow("window", th) 
    if cv2.waitKey(30) == 27:
        break 
cv2.destroyAllWindows()