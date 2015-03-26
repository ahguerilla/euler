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


def get_prime_factors(val):
    factors = []
    prime_generator = get_next_prime()
    p = prime_generator.next()
    while p <= val:
        while val % p == 0:
            factors.append(p)
            val = val/p
        p = prime_generator.next()
    return factors


def find_lowest_common_multiple(a, b):
    lcm = 1
    factors_a = get_prime_factors(a)
    factors_b = get_prime_factors(b)
    while len(factors_a) > 0:
        p = factors_a[0]
        count_p_a = factors_a.count(p)
        count_p_b = factors_b.count(p)
        count_p = count_p_a if count_p_a > count_p_b else count_p_b
        lcm = lcm*(p**count_p)
        factors_a = filter(lambda a: a != p, factors_a)
        factors_b = filter(lambda a: a != p, factors_b)   
    for i in factors_b:
        lcm = lcm*i
    return lcm


def find_lowest_common_multiple_list(list_items):
    if len(list_items) < 2:
        raise ValueError
    
    first_item = list_items.pop()
    if len(list_items) == 1:
        return find_lowest_common_multiple(first_item, list_items[0])
    else:
        return find_lowest_common_multiple(first_item, find_lowest_common_multiple_list(list_items))


def common_tests():
    try:
        if find_lowest_common_multiple(2,3) != 6:
            raise "Error"
        if find_lowest_common_multiple(4,10) != 20:
            raise "Error"
        if find_lowest_common_multiple(6,60) != 60:
            raise "Error"            
        if find_lowest_common_multiple_list(range(1,11)) != 2520:
            raise "Error"
        print "Common Tests passed"
    except:
        print "Common Tests failed"

#common_tests()


