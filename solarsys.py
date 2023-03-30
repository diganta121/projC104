
import cv2

img = cv2.imread("./proj/img.jpg")

planets = {"mercury":(120,180),
           "venus":(195,170),
           "earth":(288,165),
           "mars":(386,170),
           "jupiter":(585,50),
           "saturn":(790,126),
           "uranus":(970,135),
           "neptune":(1110,140)
           }

for name,l in planets.items():
    cv2.putText(img,name,l,fontFace=cv2.FONT_ITALIC,fontScale=0.5,color=(255,255,255))

cv2.imwrite("output.jpg",img)
cv2.imshow("img" ,img)
cv2.waitKey(0)