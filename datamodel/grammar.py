
"""Implementation of the grammar rules"""

import re


class Rule(object):
    """Class for grammar rule"""

    def __init__(self, rule, group):
        """Constructor"""
        self.group = group
        parts = rule.split('>>')
        if len(parts) == 2:
            self.input = parts[0].strip()
            self.output = [x.strip() for x in parts[1].split(',')]
        else:
            self.input = ''
            self.output = []
        reg = '^' + self.input.replace('~', r'(\w*)') + '$'
        self.reg = re.compile(reg, re.UNICODE)

    def __rshift__(self, forms):
        """Implementation of the right shift operator to assign forms"""
        self.output = forms

    def match(self, word):
        """Check if the given word matches to rule"""
        match1 = self.reg.match(word)
        if match1 is None:
            return False, ''
        elif match1.lastindex is None:
            return True, word
        else:
            return True, match1.group(match1.lastindex)

    def transform(self, word):
        """Transform the given word according to the rule"""
        ok, base = self.match(word)
        if ok:
            return [x.replace('~', base) for x in self.output]
        else:
            return []

    def includes(self, rule2):
        """Check if this rule includes another one"""
        i = rule2.input.replace('~', '')
        ok, base = self.match(i)
        return ok

    def is_one(self):
        """Check if this rule corresponds to only one word"""
        return '~' not in self.input
