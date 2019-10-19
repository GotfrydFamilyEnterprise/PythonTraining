# Greatest Common Factor - the largest number that x and y are divisible by
# ommit one from primes as it is goin to mess with our #MATH
primes = [2,3,5,7,11,13,17,19]
# x = 96 # /(2) => 48/(2) => 24/2 => 12/2 => 6/2 =>(3)
# y = 84 # /(2) => 42/(2) => 21/(3) => 7

x = 3*3*5*5*7*7*13*17
y = 2*2*3*5*5*7*19
divisors = []
_x = x
_y = y
for prime in primes:
    while _x%prime == 0 and _y%prime == 0:
        print (f"found common factor, {prime}")
        _x = _x/prime
        _y = _y/prime
        divisors.append(prime)
gcf = 1
for divisor in divisors:
    gcf = gcf * divisor
print(f"For {x} and {y}")
print(f"GCF = {gcf}")
# to find factors for each number
# pass one - looking for the first factor
# divide x and y by each number in variable primes until you find the
# smallest divisor with whole result