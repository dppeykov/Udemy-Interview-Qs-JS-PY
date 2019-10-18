#  --- Directions
#  Check to see if two provided strings are anagrams of eachother.
#  One string is an anagram of another if it uses the same characters
#  in the same quantity. Only consider characters, not spaces
#  or punctuation.  Consider capital letters to be the same as lower case
#  --- Examples
#    anagrams('rail safety', 'fairy tales') --> True
#    anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#    anagrams('Hi there', 'Bye there') --> False

import re
from collections import Counter

s1 = 'rail safety'
s2 = 'fairy tales'

# removes the spaces and the punctuation + returns the string in lowercase
def clean(s):
    # [^\w] - mathes any char that is not (^) a word (\w)
    return re.sub(r'[^\w]','',s).lower()


# print(clean('fairy tales'))

# create a dictionary map
def create_map(s):
    return dict(Counter(clean(s)))

# print(create_map('fairy tales'))

# Important: if 1 clean string is longer than the other, they are not anagrams
def checking_if_anagrams(map1, map2):
    if len(s1_clean) > len(s2_clean) or len(s1_clean) < len(s2_clean):
        return False
    elif map1 == map2:
        return True
            

s1_clean = clean(s1)
s2_clean = clean(s2)

s1_map = create_map(s1)
s2_map = create_map(s2)

print(checking_if_anagrams(s1_map, s2_map))



    
