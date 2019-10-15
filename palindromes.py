#  --- Directions
#  Given a string, return true if the string is a palindrome
#  or false if it is not.  Palindromes are strings that
#  form the same word if it is reversed. *Do* include spaces
#  and punctuation in determining if the string is a palindrome.
#  --- Examples:
#    palindrome("abba") === true
#    palindrome("abcdefg") === false

# REPL: https://repl.it/@DamyanPeykov/palindromes


# Solution 1: reversing the string with slicing and comparing
def palindorme_sh_rev(s):
    return s == s[::-1]

print(palindorme_sh_rev("abcdefg"))

# Solution 2: using a loop and going through all posibilities - not the best solution
def palindrome_loop(s):
    for i in range(len(s)):
        if s[i] == s[len(s)-i-1]:
            continue
        else:
            return False
    return True

print(palindrome_loop("tattarrattat"))

# Solution 3: deque - double ended queue - can add and remove items from the front & the back - can be FIFO & LIFO or just the either of them

class Deque:
    def __init__(self):
        self.items = []

    def add_back(self, item): # O(1)
        self.items.append(item)

    def add_front(self,item):
        self.items.insert(0,item) # O(n)

    def remove_back(self): # O(1)
        return self.items.pop()
    
    def remove_front(self): # O(n)
        return self.items.pop(0)

    def get_size(self): # O(1)
        return len(self.items)

    def is_empty(self): # O(1)
        return self.items == []


def palindrome_checker(s):
    # add the items to the Deque
    pal_d = Deque()
    for item in s:
        pal_d.add_back(item)

    while pal_d.get_size() >= 2:

        if pal_d.remove_front() != pal_d.remove_back():
            return False
    
    return True

print(palindrome_checker("tattarrattat"))
