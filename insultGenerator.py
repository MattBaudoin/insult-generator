#  Personalized insult generator that asks the users name and then returns a random insult from the available list that includes their name in the insult.

import random

print('Hi, what\'s your name?')

myname = input()  # get name from user

library = [(myname + ', if you aren\'t an idiot, you made a world-class effort at simulating one.'),
           (myname + ' has the personality of wallpaper.'),
           ('I will never get over the embarrassment of belonging to the same species as you, ' + myname + '.'),
           (myname + ' has bad breath!'),
           ('Someday ' + myname + ' will go far. I hope they stay there forever.'),
           (myname + ', I have neither the time nor the crayons to explain this to you.')
           ]

insult = random.choice(library)

print(insult)
