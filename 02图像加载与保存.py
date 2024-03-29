import cv2 as cv
import numpy as np
import path_const


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:
            break

def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(src)
    print(pixel_data)

src = cv.imread(path_const.IMAGE_PATHS[0])
cv.imshow("input image", src)
get_image_info(src)
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite(path_const.IMAGE_PATHS[0], gray)
#video_demo()
cv.waitKey(0)

cv.destroyAllWindows()