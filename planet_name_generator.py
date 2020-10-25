import random
import string

class Planet:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


def create_name(vow_lst, conson_lst):
    name = ""
    names_lenght = random.choice([n for n in range(2,5)])
    first_letter = random.choice(["vowel", "consonant"])
    count_double_letters = 0

    for num in range(names_lenght // 2 + 1):
        vowel = random.choice(vow_lst)
        consonant = random.choice(conson_lst)

        if names_lenght % 2 != 0:
            if first_letter == "vowel":
                name += consonant + vowel

            else:
                name += vowel + consonant
        else:
            if first_letter == "vowel":
                if 1 <= len(name) >= 3:
                    if count_double_letters < 1:
                        consonant = "".join(random.sample(conson_lst, 2))
                        count_double_letters += 1
                        if consonant.startswith("j"):
                            consonant = random.choice(conson_lst)
                            count_double_letters -= 1
                else:
                    consonant = random.choice(conson_lst)
                name += consonant + vowel
                
            else:
                if num > 3:
                    vowel = "".join(random.sample(vow_lst, 2))
                name += vowel + consonant
        
    if name.startswith("y") or name.startswith("q"):
        name = name[::-1]

    return name.title()

with open("vowels.txt", "r") as v, \
        open("consonants.txt", "r") as c:
        vowels_lst = [line for line in v.read() if line != "\n"]
        consonants_lst = [line for line in c.read() if line != "\n"]

name = create_name(vowels_lst, consonants_lst)
planet_0 = Planet(name)
