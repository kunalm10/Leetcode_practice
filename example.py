



#
# numbers = ['a', 'b', 'c', 'd']
#
# index = 0
# for num in numbers:
#     print(index , num)
#     index += 1
#
# for index, num in enumerate(numbers):
#     print(index, num)
#
#
def hi(take_num):
    def hi2(a,b):
        print('hi1')
        take_num(a,b)
        print('hi2')
    return hi2

@hi
def take_num(a,b):
    print(a>b)

# take_num = hi(take_num)
a = 1
b = 2
take_num(a,b)