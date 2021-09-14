a_string = "Abcde"
lowercase = a_string.lower()
# Convert to lowercase

vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)
# Count vowels

    vowel_counts[vowel] = count
# Add to dictionary


print(vowel_counts)