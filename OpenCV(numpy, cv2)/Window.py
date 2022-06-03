import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 클릭")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 클릭")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 떼기")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 더블클릭")


def onChange(value):
    global image, title

    print("추가 화소값:", value)
    image.fill(value)
    cv2.imshow(title, image)


image = np.zeros((200, 400, 3), np.uint8)
image.fill(105)  # image[:] = 105
imageCopy = image.copy()

title = 'Window'
titleCopy = 'WindowCopy'

start = (50, 50)
end = (100, 100)
blue = (255, 0, 0)  # BGR
lineWidth = 3
# Draw Line
cv2.line(imageCopy, start, end, blue, lineWidth)
start = (75, 75)
# Draw Rectangle
cv2.rectangle(imageCopy, start, end, blue, lineWidth)
start = (0, 175)
# Write Text
cv2.putText(imageCopy, "TRIPLEX", start, cv2.FONT_HERSHEY_TRIPLEX, lineWidth, blue)
start = (110, 100)
# Draw Circle
cv2.circle(imageCopy, center=start, radius=10, color=blue, thickness=lineWidth)
start = (140, 100)
axes = (20, 10)
# Draw Ellipse
cv2.ellipse(imageCopy, center=start, axes=axes, angle=360, startAngle=0, endAngle=360, color=blue, thickness=lineWidth)

cv2.imshow(titleCopy, imageCopy)
cv2.imshow(title, image)
# 마우스 이벤트 콜백 함수 부착
cv2.setMouseCallback(title, onMouse)
# 트랙바 부착 및 트랙바 이벤트 콜백 함수 부착
cv2.createTrackbar('Brightness', title, image[0][0][0], 255, onChange)
# 인자로 0을 줄 경우, 키 이벤트 발생까지 무한 대기
cv2.waitKey(0)