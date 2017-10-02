﻿
# -*- coding: utf-8 -*-

import os
import codecs
from unicode_utils import init
from statistics import Stat
from model import Model, ENCODING

def freq_cmp(a, b):
    if dwords[a]>dwords[b]:
        return -1
    else:
        return 1;

def show(msg, lst, onlyLen=False, showFreq=False):
    print msg % len(lst)
    if not onlyLen:
        if isinstance(lst, list):
            for w in lst:
                print w, 
                if showFreq:
                    print "(%i)" % dwords[w],
            print
        if isinstance(lst, dict):
            for k, v in lst.iteritems():
                print "%s (%s)" % (k, v), 
            print


init()

print
print 'Text analysis tool'

lang = 'french'
text_file_name = 't0001_paris.txt'
model_dir = os.path.join('progress', lang)



model = Model()
print "Loading '%s'..." % model_dir,
ok = model.load_dir( model_dir )
print ok

text_path = os.path.join('texts', lang, text_file_name)
stat = Stat(model)

print "Loading %s..." % text_path,

tfile = codecs.open(text_path, 'rb', ENCODING)   
print 'True'

lines = tfile.readlines()
tfile.close()

dwords = {}
for line in lines:
    stat.add(line, dwords, True)

words = dwords.keys()
words.sort(freq_cmp)

show(">> There is %i known words:", stat.fwords, True)
show(">> Found %i new words:", words, False, True)