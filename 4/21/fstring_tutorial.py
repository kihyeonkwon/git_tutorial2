from datetime import datetime
now = datetime.now()

data= datetime(2023,2,2)
today= data.strftime("%Y년 %m월 %d일")

my_name = input()

print(f"{my_name}님 안녕하세요! 오늘은 {now.year}년 {now.month}월 {now.day}일 입니다")

