#  --- Directions
#  Given a string, return a new string with the reversed
#  order of characters
#  --- Examples
#    reverse('apple') === 'leppa'
#    reverse('hello') === 'olleh'
#    reverse('Greetings!') === '!sgniteerG'

# REPL: https://repl.it/@DamyanPeykov/stringreversal

# Solution 1: loop O(n) 
s = "hello"

def rev_loop(s):
    r = ""
    for ch in s:
        r = ch + r
    return(r)

# OR range:
def rev_range(s):
    r =""
    for i in range(len(s)-1,-1,-1):
	    r = r+ s[i]
    return r

# Solution 2 - using the reversed function on a list - O(n)
def rev_func(s):
    return "".join(list(reversed(s)))

# Solution 3 - slicing - should be O(n) - going through the whole str
def rev_shortcut(s):
    return s[::-1]

# Solution 4 - reduce - O(n)
# IMPORTANT: the reduce function receives the "" string as a first argument
from functools import reduce

def rev_reduce(s):
    return reduce(lambda r,ch: ch + r ,list(s), "")


print(rev_loop(s))
print(rev_range(s))
print(rev_func(s))
print(rev_shortcut(s))
print(rev_reduce(s))
