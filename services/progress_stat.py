
# -*- coding: utf-8 -*-

from model import Model
from statistics import Stat
from unicode_utils import init

init()

pdir = 'progress/french'
m = Model()
print "Loading '%s'..." % pdir,
ok = m.load_dir( pdir )
print ok
#s = Stat(m, True)
s = Stat(m, False)
print s
