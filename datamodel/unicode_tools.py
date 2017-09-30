
# -*- coding: utf-8 -*-

import sys
import os

ND = {
    u"a\\": u"à",
    u"a`": u"à",
    u"a^": u"â",
    u"a+": u"æ",
    u"c+": u"ç",
    u"e/": u"é",
    u"e'": u"é",
    u"e\\": u"è",
    u"e`": u"è",
    u"e^": u"ê",
    u"e:": u"ë",
    u"i:": u"ï",
    u"i^": u"î",
    u"o^": u"ô",
    u"o+": u"œ",
    u"u\\": u"ù",
    u"u`": u"ù",
    u"u^": u"û",
    u"u:": u"ü",
    u"y:": u"ÿ"
}


def init():
    if sys.platform == "win32":
        class UniStream(object):
            __slots__ = ("fileno", "softspace", )

            def __init__(self, fileobject):
                self.fileno = fileobject.fileno()
                self.softspace = False

            def write(self, text):
                os.write(self.fileno, text.encode("utf-8"))

        sys.stdout = UniStream(sys.stdout)
        sys.stderr = UniStream(sys.stderr)

    print u'Test UNICODE string: une scène'
    print u'Test UNICODE string: сцена'


def simplify_spaces(line):
    return ' '.join(line.split())


def normalize(text):
    for k, v in ND.iteritems():
        text = text.replace(k, v)
    return text
