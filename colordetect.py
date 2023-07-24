import pandas as pd
import cv2 as cv
import numpy as np
# reading the image
img = cv.imread("colorimage.jpg")
cv.resize(img,(3000,3000))

# giving headings to csv file using pandas module
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# global variables for printing the output
# starting double click is false
clicked = False

# r,g,b values and positions are zero by default until the function starts working
r = g = b = xpos = ypos = 0

# function to identify the color name
def recognize_color(R,G,B):
    minimum = 10000  # assign some minimum value
    for i in range(len(csv)):  # loop repeats until the length of file
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))  # finding the absolute values for colors R,G,B
        if( d <= minimum ):
            minimum = d
            cname = csv.loc[i, "color_name"]  # getting the color name related to the selected click
    return cname

# function for the mouse double click
def mouse_click(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:  # used mouse double click event
        global b,g,r,xpos,ypos, clicked
        clicked = True
        # getting the values of colors and positions
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

# naming the window
cv.namedWindow('Color Recognition App')

# mouse click function calling
cv.setMouseCallback('Color Recognition App', mouse_click)

# infinite loop
while (1):
    cv.imshow("Color Recognition App", img)
    if (clicked):
         cv.rectangle(img, (0, 20), (600, 90), (255, 255, 255), -5)  # creating rectangle for displaying output
         text = recognize_color(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
         cv.putText(img, text, (50, 50), 2, 0.8, (b, g, r), 2, cv.LINE_AA) # displaying our required output
         cv.putText(img, "(e n t e r  ' q '  t o  e x i t )",(175,80),2,0.5,(b,g,r),2,cv.LINE_AA)
         clicked = False
    if cv.waitKey(1) == ord("q"):   # exits when user presses 'q' key
        break
cv.destroyAllWindows()  # after exiting from the loop it destroys all the opened windows