import numpy as np, cv2

# cv2.add  cv2.subtract  cv2.multiply  cv2.divide

# cv2.exp  cv2.log  cv2.sqrt  cv2.pow

# cv2.magnitude: 2차원 배열의 크기를 계산
# cv2.phase: 2차원 배열의 회전 각도를 계산

# cv2.cartToPolar  cv2.polarToCart: 2차원 배열들의 크기와 각도를 계산

# Bit Operator
image = np.zeros((300, 300), np.uint8)
imageCopy = image.copy()

h, w = image.shape[:2]
cx, cy = w//2, h//2
cv2.circle(image, (cx,cy), 100, 255, -1)
cv2.rectangle(imageCopy, (0,0,cx,h), 255, -1)

imageOR = cv2.bitwise_or(image, imageCopy)
imageAND = cv2.bitwise_and(image, imageCopy)
imageXOR = cv2.bitwise_xor(image, imageCopy)
imageNOT = cv2.bitwise_not(image, imageCopy)

titles = ['image', 'imageCopy', 'imageOR', 'imageAND', 'imageXOR', 'imageNOT']

for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)