
append_list = []
def count_substring(string, sub_string):
    for i in range(len(string)):
         if string[i:i+len(sub_string)] == sub_string:
             append_list.append(string[i:i+len(sub_string)])
     return append_list



## learnt from solutions in hacker rank
def count_substring(string,substr):
    cou=0
    # return string.count(sub_string) built in function to find the count but doesnt count overlapping substrings
    for i in range(0,len(string)):
        cou = cou + string.count(substr,i,i+len(substr))
    print(cou)

string='ABCDCDC'
substr='CDC'

substr_func=count_substring(string,substr)
print(substr_func)