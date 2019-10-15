#  --- Directions
#  Given an integer, return an integer that is the reverse
#  ordering of numbers.
#  --- Examples
#    reverseInt(15) === 51
#    reverseInt(981) === 189
#    reverseInt(500) === 5
#    reverseInt(-15) === -51
#    reverseInt(-90) === -9

# Solution 1: converting the int and using slices
def reverse_int(num):
    if num < 0:
        return int(str(num)[1:].strip("0")[::-1]) * -1
    return int(str(num).strip("0")[::-1])

print(reverse_int(-90))

# Solution 2: getting the sign + reversing the number & stripping 0s and -

def rev_int_sign(num):
    sign = -1 if num < 0 else 1
    return int(str(num)[::-1].strip("0-")) * sign

print(rev_int_sign(-15000000001000000))


