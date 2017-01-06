##Sentence No. 9302
**Text:** Errare humanum est , perseverare diabolicum ...
###Existing MWEs: 
**MWE No.:** 0
**Text:** ... Errare humanum


**MWE No.:** 1
**Text:** , perseverare
Traceback (most recent call last):


  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1531, in <module>

###Identified MWEs: 

Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Errare .. ]


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Errare]   ; buffer = [humanum .. ]


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Errare, humanum]   ; buffer = [est .. ]


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Errare, humanum, est]   ; buffer = [, .. ]


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Errare, humanum]   ; buffer = [, .. ]


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Errare, humanum, ,]   ; buffer = [perseverare .. ]


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Errare, humanum, ,, perseverare]   ; buffer = [diabolicum .. ]


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Errare, humanum, ,, perseverare, diabolicum]   ; buffer = [...]


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Errare, humanum, ,, perseverare]   ; buffer = [...]


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Errare, humanum, ,, perseverare, ...]   ; buffer = [ ]


ERROR: It's impossible to apply a SHIFT transition, the BUFFER is empty!
