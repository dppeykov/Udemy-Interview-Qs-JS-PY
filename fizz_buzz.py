# Print the numbers from 1 to n. The multiplies by 3 = fizz, *5 = buzz, *3&5 = fizzbuzz

# Solution 1: checking and printing with continue
def fizz_buzz(n):
    for num in range(1,n+1):
        if num%3 == 0 and num%5 == 0:  # could be (num%15 == 0) as well
            print("fizzbuzz")
        elif num%3 == 0:
            print("fizz")
        elif num%5 == 0:
            print("buzz")
        else:
            print(num)

fizz_buzz(15)

# Keep the code simple - it's better to be readable and don't try to overcomlicate it with 1 liners
