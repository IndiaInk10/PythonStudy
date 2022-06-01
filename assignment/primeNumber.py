import random

sum = 0
for j in range(3):
    rand_max_num = random.randint(0,10)
    print(j+1, "번째 수행. 임의의 정수:", rand_max_num)

    for i in range(1, rand_max_num+1):
        cnt = 0
        for k in range(1, rand_max_num+1):
            if i % k == 0:
                cnt += 1
            if cnt == 2:
                if k == i:
                    print("소수 :", i)
                    sum += i
                    break
            elif cnt > 2:
                break

    print("")

print("sum: ", sum)