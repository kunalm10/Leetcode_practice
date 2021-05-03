




numbers = ['a', 'b', 'c', 'd']

index = 0
for num in numbers:
    print(index , num)
    index += 1

for index, num in enumerate(numbers):
    print(index, num)