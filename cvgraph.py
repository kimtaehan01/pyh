import numpy as np
import cv2

img = np.ones((600, 600, 3), dtype=np.uint8) * 255
h,w,c=img.shape
x=np.arange(w)
def img_init():
    img.fill(255)
    cv2.putText(img, "1. y = 2x + 5", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(img, "2. y = 200 * sin(x * pi/180 * 10)", (100, 150), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(img, "3. a=200, b = 100, eclipse", (100, 200), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(img, "back : esc", (100, 250), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 2)

def graph_func(x,y):
    y = img.shape[0] - y
    for i in range(1, len(x)):
        cv2.line(img, (x[i - 1], int(y[i - 1])), (x[i], int(y[i])), (0, 0, 255), 2)
    
    for i in range(0, w, w//10):
        cv2.line(img, (i, h), (i, h-10), (0, 0, 0), 2)
        cv2.putText(img, str(i), (i - 10, h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    # Draw ticks and labels on the y-axis
    for i in range(0, h, h//10):
        cv2.line(img, (5, i), (-5, i), (0, 0, 0), 2)
        cv2.putText(img, str(img.shape[0] - i), (10, i + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(img, "back : esc", (w-120, 100), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0), 1)

def function1(x):
    img.fill(255)
    y=2*x+5
    graph_func(x,y)
    cv2.imshow("y=2*x+5",img)
    select=cv2.waitKey(0)
    if select==27:
        cv2.destroyAllWindows()
        return 0
def function2(x):
    img.fill(255)
    y=200*np.sin(x*np.pi/180*10)
    graph_func(x,y)
    cv2.imshow("y=2*x+5",img)
    select=cv2.waitKey(0)
    if select==27:
        cv2.destroyAllWindows()
        return 0
def draw_eclipse():
    img.fill(255)
    cv2.ellipse(img, (w//2, h//2), (200, 100), 0, 0, 360, (0,0,255), 5)
    cv2.imshow("y=2*x+5",img)
    select=cv2.waitKey(0)
    if select==27:
        cv2.destroyAllWindows()
        return 0

while 1:
    img_init()
    cv2.imshow("select",img)
    select=cv2.waitKey(10000)
    if select==49:
        function1(x)
    elif select==50:
        function2(x)
    elif select==51:
        draw_eclipse()
    elif select==-1:
        cv2.destroyAllWindows()
        break
    elif select==27:
        cv2.destroyAllWindows()
        break
            