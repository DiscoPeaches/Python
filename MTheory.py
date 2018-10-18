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

print(*question)
