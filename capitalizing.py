#  --- Directions
#  Write a function that accepts a string.  The function should
#  capitalize the first letter of each word in the string then
#  return the capitalized string.
#  --- Examples
#    capitalize('a short sentence') --> 'A Short Sentence'
#    capitalize('a lazy fox') --> 'A Lazy Fox'
#    capitalize('look, it is working!') --> 'Look, It Is Working!'

# REPL: https://repl.it/@DamyanPeykov/sentencecapitalization

# Solution 1: the shortest one - using the python built-in function title()
s = 'a short sentence'

print(s.title())

# Solution 2: splitting the sentence by words, looping & capitalizing and returning the result as a string
def capitalize_words(s):
    words = s.split(" ")
    capitalized = ""
    for word in words:
        capitalized += word.capitalize() + " "
        # alternative to capitalize() - just take the 1st letter and use upper():
        # capitalized += word[0].upper() + word[1:] + " "

    return capitalized
    
print(capitalize_words(s))

# Another possible solution is to loop through the string and check if the char on the left of the current char is a space => capitalize the currrent 
# This solution is not that good, because it can cause problems with the FIRST word/char in the sentence
