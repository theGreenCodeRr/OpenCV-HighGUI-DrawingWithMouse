Conventional image processing often uses standard images to demonstrate algorithms or to compare the
performance of algorithms. Among standard images, the standard image database SIDBA (Standard Image Data-
BAse) is often used.

Input & Output (Images & Movies)
The “imread” command can be used to read an image. The raw data (RGB) of the image can be displayed using
the print command. cv2.waitKey() accepts keystrokes for the number of milliseconds given as the argument. For example,
cv2.waitKey(3) waits for 3 milliseconds before executing the next line.

OpenCV also allows the window size to be changed.

One of OpenCV's HighGUI features is the trackbar. Using the trackbar, you can interactively change parameters
passed to image processing functions

A callback function is a function that is called when the trackbar position moves, and the trackbar position is
passed as an argument.
Following the trackbar, there is a HighGUI function, mouse events, which detects and calls back events such as
mouse clicks and changes in location.

Shapes can also be drawn using the mouse. It is also possible to draw a shape by specifying a different color for the right-click callback.
You can also draw shapes while dragging the mouse. 

The Undo function in the mouse drawing program
