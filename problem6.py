def sum_squares(val):
    total = 0
    for i in range(1, val+1):
        total += i*i
    return total


def square_sum(val):
    inter = sum(range(1, val+1))
    return inter*inter


def problem_six(val):
    sum_squ = sum_squares(val)
    squ_sum = square_sum(val)
    return squ_sum - sum_squ


def test():
    if problem_six(10) != 2640:
        print "Tests failed"
    else:
        print "Tests Passed"

test()
print problem_six(100)