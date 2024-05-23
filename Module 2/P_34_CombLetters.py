'''Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary'''

import itertools

#create multi value dictionary 
dict = {10:['A','B'],11:['C','D']}

#create combination of letters using product method of itertools
for comb in itertools.product(*[dict[k] for k in sorted(dict.keys())]):
    #print the combination using join() function
    print(''.join(comb))

    