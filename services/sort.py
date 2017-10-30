
# -*- coding: utf-8 -*-

import os
from model import Model
from unicode_tools import init

def sort_all(lang):
    model_dir = os.path.join('progress', lang)
    model = Model()

    ff = model.all_files( model_dir )

    fname = ff[2]
    p = fname.split('.')
    fname1 = p[0] + '_s' + '.' + p[1]
    print fname
    print fname1
    model.load(fname)
    model.short_ignore = ['une', 'un']
    model.sort()
    model.save(fname1)
    

init()

print
print 'Sorting tool'

sort_all( 'french' )

