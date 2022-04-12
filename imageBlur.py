import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("nature.jpg", 1)
blur=cv2.blur(img,(5,5))
cv2.imshow("blur",blur)
cv2.imwrite('blur.jpeg',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
