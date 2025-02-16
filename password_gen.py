import random
import string

characters_lowercase = []
characters_uppercase = []
numbers = []
for i in string.ascii_lowercase:
    characters_lowercase.append(i)
for i in string.ascii_uppercase:
    characters_uppercase.append(i)
for i in range(0, 10):
    numbers.append(i)


char1 = 0
char2 = 0
char3 = 0
part1 = ""
part2 = ""
part3 = ""
while char1 < 6:
    random_char = random.choice(characters_lowercase)
    part1 += random_char
    char1 += 1
while char2 < 6:
    random_num = str(random.choice(numbers))
    part2 += random_num
    char2 += 1
while char3 < 6:
    random_upchar = random.choice(characters_uppercase)
    part3 += random_upchar
    char3 += 1
def password_gen():
    print(part1 + "-" + part2 + "-" + part3)
password_gen()
    

