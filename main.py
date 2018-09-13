import cv2
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="Provide template ")
ap.add_argument("-n", "--names", required=True,
	help="Provide names in a txt file seperated by ', ' ")
args = vars(ap.parse_args())

file = open(args["names"], 'r')
lines = file.readlines()

list_word = []
for l in lines:
    list_word.append(l.split(", "))

im = cv2.imread(args["image"])

(x, y, a, b) = cv2.selectROI(im)

for item in list_word:
    for i in item:
        im2 = cv2.imread(args["image"])
        cv2.putText(im2, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)  
        cv2.imwrite(os.path.join('Generated' , '%s.jpg'%str(i)), im2)

cv2.waitKey(0)
cv2.destroyAllWindows()