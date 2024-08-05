def rev_st(inp):
    fun_split = inp.split(' ')  # to generate list out of the string

    rev_str = fun_split[::-1]  # reversing the list
    return ' '.join(rev_str)   # converting list back to string


str_to_rev = "I love python"
op_rev = rev_st(str_to_rev)
print("reverse string of {} is: {}".format(str_to_rev,op_rev))
