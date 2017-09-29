
import unittest

from test_model import TestModel
from test_generators import TestGenerators
from unicode_utils import init
 
try:
    init()
    unittest.main()
except Exception as error:
    print "Unexpected error:", format(error)
