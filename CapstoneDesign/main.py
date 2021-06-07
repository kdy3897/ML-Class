import MakeFolder as MF
from Capture import capture
import cv2
from Match import match, size

f = open("test.txt", "r")
contents = f.read()
videoname = contents

MF.mkfolder(videoname)
capture(videoname)

if round(16/9,2) > size(videoname) >= 1.00 :
    match(videoname)

else :
    img = cv2.imread('C:/Users/pc/PycharmProjects/CapstoneDesign/XX.png')
    cv2.imshow('Message', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 해당없음 이미출력
#   비율 X, 워터마크 X


