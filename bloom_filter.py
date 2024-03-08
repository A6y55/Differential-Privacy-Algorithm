from hash_lib import *

def test(arr,num):
    if arr[hash1(num) % 18] != 1:
        return False
    if arr[hash2(num) % 18] != 1:
        return False
    if arr[hash3(num) % 18] != 1:
        return False
    if arr[hash4(num) % 18] != 1:
        return False
    return True

def answer():
    result = []
    for i in range(100):
        if test(i):
            result.append(i)
    return result

def in_4_hash1(arr, num):
        arr[hash11(num) % 18] = 1
        arr[hash12(num) % 18] = 1
        arr[hash13(num) % 18] = 1
        arr[hash14(num) % 18] = 1

def test_ture(arr, num):
    if arr[hash11(num) % 18] != 1:
        return False
    if arr[hash12(num) % 18] != 1:
        return False
    if arr[hash13(num) % 18] != 1:
        return False
    if arr[hash14(num) % 18] != 1:
        return False
    return True

def test_min(arr, num):
    if arr[hash11(num) % 18] <= 0:
        return 0
    min_val = arr[hash11(num) % 18]

    if arr[hash12(num) % 18] <= 0:
        return 0
    min_val = min(min_val, arr[hash12(num) % 18])

    if arr[hash13(num) % 18] <= 0:
        return 0
    min_val = min(min_val, arr[hash13(num) % 18])

    if arr[hash14(num) % 18] <= 0:
        return 0
    min_val = min(min_val, arr[hash14(num) % 18])

    return min_val