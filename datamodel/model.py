
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
            
        # TODO: interpret comment
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
        