import random
from math import sqrt

def xgcd(a, b):
    xprev, x = 0, 1
    yprev, y = 1, 0

    while a:
        q = b // a
        x, xprev = xprev - q * x, x
        y, yprev = yprev - q * y, y
        a, b = b % a, a

    return b, xprev, yprev

def generate_large_prime(bit_size):
    p = random.getrandbits(bit_size)
    if not p & 1:  # make sure it's odd
        p += 1
    while not miller_rabin(p):  # test for primality
        p = p + 2
    return p

def miller_rabin(n, k=10):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False

    s, d = 0, n - 1
    while not d % 2:
        s += 1
        d //= 2
    assert(2**s*d == n - 1)

    def check_if_composite_using(a):
        x = exp(a, d, n)
        if x == 1 or x == n - 1:
            return False  # probably prime
        for _ in range(s):
            x = (x * x) % n  # check for each a^((2^i)*d)
            if x == n - 1:
                return False  # probably prime
        return True  # definitely composite
    for _ in range(k):
        a = random.randint(2, n-1)
        if check_if_composite_using(a):
            return False  # definitely composite
    return True  # probably prime


def exp(x, n, p=1000007):
    ans = 1
    x = x % p
    while n > 0:
        if n & 1:
            ans = (ans * x) % p
        x = (x * x) % p
        n = n >> 1

    return ans

def as_bytes(string):
    try:
        return bytes(string)
    except:
        return bytes(string, "utf-8")

def gcd(a, b):
    while a:
        a, b = b % a, a
    return b

def inverse(a, n):
    g, x, _ = xgcd(a, n)
    return (x % n + n) % n
