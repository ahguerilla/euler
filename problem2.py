def problem_two(value):
    if type(value) != int:
        raise ValueError
    output = 0
    previous_val = 1
    current_val = 2
    while current_val <= value:
        if current_val % 2 == 0:
            output += current_val        
        new_val = current_val + previous_val        
        previous_val = current_val
        current_val = new_val
    return output


def test():
    try:
        if problem_two(-5) != 0:
            raise "Error"
        if problem_two(20) != 10:
            raise "Error"
        try:
            problem_two("hello")
        except ValueError:
            pass
        print "Tests Passed"
    except:
        print "Tests Failed"


test()
print problem_two(4000000)