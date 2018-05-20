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
print()

mylist= [textSpeeds[i].center(4+len(textSpeeds[i])) for i in range(len(textSpeeds))]
print(mylist)

choice=1

mylist2 = [ ('('+textSpeeds[i]+')').center(4+len(textSpeeds[i])) if i==choice else textSpeeds[i].center(4+len(textSpeeds[i])) for i in range(len(textSpeeds))]
print('|',end='')
for x in mylist2:
	print(x,end='')
print('|',end='')

print()
print('|',end='')
for i in range(len(textSpeeds)):
	if(i==choice):
		print(('('+textSpeeds[i]+')').center(4+len(textSpeeds[i])),end='')
	else:
		print(textSpeeds[i].center(4+len(textSpeeds[i])),end='')

print('|',end='')
print()