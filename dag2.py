is_prime = lambda num: False if len([x for x in range(2, num) if num % x == 0]) > 0 else True

def find_prime(num):
    found = False
    while(not found): 
        if(is_prime(num)): 
            found = True
        else:
            num -=  1
    return num

gifts = i = 0
while(i < 5433000):
    if "7" in str(i):
        i += find_prime(i)
    else:
        gifts += 1
    i += 1

print(f"gifts: {gifts}")