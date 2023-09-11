# basic import
import playlist

playlist.play("Digimon - Butterfly")
playlist.DURATION

# recommended import
import playlist as pl

print(pl.GENRE)
pl.play("Naturo - Flow") # kalo ga pake print dia function

# opsi lain
from playlist import GENRE, DURATION, TYPE, play, pause

print(DURATION) # kalo pake print berarti dia variable
print(GENRE)
print(TYPE)

play("Ndasku Mumet - Sadikin")
pause("Ndasku Ra Mumet - Sadimin")

# import module yang sudah ada
import math
import os

print(math.pi)

from math import pi, e # e untuk epsilon

print(pi)
print(e)


# Buatlah sebuah modul game
# Modul tersebut memiliki fungsi terkait Hero, Item, Enemy, Area dan Rank
# Lalu import modul game tersebut ke satu file python bernama main.py

import game

game.hero('Elquartz')
game.item('Elquartz,','Katana')
game.enemy('PMS Rika')
game.area('Purwokerto')
game.rank('99')