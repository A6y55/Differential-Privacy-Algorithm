from bloom_filter import *
import random
import math

def random_permanent(f):
    a = random.randint(0, 9999)
    F = int(f * 10000)
    if a < F // 2:
        return 1
    if a > F:
        return -1
    return 0

def random_instant(p, q, a):
    s = random.randint(0, 9999)
    if a == 1:
        return 1 if s < q * 10000 else 0
    if a == 0:
        return 1 if s < p * 10000 else 0

# def rappor(f, p, q, num, c, arr_all):
#     A = [0] * 18
    
#     in_4_hash1(A, num)
    

#     for k in range(18):
#         s = random_permanent(f)
#         if s == 0:
#             A[k] = 0
#         if s == 1:
#             A[k] = 1

#     s = [0] * 18
#     for k in range(18):
#         if A[k] == 0:
#             s[k] = random_instant(p, q, A[k])
#             A[k] = s[k]

#     for k in range(18):
#         if A[k] == 1:
#             c[k] += 1

#     arr_all[num] += 1

def rappor(fraction, p_value, q_value, item_num, interest_counts, total_interest_counts):
    A = [0] * 18
    
    in_4_hash1(A, item_num)
    
    for k in range(18):
        random_perm = random_permanent(fraction)
        A[k] = random_perm
        
    for k in range(18):
        if A[k] == 0:
            random_inst = random_instant(p_value, q_value, A[k])
            A[k] = random_inst
    
    for k in range(18):
        if A[k] == 1:
            interest_counts[k] += 1
    
    total_interest_counts[item_num] += 1

def calculate_epsilon(f):
    return -math.log(1/f - 1)