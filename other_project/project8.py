'''
sound
'''

from gtts import gTTS
from playsound import playsound
with open('teclado.txt', 'r') as f:
    f = f.read()
    audio = "speech.mp3"
    language = 'en'
    sp = gTTS(text = f,
                lang= language, slow=False)

    sp.save(audio)
    playsound(audio)


l_2D =[
    [(1, 0), (2, 0), (3, 1)],
    [(4, 1), (5, 0), [6, 1]]
    ]

