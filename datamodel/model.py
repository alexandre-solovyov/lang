
import codecs
import copy

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
        self.filename = filename
        mfile = codecs.open(filename, 'rb', 'utf-8')
        lines = mfile.readlines()
        mfile.close()
        for line in lines:
            line = self.simplify(line)
            if len(line.text) > 0:
                self.lines.append(line)
    
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

    def simplify(self, line):
        line = ' '.join(line.split())
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
        