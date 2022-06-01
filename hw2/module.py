HEX_DIGITS = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
N = 2 # number of bytes in the hex value

def digit_hex_2_dec(val): # hex -> dec for one digit
    return int("0x" + val, 0)


def hex_2_little_endian(val): 
    result = 0
    pow16 = 1
    for index in range(2, len(val), N): 
        # we start with the index = 2 because of 0x symbol in the beginning
        # also we suppose that the size of our value is even
        result += digit_hex_2_dec(val[index + 1]) * pow16
        pow16 *= 16
        result += digit_hex_2_dec(val[index]) * pow16
        pow16 *= 16

    return result


def hex_2_big_endian(val):
    result = 0
    pow16 = 1
    for index in range(len(val) - 1, 1, -1):
        result += digit_hex_2_dec(val[index]) * pow16
        pow16 *= 16
    return result


def little_endian_2_hex(val, size):
    result = ''
    buffer = '' # as we have several bytes in one "cell" we will need a way to store them
    while val != 0:
        buffer = HEX_DIGITS[val % 16] + buffer
        if (len(buffer) == N):
            result += buffer
            buffer = ''
        val //= 16
    result = '0x' + result + '0' * (size * 2 - len(result)) # adding missing zeroes and 0x
    return result


def big_endian_2_hex(val, size):
    result = ''
    while val != 0:
        result = HEX_DIGITS[val % 16] + result
        val //= 16
    result = '0x' + '0' * (size * 2 - len(result)) + result # adding missing zeroes and 0x
    return result
