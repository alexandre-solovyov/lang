
# -*- coding: utf-8 -*-

import re

class Stat(object):
    def __init__(self, model):
        self.pattern = re.compile('\W+', re.UNICODE)
        self.lines  = len(model.lines)            
        self.exercises = len(model.exercises)
        self.language = model.language()
        
        lang = None
        if len(self.language) > 0:
            lang = self.language[0]

        self.words  = self.count(model, '', 0)
        self.fwords = self.count(model, lang, 0)
        self.swords = self.count(model, lang, 2)

    def __repr__(self):
        s = ''
        if len(self.language)==2:
            s = s + ( "  Language:      %s <=> %s\n" % ( self.language[0], self.language[1] ) )
        s = s + ( "  Lines:         %i\n" % self.lines )
        s = s + ( "  Exercises:     %i\n" % self.exercises )
        s = s + ( "  All words:     %i\n" % self.words )
        s = s + ( "  Foreign words: %i\n" % self.fwords )
        s = s + ( "  Studied words: %i\n" % self.swords )
        return s
               
    @staticmethod
    def lang_comp(lang1, lang2):
        return lang1=='' or lang1==lang2
        
    def count(self, model, lang, mode):
        words = {}
        for e in model.exercises:
            if mode==0 or mode==1:
                if self.lang_comp(lang, e.lang1):
                    self.add(e.question, words)
            if mode==0 or mode==2:
                if self.lang_comp(lang, e.lang2):
                    self.add(e.answer, words)
        return len(words)
        
    def add(self, text, words):
        ww = re.split(self.pattern, text)
        for w in ww:
            if len(w)>0:
                words[w] = True
