# scraper from https://docs.scrapy.org/en/latest/intro/tutorial.html

from random import shuffle, choice
from time import sleep
from termcolor import colored, cprint
import sys
import data


def capitalize_all(string):
    new_string = string.split(' ')
    for word in new_string:
        word.capitalize()
    return ' '.join(map(str, new_string))


# start
classes = data.classes
skills = data.skills
bonecos = [key for key in classes.keys()]


# pick char
# 1. object
bonecos.sort()
shuffle(bonecos)
saida = classes[choice(bonecos)]
# 2. pick ascension
ascensao = saida[0]
ascensao.sort()
shuffle(ascensao)
ascensao = choice(ascensao)
# 3. pick title
titulo = saida[1]
# 4. pick color
cor = choice(['red', 'green', 'blue'])


# pick skill
skills.sort()
shuffle(skills)
main_skill = choice(skills)


# coloring text
titulo = colored(titulo.capitalize(), cor)
ascensao = colored(ascensao.capitalize(), cor)
main_skill = colored(capitalize_all(main_skill), cor)

# chat part
print("Exile, we need your help.")
sleep(1)
print("You, my " + titulo  + " " + ascensao + ", is the one to come in our aid.")
sleep(1)
print("You may save Oriath from Sirus' menace.")
sleep(1)
print("I hope you can save us, with your " + main_skill + " skills.")