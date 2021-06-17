'''
Please write a program to generate 
all random sentences where 
subject is in ["I", "You"] and 
verb is in ["Play", "Love"] and 
the object is in ["Hockey","Football"].
'''

import random
subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey","Football"]

for i in range(10):
    print("%s %s %s." % (random.choice(subject), random.choice(verb), random.choice(object)))
