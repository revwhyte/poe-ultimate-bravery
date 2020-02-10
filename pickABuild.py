# scraper from https://docs.scrapy.org/en/latest/intro/tutorial.html

from random import shuffle, choice
from time import sleep

bonecos = ['duelist','marauder','ranger','scion','shadow','templar','witch']
ascensoes = {
    'duelist': ['slayer', 'champion', 'gladiator'],
    'marauder': ['chieftain', 'berserker', 'juggernaut'],
    'ranger': ['raider', 'pathfinder', 'deadeye'],
    'scion': ['ascendant'],
    'shadow': ['saboteur', 'trickster', 'assassin'],
    'templar': ['hierophant', 'inquisitor', 'guardian'],
    'witch': ['necromancer', 'occultist', 'elementalist'],
}
titles = {
    'duelist': 'handsome ',
    'marauder': 'brave ',
    'ranger': 'ferocious ',
    'scion': 'bitter ',
    'shadow': 'tricky ',
    'templar': 'faithful ',
    'witch': 'insane '
}
skills = {

}
spells = {

}

bonecos.sort()
shuffle(bonecos)
classe = choice(bonecos)
titulo = titles[classe]

ascensoes = ascensoes[classe]
ascensoes.sort()
shuffle(ascensoes)
ascensao = choice(ascensoes)

# chat part
print("Exile, my brothers, sisters and I need your help.")
sleep(1)
print("You, my " + titulo + classe + ", is the one to come in our aid.")
sleep(1)
print("with your " + ascensao + " skills, you may save Oriath from those who got influenced by the Eldritch curse.")