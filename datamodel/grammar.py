
import re
import model

class Rule:
    def __init__(self, rule, group):
        self.group = group
        parts = rule.split('>>')
        if len(parts)==2:
            self.input = parts[0].strip()
            self.output = [x.strip() for x in parts[1].split(',')]
        else:
            self.input = ''
            self.output = []
        reg = '^' + self.input.replace('~', '(\w*)') + '$'
        self.reg = re.compile(reg, re.UNICODE)
        
    def __rshift__(self, forms):
        self.output = forms
        
    def match(self, word):
        m = self.reg.match(word)
        if m is None:
            return False, ''
        elif m.lastindex==None:
            return True, word
        else:
            return True, m.group(m.lastindex)

    def transform(self, word):
        ok, base = self.match(word)
        if ok:
            return [x.replace('~', base) for x in self.output]
        else:
            return []

    def includes(self, rule2):
        i = rule2.input.replace('~', '')
        ok, base = self.match(i)
        return ok

    def is_one(self):
        return not '~' in self.input
