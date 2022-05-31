HEX_DIGITS = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
N = 2 # number of bytes in hex value

def HEX_2_little_endian(val): 
    result = 0
    pow16 = 1
    for index in range(2, len(val), N):
        result += int("0x" + val[index + 1], 0) * pow16
        pow16 *= 16
        result += int("0x" + val[index], 0) * pow16
        pow16 *= 16
    return result


def HEX_2_big_endian(val):
    result = 0
    pow16 = 1
    for index in range(len(val) - 1, 1, -1):
        result += int("0x" + val[index], 0) * pow16
        pow16 *= 16
    return result


def little_endian_2_HEX(val, size):
    result = ''
    buffer = ''
    while val != 0:
        buffer = HEX_DIGITS[val % 16] + buffer
        if (len(buffer) == N):
            result += buffer
            buffer = ''
        val //= 16
    result = '0x' + result + '0' * (size * 2 - len(result))
    return result


def big_endian_2_HEX(val, size):
    result = ''
    while val != 0:
        result = HEX_DIGITS[val % 16] + result
        val //= 16
    result = '0x' + result + '0' * (size * 2 - len(result))
    return result
