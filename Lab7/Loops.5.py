def get_character_frequencies(input_string):
    frequencies = {}
    for char in input_string:
        char = char.lower()  # Convert to lowercase for case-insensitive counting
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

mydict = get_character_frequencies("SNow White and the Seven Dwarfs")


print(mydict)
sortted_by_key = dict(sorted(mydict.items()))
print(sortted_by_key)