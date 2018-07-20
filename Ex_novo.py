# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:15:56 2018

@author: Theo B.R
"""

import time
import random


nomes = ['Isgalamido', 'MOD_TRIGGER_HURT', 'MOD_FALLING', 'Dono da Bola', 'Zeh']
ident = 2
connection = False
collect = True
Kill = False
entrada = input('Digite o nome do arquivo:')
Abrir = open(entrada, 'r')
print('InitGame: {0}'.format(Abrir))

tempo = time.clock()

if tempo == 900:
    print('Exit: Timelimit hit')

client = input('User name: ')

num = 0

change = input('ClientUserinfoChanged: ')
client = change
while num <= 2:
    num += 1
change = print('ClientUserinfoChanged: {0}'.format(ident))

start = print('ClientBegin: {0}'.format(ident))

start_client = print('ClientConnect: {0}'.format(ident))

if connection == True:
    ident += 1
    print(start_client)


Item_1 = 'weapon_rocketlauncher'
Item_2 = 'health_large'
Item_3 = 'ammo_rockets'
Item_4 = 'item_armour_body'
Item_5 = 'item_armor_shard'
Item_6 = 'ammo_shells'
Item_7 = 'item_health_mega'
Item_8 = 'item_armor_combat'
Item_9 = 'weapon_railgun'
Item_10 = 'item_quad'
Lista_item = ['weapon_rocketlauncher', 'health_large', 'ammo_rockets', 'item_armour_body', 'item_armour_shard', 'ammo_shells', 'item_health_mega', 'item_armour_combat', 'weapon_railgun', 'item_quad']
for i in Lista_item:
    Lista_item = Lista_item

item_coletado = input('Item: {0} '.format(ident))
if item_coletado in Lista_item:
    print('Item: {0} {1}'.format(ident, item_coletado))

if Kill == True:
    print('<world> killed {0} by {1}'.format(random.choice(nomes), random.choice(nomes)))

print('''ShutdownGame:
         ------------------------------------------------------------
         ------------------------------------------------------------''')
tempo_2 = time.clock()
if tempo_2 == 2:
    quit()

    

