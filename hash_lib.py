def hash1(num):
        hash_value = 0
        if num == 0:
            return 0
        while True:
            if num > 0:
                k = num % 10
                hash_value = hash_value * 1311 + k
                num = num // 10
            else:
                return hash_value


def hash2(num):
        hash_value = 0
        if num == 0:
            return 0
        while True:
            if num > 0:
                k = num % 10
                hash_value = hash_value * 3677 + k
                num = num // 10
            else:
                return hash_value

def hash3(num):
        hash_value = 0
        if num == 0:
            return 0
        while True:
            if num > 0:
                k = num % 10
                hash_value = hash_value * 4423 + k
                num = num // 10
            else:
                return hash_value

def hash4(num):
        hash_value = 0
        if num == 0:
            return 0
        while True:
            if num > 0:
                k = num % 10
                hash_value = hash_value * 4871 + k
                num = num // 10
            else:
                return hash_value


def hash11(num):
        temp = [0] * 4
        num = num * num
        if num < 26:
            return num + 2
        for i in range(4):
            k = num % 10
            temp[i] = k
            num = num // 23
        return temp[2] * 10 + temp[1]

def hash12(num):
        temp = [0] * 4
        num = num * num
        if num < 26:
            return num + 1
        for i in range(4):
            k = num % 10
            temp[i] = k
            num = num // 11
        return temp[2] * 10 + temp[1]

def hash13(num):
        temp = [0] * 4
        num = num * num
        if num < 26:
            return num + 5
        for i in range(4):
            k = num % 10
            temp[i] = k
            num = num // 13
        return temp[2] * 10 + temp[1]

def hash14(num):
        temp = [0] * 4
        num = num * num
        if num < 26:
            return num + 9
        for i in range(4):
            k = num % 10
            temp[i] = k
            num = num // 17
        return temp[2] * 10 + temp[1]
