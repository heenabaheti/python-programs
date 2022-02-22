def my_func(n):
    if n >= 0:
        return True
    else:
        return False
my_list = [2, -3, 4, -5, 6, -7, 8, 9]
result = filter(my_func, my_list)
for i in result:
    print(i)

