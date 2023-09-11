# untuk package harus disave dibagian folder file __init__.py  

import Music.Playlist.play  as Play # kalo package aliasing dengan huruf besar
import Music.Playlist.pause as Pause # cek di terminal folder yang akan dituju
import Music.Playlist.load as Load # import nama folder.subfoler.module

Play.play('Duit - Alyn')
Pause.pause('Uang - Aisyah')
Load.load('Tas Sepatu - Mama')

# Kembangkanlah modul game yang sudah dibuat sebelumnya menjadi package
# Package tersebut berupa folder yang memuat modul-modul terkait Hero, Item, Enemy, Area dan Rank
# Lalu import package game tersebut ke satu file python bernama main.py

import Game.hero as Hero
import Game.rank as Rank
import Game.enemy as Enemy
import Game.item as Item
import Game.area as Area

Hero.hero('Elquartz')
Item.item('Elquartz,','Katana')
Enemy.enemy('PMS Rika')
Area.area('Purwokerto')
Rank.rank('99')