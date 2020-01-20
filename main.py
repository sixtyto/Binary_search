def binary_search(list, item):
    start = 0
    end = len(list)-1

    while start <= end:
        middle = (start + end)//2
        guess = list[middle]
        if guess == item:
            return middle
        if guess > item:
            end = middle - 1
        else:
            start = middle + 1
    return None

my_range = range(1,10**5,2)
my_list = [2,4,6,8,10,12]

print(binary_search(my_range,33339))
print(binary_search(my_range,21542))
print(binary_search(my_list,8))
print(binary_search(my_list,13))
