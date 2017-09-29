
class Exercise(object):
    def __init__(self, etype, question, answer, lang1, lang2, category, tag):
        self.etype = etype
        self.question = question.strip()
        self.answer = answer.strip()
        self.lang1 = lang1
        self.lang2 = lang2
        self.category = category
        self.tag = tag

    def __repr__(self):
        r = "%s (%s) [%s, %s]" % ( self.question, self.answer, self.lang1, self.lang2 )
        if len(self.tag)>0:
            r = r + ' #' + self.tag
        if len(self.etype)>0:
            r = self.etype + ' ' + r
        return r

    def __unicode__(self):
        return self.__repr__()

    @staticmethod
    def placeholder():
        return '...'

