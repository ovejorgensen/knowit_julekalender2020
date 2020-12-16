import math

""" ULTRA FAST way of finding sums of divisors """
def sum_divisors(n):
    result = [1] * n
    result[0] = 0
    for p in range(2, n):
        if result[p] == 1: # p is prime
            p_power, last_m = p, 1
            while p_power < n:
                m = last_m + p_power
                for i in range(p_power, n, p_power):
                    result[i] //= last_m    # (B)
                    result[i] *= m          # (B)
                last_m = m
                p_power *= p
    return result

res = 0
divisors = sum_divisors(1000000)
for n, el in enumerate(divisors):
    diff = abs(el - 2*n)
    if el > 2*n and diff == math.isqrt(diff)**2: 
        res += 1
print(f'Result: {res} numbers')

""" short version that is a bit slower """

# from sympy import divisors
# divisor_sums = [sum(divisors(x)) for x in range(1000000)]
# res = 0
# for n, el in enumerate(divisor_sums):
#     diff = abs(el - 2*n)
#     if el > 2*n and diff == math.isqrt(diff)**2: 
#         res += 1
# print(res)


""" MEGA SLOW VERSION """

# for n in range(1,1000000):
#     sum_divisors = sum([x for x in range(1,n+1) if not n%x])
#     diff = abs(sum_divisors - 2*n)
#     if sum_divisors > diff and diff not in non_quadratic: 
#         result += 1
#     print(n)

