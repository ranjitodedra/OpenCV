import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("tajmahal.jpg", 1)
filter=cv2.filter2D(img,16,2,17)
cv2.imshow("filter",filter)
cv2.imwrite('filter.jpeg',filter)
cv2.waitKey(0)
cv2.destroyAllWindows()
