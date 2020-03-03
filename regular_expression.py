# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:23:34 2019

@author: Abirmoy
"""

import re

s = '100,000,0000.0'

#re.split(pattern, string, maxsplit=0, flags=0)
x = re.split(r'[,-.]',s) # will ignore comma to dash
print(x)

#print(re.split('[a-x]+', '0xax3Bxx9', flags=re.IGNORECASE))

'''
Split string by the occurrences of pattern. If capturing parentheses are used 
in pattern, then the text of all groups in the pattern are also returned 
as part of the resulting list. If maxsplit is nonzero, at most maxsplit 
splits occur, and the remainder of the string is returned as the final element 
of the list. (Incompatibility note: in the original Python 1.5 release, 
maxsplit was ignored. This has been fixed in later releases.)

>>> re.split('\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split('(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split('\W+', 'Words, words, words.', 1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
If there are capturing groups in the separator and it matches at the start
 of the string, the result will start with an empty string. The same holds for
 the end of the string:

>>> re.split('(\W+)', '...words, words...')
['', '...', 'words', ', ', 'words', '...', '']
That way, separator components are always found at the same relative indices
 within the result list (e.g., if there’s one capturing group in the separator,
 the 0th, the 2nd and so forth).

Note that split will never split a string on an empty pattern match. 
For example:

>>> re.split('x*', 'foo')
['foo']
>>> re.split("(?m)^$", "foo\n\nbar\n")
['foo\n\nbar\n']
'''
