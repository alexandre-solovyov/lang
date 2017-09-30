
# -*- coding: utf-8 -*-

from unicode_tools import normalize

class EV_Console(object):
	def __init__(self):
		pass

	def show(self, ex):
		#print ex.etype, ex.tag, ex.category
		#print ex.question
		#print ex.answer
		
		print
		print 'QUESTION:', ex.question
		ans = raw_input('ANSWER: ')
		ans = ans.encode('utf-8')

		nans = normalize(ans)
		print
		print 'YOUR ANSWER:', nans
		print 'CORRECT ANSWER:', ex.answer
