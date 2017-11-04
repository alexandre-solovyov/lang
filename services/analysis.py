
# -*- coding: utf-8 -*-

import os
import codecs
from unicode_tools import init
from statistics import Stat
from model import Model, ENCODING
from forms import Forms
import time
import glob

dwords = {}
model = None

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
            if len(lst)>0:
                print
        if isinstance(lst, dict):
            for k, v in lst.iteritems():
                print "%s (%s)" % (k, v), 
            if len(lst)>0:
                print

def load_model(lang):
    global dwords
    global model
    
    model_dir = os.path.join('progress', lang)
    model = Model()
    print "Loading '%s'..." % model_dir,
    ok = model.load_dir( model_dir )
    print ok
    
    print 'Number of forms:', model.forms.nb_forms()
    print
    
    #model.forms.dump()
    #print model.forms.forms('premier', 'FemPl')
    #return 
    
def analyze(lang, text_file_name):
    global dwords
    global model
    
    if model is None:
        load_model(lang)
        
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
    print

def analyze_all(lang):
    path = os.path.join('texts', lang)
    files = [x for x in os.listdir(path) if x.endswith(".txt") and x.startswith("t")]
    for fname in files:
        analyze(lang, fname)
    
init()

print
print 'Text analysis tool'
print

t0 = time.time()

#analyze('french', 't0001_paris.txt')
#analyze('french', 't0002_ecole_primaire.txt')
#analyze('french', 't0003_fetes.txt')
#analyze('french', 't0004_tgv.txt')
analyze('french', 't0005_fromage.txt')
#analyze_all('french')


#analyze('french', "Ensemble, c'est tout.txt")
#analyze('german', 't0001_berlin.txt')

t1 = time.time()
print
print "Time: %f s" % (t1 - t0)
