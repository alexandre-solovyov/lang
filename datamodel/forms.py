
# -*- coding: utf-8 -*-

import copy
from unicode_tools import ext_concat

FORMS = {}
RFORMS = {}
IS_COMPLETE = False

class Tense:
    def __init__(self, name):
        self.name = name


class Word:
    def __init__(self, text, tense=''):
        self.text = text
        self.tense = tense
    
    def __add__(self, arg):
        #print 'add', repr(arg)
        if isinstance(arg, Word):
            return Word(self.text + arg.text, self.tense)
        elif isinstance(arg, str):
            return Word(self.text + arg, self.tense)
        elif isinstance(arg, list):
            return Word([self.text + a for a in arg], self.tense)
        elif isinstance(arg, Tense):
            return Word(self.text, arg.name)
        else:
            return self
    
    def __repr__(self):
        return repr(self.text)
        
    def __call__(self, *kwarg):
        #print 'call', repr(self)
        for a in kwarg:
            ff = ext_concat(a, self.text)
            if isinstance(ff, str):
                self.store(self.tense, a, ff)
            elif isinstance(ff, list):
                for f in ff:
                    self.store(self.tense, a, f)
            
    def store(self, tense, init_form, custom_form):
        #print tense, init_form, custom_form
        
        if tense not in FORMS:
            FORMS[tense] = {}
        if init_form not in FORMS[tense]:
            FORMS[tense][init_form] = [custom_form]
        elif IS_COMPLETE or custom_form not in FORMS[tense][init_form]:
            FORMS[tense][init_form].append(custom_form)
          
        if custom_form not in RFORMS:
            RFORMS[custom_form] = [init_form]
        else:
            if init_form not in RFORMS[custom_form]:
                RFORMS[custom_form].append(init_form)

class Forms:

    def __init__(self, isComplete):
        self.isComplete = isComplete
        self.context = {'w': Word('~'), 'Tense': Tense}

    def load(self, filename):
        global IS_COMPLETE
        global FORMS
        global RFORMS
        FORMS = {}
        RFORMS = {}
        IS_COMPLETE = self.isComplete
        execfile(filename, self.context)
        self._forms = copy.deepcopy(FORMS)
        self._rforms = copy.deepcopy(RFORMS)
        #print self._forms
        #print self._forms['PrInd']
        #print self._rforms

    def forms(self, word, group):
        try:
            return self._forms[group][word]
        except:
            return [word]

    def init_forms(self, word):
        try:
            return self._rforms[word]
        except:
            return [word]
