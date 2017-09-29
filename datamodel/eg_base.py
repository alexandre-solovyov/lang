
class EG_Base(object):

    def __init__(self):
        self.tag = ''

    def set_tag(self, line):
        p1 = line.find('[')
        p2 = line.find(']')
        if p1 >= 0 and p2 > p1:
            self.tag = line[p1 + 1:p2]
            line = line[:p1] + line[p2 + 1:]
        return line
