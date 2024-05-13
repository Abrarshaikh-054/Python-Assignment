'''Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary'''

import itertools

dict = {10:['A','B'],11:['C','D']}

for comb in itertools.product(*[dict[k] for k in sorted(dict.keys())]):

    print(''.join(comb))