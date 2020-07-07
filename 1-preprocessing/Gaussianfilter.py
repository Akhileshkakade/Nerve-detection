
import cv2
import numpy as np
from PIL import Image,ImageFilter
from scipy.ndimage.filters import gaussian_filter

DELAY_CAPTION = 1500;
DELAY_BLUR = 500;

img = cv2.imread("/home/akhilesh/train/1_1.tif")


'''for i in xrange(1,30,30):
    
    gaussian_blur = cv2.GaussianBlur(img,(i,i),0)
    string = 'guassian_blur : kernel size - '+str(i)
    cv2.imshow('Blur',gaussian_blur)
    cv2.waitKey(DELAY_BLUR)


cv2.waitKey(DELAY_CAPTION)
'''
#image=Image.fromarray(img)
filtered=gaussian_filter(img,sigma=7)
cv2.imwrite("/home/akhilesh/Nerve code/gaussian1.tif",filtered)


cv2.destroyAllWindows()


