
# -*- coding: utf-8 -*-

import re


class Stat(object):

    def __init__(self, model, verbose=False, forms=None):
        self.pattern = re.compile('\W+', re.UNICODE)
        self.lines = len(model.lines)
        self.exercises = 0
        self.categories = {}
        for c, elist in model.exercises.iteritems():
            self.categories[c] = len(elist)
            self.exercises = self.exercises + len(elist)

        self.language = model.language()
        self.verbose = verbose
        self.model = model

        lang = None
        if len(self.language) > 0:
            lang = self.language[0]

        self.fwords = []

        self.words = self.find('', 0, '', forms)
        self.fwords = self.find(lang, 0, 'Foreign', forms)
        self.swords = self.find(lang, 2, 'Studied', forms)

    def __repr__(self):
        s = ''
        if len(self.language) == 2:
            s = s + ("  Language:      %s <=> %s\n" %
                     (self.language[0], self.language[1]))
        s = s + ("  Lines:         %i\n" % self.lines)
        s = s + ("  Exercises:     %i\n" % self.exercises)
        s = s + ("  Categories:")
        for c, cnt in self.categories.iteritems():
            s = s + " %s (%i)" % (c, cnt)
        s = s + "\n"
        s = s + ("  All words:     %i\n" % len(self.words))
        s = s + ("  Foreign words: %i\n" % len(self.fwords))
        s = s + ("  Studied words: %i\n" % len(self.swords))
        return s

    @staticmethod
    def lang_comp(lang1, lang2):
        return lang1 == '' or lang1 == lang2

    def find(self, lang, mode, mode_name, forms):
        words = {}
        for c, elist in self.model.exercises.iteritems():
            for e in elist:
                if mode == 0 or mode == 1:
                    if self.lang_comp(lang, e.lang1):
                        self.add(e.question, words, False, forms)
                if mode == 0 or mode == 2:
                    if self.lang_comp(lang, e.lang2):
                        self.add(e.answer, words, False, forms)

        if self.verbose and len(mode_name) > 0:
            print
            print mode_name + ':',
            ww = words.keys()
            ww.sort()
            for w in ww:
                print w,
            print

        _words = words.keys()
        _words.sort()
        return _words

    def add(self, text, words, only_new=False, forms=None):
        p = text.find('=')
        if p >= 0:
            text = text[:p]
        ww = re.split(self.pattern, text)

        for w in ww:
            w = w.lower()
            if forms is None:
                wf = [w]
            else:
                wf = forms.init_forms(w)
                # if wf[0]!=w:
                #    print w, wf

            for w in wf:
                if len(w) == 0:
                    continue
                if w in self.model.ignore:
                    continue
                if w.isdigit() or w.replace('e', '').isdigit():
                    continue
                if only_new and w in self.fwords:
                    # print 'Ignore:', w
                    continue

                if w in words:
                    words[w] = words[w] + 1
                else:
                    words[w] = 1
