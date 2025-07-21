# preprocessing
# from itertools import combinations as C

# def isprime(n):
#     for i in range(3, int(n**.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# Lambda = 16765056000
# L = []
# for i in range(int(1e7)+1, int(1e8), 2):
#     if Lambda % i != 0:
#         if Lambda % (i - 1) == 0:
#             if isprime(i):
#                 L.append(i)
#                 print(i)
# print(L)
# print(len(L))

# note
# This code below is too slow to copy and paste right into baekjoon, please run it in a local environment and copy paste the output.

import random

l = [10478161, 10584001, 10886401, 10914751, 11289601, 12096001, 12192769, 12418561, 13305601, 13970881, 14553001, 14784001, 15240961, 15552001, 18144001, 18627841, 18711001, 19404001, 20697601, 20956321, 21829501, 22809601, 24837121, 27216001, 29568001, 29937601, 31752001, 33264001, 37255681, 39916801, 44352001, 47628001, 47900161, 50803201, 55883521, 56448001, 58212001, 59875201, 72576001, 77616001, 84672001, 88704001, 93139201]
while True:
    p = 1
    P = random.sample(l, 11)
    for i in P: p *= i
    if p % 16765056000 == 1:
        print(*sorted(P))
        break

# or just copy paste this code:
# print("11289601 12418561 18144001 18627841 19404001 29937601 31752001 56448001 58212001 72576001 77616001")