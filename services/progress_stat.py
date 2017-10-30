
# -*- coding: utf-8 -*-

import os
from model import Model
from statistics import Stat
from unicode_tools import init
from forms import Forms

init()

pdir = 'progress/french'
m = Model()
print "Loading '%s'..." % pdir,
ok = m.load_dir( pdir )
print ok

#forms = Forms(False)
#forms_path = os.path.join(pdir, 'forms')
#print "Loading forms '%s'..." % forms_path,
#ok = forms.load(forms_path)
#print ok

#print forms.init_forms('ai')

#s = Stat(m, True)
s = Stat(m, False, m.forms)
print s

#for w in s.fwords:
#    print w,
#print

s_path = os.path.join(pdir, 'stat')
f = open(s_path, 'w')
f.write(repr(s))
f.close()

