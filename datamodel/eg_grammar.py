
from eg_trans import EG_Trans
import grammar


class EG_Grammar(EG_Trans):

    def __init__(self, model):
        super(EG_Grammar, self).__init__()
        self.rules = []
        self.model = model

    def set_file(self, filename):
        # print 'set file', filename
        self.rules = []

    def generate(self, line, lang1, lang2, category):
        ex = EG_Trans.generate(self, line, lang1, lang2, category)
        # print line, ex
        if len(ex) > 0:
            # print '1:', ex[0].question
            w = ex[0].question
            ww = w.split(' ')
            if len(ww) > 1:
                w = ww[-1]  # TODO: treat not only the last word in question
            self.generate_forms(w)
            # print ff
        else:
            line = self.set_tag(line)
            ex = []
            if '>>' in line:
                r = grammar.Rule(line, self.tag)
                self.rules.append(r)
                # print line
                # print '2: inp', r.input,
                # print '2: out', r.output
                if r.is_one():
                    self.generate_forms(r.input)
        return []

    def active(self, mark):
        return mark == '='

    def generate_forms(self, word):
        used = {}
        for r in self.rules:
            if r.group in used:
                continue
            ff = r.transform(word)
            if len(ff) > 0:
                self.model.forms.store(r.group, word, ff)
                used[r.group] = True
