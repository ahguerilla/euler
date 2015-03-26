from common import find_lowest_common_multiple_list

def problem_five(val):
    return find_lowest_common_multiple_list(range(1, val+1))


def test():
    if problem_five(10) == 2520:
        print "Tests Passed"
    else:
        print "Tests Failed"


test()
print problem_five(20)