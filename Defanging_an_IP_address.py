# 1108


def defanging_an_address(address):
    return_string = str()
    for char in address:
        if char == ".":
            return_string += "[.]"
        else:
            return_string += char
    return return_string


if __name__ == '__main__':
    address = "1.1.1.1"
    print(defanging_an_address(address))
