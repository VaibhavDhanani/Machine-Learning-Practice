import cv2 as cv
import numpy as np 

blank = np.zeros((600,600,3),dtype="uint8")
# cv.imshow("Blank",blank)

# img = cv.imread("Resources/Photos/cat.jpg")
# cv.imshow("Cat",img)

# 1. Paint img with color
# blank[200:300,300:400] = 100,99,200
# cv.imshow("Blank",blank)

# 2. draw rectangle
cv.rectangle(blank,(100,100),(256,412),(100,175,10),thickness=-1)
cv.imshow("Blank",blank)

# 3. draw circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),70,(100,100,120),thickness=cv.FILLED)
cv.imshow("Circle",blank)

# 4. draw line 
cv.line(blank,(20,100),(321,432),(44,44,44),thickness=5)
cv.imshow("line", blank)

# 5. write text in img 
cv.putText(blank,"Dhanani Vaibhav ",(200,300),cv.FONT_HERSHEY_DUPLEX,1.0,(0,222,2),thickness=2)
cv.imshow("Name", blank)

cv.waitKey(0) 
cv.destroyAllWindows()