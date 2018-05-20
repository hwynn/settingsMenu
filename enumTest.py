#!/usr/bin/env python3
import os
import enum

class MenuItemType(enum.Enum):
	choiceInList = 1
	numberInRange = 2
	storedString = 3

#print enum member as string
print("The string representation of enum member is: ",end=" ")
print(MenuItemType.choiceInList)

#print enum member as repr
print("The repr representation of enum member is : ",end=" ")
print(repr(MenuItemType.choiceInList))

#print the type of enum member using type()
print ("The type of enum member is : ",end=" ")
print (type(MenuItemType.choiceInList))

#printing the name of enum member using "name" keyword
print ("The name of enum member is : ",end=" ")
print (MenuItemType.choiceInList.name)

print ("Other enum access stuff: ")
print(MenuItemType(1))
print(MenuItemType['numberInRange'])
print()
mem = MenuItemType.storedString
print(mem.value)
print(mem.name)
print()

thing = MenuItemType(2)
print(thing.value)
print(thing.name)
print()