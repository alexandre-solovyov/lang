
import codecs
import copy
import os

ENCODING = 'UTF-8'

class Line(object):
    def __init__(self, text, context):
        self.text = text
        self.context = copy.deepcopy(context)

class Model(object):
    def __init__(self):
        self.lines = []
        self.context = {}
        
    def load(self, filename):
        if not os.path.isfile(filename):
            return False
        self.filename = filename
        mfile = codecs.open(filename, 'rb', 'utf-8')
        lines = mfile.readlines()
        mfile.close()
        for line in lines:
            line = self.simplify(line)
            if len(line.text) > 0:
                self.lines.append(line)
        return True
        
    def diff_context(self, old_context, new_context):
        diff = {}
        for key, value in new_context.iteritems():
            if not key in old_context or old_context[key] != value:
               diff[key] = value
        return diff
        
    def save(self, filename):
        self.filename = filename
        mfile = codecs.open(filename, 'wb', 'utf-8')
        old_context = {}
        for line in self.lines:
            diff = self.diff_context(old_context, line.context)
            if len(diff) > 0:
                mfile.write('\n')
                for key, value in diff.iteritems():
                    mfile.write('//! %s: %s\n' % (key, value)) 
            old_context = line.context
            mfile.write(line.text+'\n')
        mfile.close()

    def simplify_spaces(self, line):
        return ' '.join(line.split())

    def simplify(self, line):
        line = self.simplify_spaces(line)
        line = self.comment(line)
        return line
    
    def comment(self, line):
        if '#' in line:
            index = line.index('#')
            length = 1
        elif '//' in line:
            index = line.index('//')
            length = 2
        else:
            return Line(line, self.context)

        comment = line[index+length:]
        if len(comment)>0 and comment[0]=='!':
            # this is the interpreted comment
            comment = comment[1:]
            parts = comment.split(':')
            if len(parts)==2:
                p1 = parts[0].strip()
                p2 = parts[1].strip()
                self.context[p1] = p2
        
        text = line[:index]
        line = Line(text, self.context)
        return line
    
    def value(self, line, key):
        if key in line.context:
            return line.context[key]
        else:
            return None
            
    def values(self, key):
        values_set = set()
        for line in self.lines:
            line_value = self.value(line, key)
            if line_value is not None:
                values_set.add(line_value)
        values_lst = list(values_set)
        values_lst.sort()
        return values_lst

    def update_exercises(self):
        # TODO
        pass

    def choose_exercise(self):
        # TODO
        pass

    def add(self, text, context=None):
        text = self.simplify_spaces(text)
        if len(text)==0:
            return False

        for line in self.lines:
            if line.text==text:
                 return False
        if len(self.lines)>0:
           cur_context = copy.deepcopy(self.lines[-1].context)
        else:
           cur_context = {}
        if context is not None:
             for key, value in context.iteritems():
                  cur_context[key] = value
        new_line = Line(text, cur_context)
        self.lines.append(new_line)
        return True

