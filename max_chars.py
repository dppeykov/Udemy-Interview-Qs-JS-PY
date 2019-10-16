#  --- Directions
#  Given a string, return the character that is most
#  commonly used in the string.
#  --- Examples
#  maxChar("abcccccccd") === "c"
#  maxChar("apple 1231111") === "1"

# OTHER QUESTIONS LIKE THIS: anagrams & repeated characters in string

# Solution 1: using a loop - my own solution
s = "apple 1231111"
counter = 0
most_common = ""
for item in s:
    if s.count(item) > counter:
        counter = s.count(item)
        most_common = item
print(most_common)

# Solution 2: using a the Counter from the collections library
from collections import Counter
print(Counter(s). most_common(1)[0][0])

# Solution 3: creating a dictionary map of all the items in the string and checking the max value 
chars = {}
for item in s:
    if item not in chars:
        chars[item] = 1
    else:
        chars[item] += 1

# print(sorted(chars.items(), key=lambda x: x[1])) # to sort by the values

# print(chars) # {'a': 1, 'p': 2, 'l': 1, 'e': 1, ' ': 1, '1': 5, '2': 1, '3': 1}

# Definition of max: max(iterable, *iterables[,key, default])
# We are giving the key, which is equal to:
# def lambda_func(chars, key):
#   return chars[key] --->> will return the key instead of the value
# In this case max is retutning the key of the most common letter

print(max(chars, key=lambda key: chars[key]))

# instead of using max, we can loop through the chars dictionary and find the max
