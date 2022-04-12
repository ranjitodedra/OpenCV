import cv2

img = cv2.imread('asset/perfil.png',1) #
img = cv2.resize(img, (400,400)) 
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE) # for rotation 


cv2.imwrite('new_img.jpeg',img) #create new img file
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
