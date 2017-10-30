
# -*- coding: utf-8 -*-

import os
import codecs
from unicode_tools import init
from statistics import Stat
from model import Model, ENCODING
from forms import Forms

dwords = {}

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

def analyze(lang, text_file_name):
    global dwords
    
    model_dir = os.path.join('progress', lang)
    model = Model()
    print "Loading '%s'..." % model_dir,
    ok = model.load_dir( model_dir )
    print ok
    
    print 'Number of forms:', model.forms.nb_forms()
    #model.forms.dump()
    #print model.forms.forms('premier', 'FemPl')
    #return 
    
    text_path = os.path.join('texts', lang, text_file_name)
    stat = Stat(model, False, model.forms)

    print "Loading %s..." % text_path,

    tfile = codecs.open(text_path, 'rb', ENCODING)   
    print 'True'

    lines = tfile.readlines()
    tfile.close()

    dwords = {}
    for line in lines:
        stat.add(line, dwords, True, model.forms)
    
    words = dwords.keys()
    words.sort(freq_cmp)

    show(">> There is %i known words:", stat.fwords, True)
    show(">> Found %i new words:", words, False, True)

init()

print
print 'Text analysis tool'

#analyze('french', 't0001_paris.txt')
#analyze('french', 't0002_ecole_primaire.txt')
#analyze('french', 't0003_fetes.txt')
analyze('french', 't0004_tgv.txt')
#analyze('french', 't0005_fromage.txt')


#analyze('french', "Ensemble, c'est tout.txt")
#analyze('german', 't0001_berlin.txt')




