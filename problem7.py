from common import get_next_prime

def problem_seven(val):
    counter = 0
    current_prime = 0
    prime_generator = get_next_prime()
    while counter < val:
        counter += 1
        current_prime = prime_generator.next()
    return current_prime

    
def tests():
    if problem_seven(6) == 13:
        print "Tests Passed"
    else:
        print "Tests Failed"

tests()
print problem_seven(10001)