#  --- Directions
#  Check to see if two provided strings are anagrams of eachother.
#  One string is an anagram of another if it uses the same characters
#  in the same quantity. Only consider characters, not spaces
#  or punctuation.  Consider capital letters to be the same as lower case
#  --- Examples
#    anagrams('rail safety', 'fairy tales') --> True
#    anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#    anagrams('Hi there', 'Bye there') --> False

# REPL: https://repl.it/@DamyanPeykov/Anagrams

# Solution 1: my solution - just clean the strings, create dict maps and compare them
import re
from collections import Counter

s1 = 'RAIL! SAFETY!'
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
    # > or < basically means not equal, so see solution 2 for a shorter syntax
    if len(s1_clean) > len(s2_clean) or len(s1_clean) < len(s2_clean):
        return False
    elif map1 == map2:
        return True
            

s1_clean = clean(s1)
s2_clean = clean(s2)

s1_map = create_map(s1)
s2_map = create_map(s2)

print(checking_if_anagrams(s1_map, s2_map))


# Solution 2: course's solution - again cleans, creates maps and compares 

def anagrams(string_a, string_b):
    a_char_map = build_char_map(string_a)
    b_char_map = build_char_map(string_b)

    # to find the length, we can look at the number of keys
    if len(a_char_map.keys()) != len(b_char_map.keys()):
        return False
    # another way to solve the problem is by looping through both maps (dicts)
    else:
        for k,v in a_char_map.items():
            # cheking if the number of letters are different
            if a_char_map[k] != b_char_map[k]:
                return False
        return True

def build_char_map(s):
    char_map = {}

    for char in re.sub(r'[^\w]','',s).lower():
        if char in char_map:
            char_map[char] += 1 
        else: 
            char_map[char] = 1 

    return char_map

print(anagrams(s1, s2))

# Solution 3 - using sorting - clean the data and return it sorted as a string, then compare the 2 strings

def anagrams_2(s_a, s_b):
    if clean_s(s_a) == clean_s(s_b):
        return True
    return False


def clean_s(s):
    # [^\w] - mathes any char that is not (^) a word (\w)
    # OPTION 1: WE CAN CLEAR, CONVERT TO A LIST AND SORT
    # return "".join(sorted(list(re.sub(r'[^\w]','',s).lower())))
    # WORKS AS WELL WITH LIST ONLY: 
    #return sorted(list(re.sub(r'[^\w]','',s).lower()))
    # WORKS ON THE STRING DIRECTLY: 
    return sorted(re.sub(r'[^\w]','',s).lower())

print(anagrams_2(s1, s2))
