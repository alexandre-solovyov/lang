
# -*- coding: utf-8 -*-

import sys
import os


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
