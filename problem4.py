def is_palindromic(value):
    val_as_string = str(value) 
    val_reversed = str(value)[::-1]
    if val_reversed == val_as_string:
        return True
    return False


def problem_four():
    output = 0
    i = 100
    while i < 1000:
        j = 100
        while j < 1000:
            test = i*j
            if is_palindromic(test) and test > output:
                output = test
            j += 1
        i += 1
    return output


def test_is_palindromic():
    try:
        if not is_palindromic(90009):
            raise "Error"
        if not is_palindromic(99):
            raise "Error"
        if not is_palindromic(9):
            raise "Error"
        if is_palindromic(1234):
            raise "Error"
        print "Is Palindromic Tests Passed"    
    except:
        print "Is Palindromic Tests Failed"


test_is_palindromic()
print problem_four()