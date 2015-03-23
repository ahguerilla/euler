def problem_one(value):
    output = 0
    for i in range(value):
        if (i % 3 == 0) or (i % 5 == 0):
            output += i
    return output


def test():
    if problem_one(10) != 23:
        print "Tests Failed"
    else:
        print "Tests Passed"



test()
print problem_one(1000)