import cv2

image = cv2.imread("../src/metaverse.jpg", cv2.IMREAD_COLOR)
image = cv2.resize(image, (500, 300), cv2.INTER_LINEAR)
imageGray = cv2.imread("../src/metaverse.jpg", cv2.IMREAD_GRAYSCALE)
imageGray = cv2.resize(imageGray, (500, 300), cv2.INTER_LINEAR)

title, titleGray = "image", "imageGray"

print(title + ":" + str(image.ndim))
print(titleGray + ":" + str(imageGray.ndim))

cv2.imshow(title, image)
cv2.imshow(titleGray, imageGray)
cv2.waitKey(0)