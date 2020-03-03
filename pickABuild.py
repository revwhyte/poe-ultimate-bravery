# scraper from https://docs.scrapy.org/en/latest/intro/tutorial.html

from random import shuffle, choice
from time import sleep
import gems

def capitalize_all(string):
    new_string = string.split(' ')
    for word in new_string:
        word.capitalize()
    return ' '.join(map(str, new_string))

bonecos = gems.bonecos
titles = gems.titles
ascensoes = gems.ascensoes
skills = gems.skills

# pick char
bonecos.sort()
shuffle(bonecos)
classe = choice(bonecos)
titulo = titles[classe]

# pick ascension
ascensoes = ascensoes[classe]
ascensoes.sort()
shuffle(ascensoes)
ascensao = choice(ascensoes)

# pick skill
skills.sort()
shuffle(skills)
main_skill = choice(skills)

# chat part
print("Exile, we need your help.")
sleep(1)
print("You, my " + titulo.capitalize() + classe.capitalize() + ", is the one to come in our aid.")
sleep(1)
print("with your " + ascensao.capitalize() + " skills, you may save Oriath from those who got influenced by the Eldritch curse.")
sleep(1)
print("I hope you can save us, sice you're the best with your " + capitalize_all(main_skill) + " ability.")