
# -*- coding: utf-8 -*-

class Forms:

    def __init__(self, isComplete):
        self.isComplete = isComplete
        self._forms = {}
        self._rforms = {}
        
    def forms(self, word, group):
        try:
            return self._forms[group][word]
        except:
            return [word]

    def store(self, group, word, forms):
        #print group, word, forms
        if not group in self._forms:
            self._forms[group] = {}
        self._forms[group][word] = forms
        for f in forms:
            if not f in self._rforms:
                self._rforms[f] = []
            if not word in self._rforms[f]: 
                self._rforms[f].append(word)
        
    def init_forms(self, word):
        try:
            lst = self._rforms[word]
            res = []
            for q in lst:
                if q in self._rforms:
                    rq = self.init_forms(q)
                    for q1 in rq:
                        res.append(q1)
                else:
                    res.append(q)
            return res
        except:
            return [word]

    def nb_forms(self):
        return len(self._rforms)
        
    def dump(self):
        for k in self._rforms.keys():
            print k,
        print
