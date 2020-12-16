
num_list = [0, 1]
num_list_set = {0, 1}
primes = []

def prime_check(n):
    if n==1 or n==0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n%i == 0:
                return False
        return primes.append(n)

for i in range(2, 1800813):
    sub = num_list[i-2] - i
    add = num_list[i-2] + i
    if sub > 0 and (sub not in num_list_set):
        num_list.append(sub)
        num_list_set.add(sub)
    elif sub < 0 or (sub in num_list_set):
        num_list.append(add)
        num_list_set.add(add)
    prime_check(num_list[i])

print(f'Number of primes: {len(primes)}')



