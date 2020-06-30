import string

with open("vowels.txt", "w") as v, open("consonants.txt", "w") as c:
    for vowel in "aeiouy":
        v.write(vowel + "\n")
    for consonant in string.ascii_lowercase:
        if consonant not in "aeiouy":
            c.write(consonant + "\n")
