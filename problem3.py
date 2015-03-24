def get_next_prime():
    list_primes = []
    counter = 2
    while True:
        found_divisor = False
        for i in list_primes:
            if counter % i == 0:
                found_divisor = True
                break
        if not found_divisor:
            list_primes.append(counter)
            yield counter
        counter += 1

def problem_three(value):
    primes = get_next_prime()
    p = primes.next()
    while p < value:
        if value % p == 0:
            while value % p == 0:
                value = value/p
        p = primes.next()
    return value


def test():
    if problem_three(13195) != 29:
        print "Test Failed"
    else:
        print "Test Passed"


test()
print problem_three(600851475143)


