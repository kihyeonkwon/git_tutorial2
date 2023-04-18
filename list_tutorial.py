my_list = ['a', 'b', 'c', 'd', 'e', 'f']


print(my_list[5])

# 인덱싱
# print(id(my_list[0]))
# print(id(my_list[1]))
# print(id(my_list[2]))

# 슬라이싱 (인덱싱과 비슷하다)
# new_list = my_list[0:-1:1]
# new_list = my_list[::-1]
new_list = my_list[::-1]
print(new_list)



# - a, b, c, d, e가 있게
# - c, d, e, f가 있게
# - d, c, b가 있게
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(my_list[:-1])
print(my_list[2:6])
print(my_list[3:0:-1])
print(my_list[::2])



import time

my_list = ['a', 'b', 'c', 'd', 'e', 'f']

for i in my_list:
    print(i)
    time.sleep(1)


