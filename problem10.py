from common import get_next_prime


def problem_ten(val):
    get_prime_generator = get_next_prime()
    p = get_prime_generator.next()
    output = 0
    while p < val:
        output += p
        p = get_prime_generator.next()
    return output

def test():
    if problem_ten(10) == 17:
        print "Tests Passed"
    else:
        print "Tests Failed"
    

test()

# 142913828922 - not found very fast
print problem_ten(2000000)