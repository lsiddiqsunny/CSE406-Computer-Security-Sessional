def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def frombits(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def Initial_Transpose(current_bits):
    PI = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    result = []
    for i in range(0, 64):
        result.append(current_bits[PI[i] - 1])
    return result


def to56bits(key_in_64bits):
    CP_1 = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]
    result = []
    for i in range(0, 56):
        result.append(key_in_64bits[CP_1[i] - 1])
    return result

def keyto48bits(key_in_56bits) :
    CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]
    result = []
    for i in range(0, 48):
        result.append(key_in_56bits[CP_2[i] - 1])
    return result

def getfirsthalf(key_in_56bits, n):
    result = []
    temp = []
    for i in range(0,n):
        temp.append(key_in_56bits[i])
    for i in range(0,28):
        result.append(key_in_56bits[i])
    for i in range(0,28-n):
        result[i] = result[i+n]
    for i in range(0,n):
        result[28-n+i] = temp[i]

    return result


def getsecondhalf(key_in_56bits, n):
    result = []
    temp = []
    for i in range(0, n):
        temp.append(key_in_56bits[i+28])
    for i in range(0, 28):
        result.append(key_in_56bits[i+28])
    for i in range(0, 28 - n):
        result[i] = result[i + n]
    for i in range(0, n):
        result[28 - n + i] = temp[i]

    return result


def getfirsthalftext(plaintext):
    result = []
    for i in range(0,32):
        result.append(plaintext[i])
    return result


def getsecondhalftext(plaintext):
    result = []
    for i in range(0,32):
        result.append(plaintext[i+32])
    return result


def expandbits(right_from_text) :
    E = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]
    result = []
    for i in range(0, 48):
        result.append(right_from_text[E[i] - 1])
    return result

def samplebit(Xored_bit):
    PI_2 = [35, 38, 46, 6, 43, 40, 14, 45,
            33, 19, 26, 15, 23, 8, 22, 10,
            12, 11, 5, 25, 27, 21, 16, 31,
            28, 32, 34, 24, 9, 37, 2, 1]
    result = []
    for i in range(0, 32):
        result.append(Xored_bit[PI_2[i] - 1])
    return result

def PBox(current_bits):
    P = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]
    result = []
    for i in range(0, 32):
        result.append(current_bits[P[i] - 1])
    return result

def Final_Transpose(current_bits):
    PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]
    result = []
    for i in range(0, 64):
        result.append(current_bits[PI_1[i] - 1])
    return result