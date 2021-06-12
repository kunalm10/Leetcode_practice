def binaryRepresentationFunction(num):
    number = num
    number_of_bits_required = 0
    binary_representation_string = ''
    number_of_ones_in_bit_representaion_string = 0
    if num == 0:
        binary_representation_string = '0'
        print(binary_representation_string)
        return binary_representation_string
    while num >= 1:
        num //= 2
        number_of_bits_required += 1
        # print(num)
    print(number_of_bits_required)

    for i in range(number_of_bits_required, 0, -1):
        print(2**(i-1))
        if number >= 2 ** (i-1):
            number -= 2 ** (i-1)
            binary_representation_string = binary_representation_string + '1'
            number_of_ones_in_bit_representaion_string += 1
        else:
            binary_representation_string = binary_representation_string + '0'
    print('number_of_ones_in_bit_representaion_string = ', number_of_ones_in_bit_representaion_string)
    print(binary_representation_string)
    return binary_representation_string

binaryRepresentationFunction(10)