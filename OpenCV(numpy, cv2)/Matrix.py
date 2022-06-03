import numpy as np, cv2

image = cv2.imread("src/metaverse.jpg", cv2.IMREAD_COLOR)
image = cv2.resize(image, (500, 300), cv2.INTER_LINEAR)

x_axis = cv2.flip(image, 0)
y_axis = cv2.flip(image, 1)
xy_axis = cv2.flip(image, -1)
rep_image = cv2.repeat(image, 1, 2)
trans_image = cv2.transpose(image)

titles = ['image', 'x_axis', 'y_axis', 'xy_axis', 'rep_image', 'trans_image']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)