
from model import Model
from unicode_tools import init
from ev_console import EV_Console
import random

print 'Lang console application'
init()

print 'Loading model...'
model = Model()
model.load('progress/french.lang')

print 'Language: %s' % model.language()
n = len(model.exercises)
print 'Exercises: %i' % n

view = EV_Console()

ind = random.randint(0, n) # TODO
e = model.exercises[ind]
#print unicode(e)

view.show(e)
