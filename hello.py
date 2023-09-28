import time

def timer(f) :
    def wrapper(n):
        start_time = time.time()
        result = f(n)
        stop_time = time.time()
        dt = stop_time - start_time
        print(f'delta t = {dt}')
        return result
    return wrapper

@timer
def prime_factor(n) :
    factor = []
    divisor = 2

    while n>1:
        while n%divisor == 0:
            factor.append(divisor)
            n //= divisor
        divisor+=1
    return  factor


result = prime_factor(2**29 + 1)
print(result)


