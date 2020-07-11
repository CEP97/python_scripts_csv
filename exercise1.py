# Exercise 1 from CSV module
# Author: Goz
# Description: Get information from csv file

import csv

my_csv = open('videogames.csv')
videogames_csv = csv.reader(my_csv)
videogames = list(videogames_csv)

print(videogames)

for videogame in videogames:
    name = videogame[0]
    console = videogame[1]
    release = videogame[2]
    character = videogame[3]
    print(f'{name} de la consola {console} se lanzó en {release} con el personaje {character}')

my_csv.close()
