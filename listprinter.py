#!/usr/bin/env python3
import os

#test speed
#slow (medium) fast

textSpeeds = ['slow', 'medium', 'fast']
printsize = 0
for x in textSpeeds:
	printsize = printsize + 4 + len(x)
print(printsize)
print('text speed'.center(printsize))
for i in range(len(textSpeeds)):
	print(textSpeeds[i].center(4+len(textSpeeds[i])),end='')
