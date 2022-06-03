import numpy as np

# 원소값 0 행렬 - 2행 5열, 32비트 정수형
zero = np.zeros((2, 5), int)
print(zero)
# 원소값 1 행렬 - 3행 1열, 부호 없는 8비트 정수형
one = np.ones((3, 1), np.uint8)
print(one)
# 원소값 쓰레기값 행렬 - 1행 5열
empty = np.empty((1, 5), float)
# 원소값 입력된 값 행렬 - 2행 5열 32비트 실수형
full = np.full((2, 5), 15, np.float32)

# Reshape
reshape1 = np.reshape(zero, (5, 2))
print(reshape1)
reshape2 = one.reshape(1, 3)
print(reshape2)

# Random Value Generate
np.random.seed(10)  # Random seed generate
rand1 = np.random.rand(2, 3)  # 균일분포 난수 행렬 - 2행 3열
rand2 = np.random.randn(3, 2)  # 평균 0, 표준편차 1의 정규분포 난수 행렬 - 3행 2열
rand3 = np.random.rand(6)  # 균일분포 난수 행렬 - 1행 6열
rand4 = np.random.randint(1, 100, 6)  # [1,100] 사이 정수 난수 행렬 - 1행 6열
# 0~9값들이 나열된 행렬을 2행 5열짜리 행렬로 변환
print(np.arange(10).reshape(2, 5))

# Multi demension to One demension
print(full)
print(full.flatten())
print(reshape1)
print(np.ravel(reshape1))
print(one)
print(np.reshape(one, (-1,)))
print(full)
print(full.reshape(-1, ))

