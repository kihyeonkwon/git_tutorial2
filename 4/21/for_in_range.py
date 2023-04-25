my_list = [5, 7, 8, 9, 4, 3, 2, 1, 2]

print('len', len(my_list))

for i in range(len(my_list)):
    if i == len(my_list)-1:
        print(my_list[i], end=' ')
    else:
        print(my_list[i], end=' ')
