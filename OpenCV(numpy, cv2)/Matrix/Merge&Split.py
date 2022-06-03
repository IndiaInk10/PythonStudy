import numpy as np, cv2

B0 = np.zeros((100, 100), np.uint8)
B0.fill(255)
B1 = np.zeros((100, 100), np.uint8)
B2 = np.zeros((100, 100), np.uint8)

blueList = [B0, B1, B2]
mergeChannel = cv2.merge(blueList)
cv2.imshow("Blue", mergeChannel)
splitChannel = np.array(cv2.split(mergeChannel))

for i in range(len(splitChannel)):
    print(f"{i}번 채널\n:", splitChannel[i], sep="")

image = cv2.imread("../src/metaverse.jpg", cv2.IMREAD_COLOR)
image = cv2.resize(image, (500, 300))

image[:,:,1:] = 0
cv2.imshow("Blue Channel", image)
cv2.waitKey(0)