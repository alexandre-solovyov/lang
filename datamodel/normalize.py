
# -*- coding: utf-8 -*-

ND = {
  u"a\\": u"à",
  u"a`" : u"à",
  u"a^" : u"â",
  u"a+" : u"æ",
  u"c+" : u"ç",
  u"e/" : u"é",
  u"e'" : u"é",
  u"e\\": u"è",
  u"e`" : u"è",
  u"e^" : u"ê",
  u"e:" : u"ë",
  u"i:" : u"ï",
  u"i^" : u"î",
  u"o^" : u"ô",
  u"o+" : u"œ",
  u"u\\": u"ù",
  u"u`" : u"ù",
  u"u^" : u"û",
  u"u:" : u"ü",
  u"y:" : u"ÿ"
}

def normalize(text):
    for k, v in ND.iteritems():
        text = text.replace(k, v)
    return text
