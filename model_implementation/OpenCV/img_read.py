import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    # works for images,videos, and live videos
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


def changeRes(width,height):
    # only works for live video
    cap.set(3,width)
    cap.set(4,height)

img = cv.imread("Resources/Photos/cat_large.jpg")

cv.imshow("Cat",img)

cap = cv.VideoCapture("Resources/Videos/dog.mp4")


    




while True:
    isTrue,frame = cap.read()
    frame_resized = rescaleFrame(frame)
    
    cv.imshow("Video",frame)
    cv.imshow("Video re",frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord("d"): # if d key is entered than video will stop
        break


cap.release()


cv.destroyAllWindows()
