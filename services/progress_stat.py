
# -*- coding: utf-8 -*-

import glob
from model import Model
from statistics import Stat
from unicode_utils import init

init()
files = glob.glob('../progress/*.lang')
for f in files:
    m = Model()
    print "Loading '%s'..." % f,
    ok = m.load(f)
    print ok
    s = Stat(m)
    print s
