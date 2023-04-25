import random

answer = random.randint(10, 100)
while True:
    user_input = int(input())
    if user_input == answer:
        print("정답입니다")
        break
    else:
        print("틀렸습니다")
print("게임이 끝났습니다.")