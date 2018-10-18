#List of chords in a key based on the major scale
major_scale = [
    ['A', 'Bm', 'C#m','D', 'E', 'F#m', 'G#dim'],
    ['Bb', 'Cm', 'Dm', 'Eb', 'F', 'Gm', 'Adim'],
    ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'],
    ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'],
    ['Db', 'Ebm', 'Fm', 'Gb', 'Ab', 'Bbm', 'Cdim'],
    ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'],
    ['Eb', 'Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Ddim'],
    ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'],
    ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'],
    ['Gb', 'Abm', 'Bbm', 'B', 'C#', 'D#m', 'Fdim'],
    ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'],
    ['Ab', 'Bbm', 'Cm', 'Db', 'Eb', 'Fm', 'Gdim']       
]

import random

x = random.randint(0,11)
y = random.randint(3,4)

key = major_scale[x][0]
interval = random.sample(range(1,7), y)
question = key, *interval

print("\n--What are the chords related to the numbers below?")
print("--If there isn't a 4th chord, press enter\n")
print(*question,"\n")

chord1 = input("1st chord?> ")
chord2 = input("2nd chord?> ")
chord3 = input("3rd chord?> ")
chord4 = input("4th chord?> ")

print("Is this correct?:", chord1, chord2, chord3, chord4)
