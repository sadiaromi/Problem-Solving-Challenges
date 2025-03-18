def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count

print(count_vowels("Apple"))
print(count_vowels("Watermelon"))
print(count_vowels("Grapes"))