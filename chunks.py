#  --- Directions
#  Given an array and chunk size, divide the array into many subarrays
#  where each subarray is of length size
#  --- Examples
#  chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
#  chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
#  chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
#  chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
#  chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

# REPL: https://repl.it/@DamyanPeykov/ArrayChunk

# Solution 1: mine - just loop through the length of the array with step of the size

def find_chunks(chunk):
    l = chunk[0]
    size = chunk[1]

    new_list = []
    for i in range(0,len(l),size):
        new_list.append((l[i:i+size]))

    return(new_list)

# print(find_chunks(([1, 2, 3, 4], 2)))
# print(find_chunks(([1, 2, 3, 4, 5], 2)))
# print(find_chunks(([1, 2, 3, 4, 5, 6, 7, 8], 3)))
# print(find_chunks(([1, 2, 3, 4, 5], 4)))
# print(find_chunks(([1, 2, 3, 4, 5], 10)))


# Solution 2: running a loop through all elements and adding chunk by find_chunks

def add_chunks(list_input, size):
    chunked = []

    for element in list_input:
        last = chunked[-1] if chunked != [] else None
        if last == None or len(last) == size:
            chunked.append([element])
        else:
            last.append(element)
    return chunked

print(add_chunks([1, 2, 3, 4], 2))
print(add_chunks([1, 2, 3, 4, 5], 2))
print(add_chunks([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(add_chunks([1, 2, 3, 4, 5], 4))
print(add_chunks([1, 2, 3, 4, 5], 10))
