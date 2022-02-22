
def result(n):
    return n + n

my_list = [2, 3, 4, 5, 6, 7, 8, 9]
updated_list = map(result, my_list)
print(list(updated_list))

