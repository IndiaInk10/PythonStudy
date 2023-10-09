import numpy as np, cv2

path = 'src/everytime/2.jpg'

image = cv2.imread(path)
image_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

b, g, r = cv2.split(image)

ret, dst  = cv2.threshold(image_gray, 250, 255, cv2.THRESH_BINARY)

mask = np.array([[0,1,0],
                 [1,1,1],
                 [0,1,0]]).astype('uint8')

dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, mask)
contour, hierarchy = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contour:
    cv2.drawContours(image, [cnt], 0, (0,255,0), 3)

cv2.imshow('process', dst)
cv2.imshow('origin', image)
cv2.waitKey(0)

