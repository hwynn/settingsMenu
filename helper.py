#!/usr/bin/env python3
import os
import enum
import random
current = os.getcwd();
print("hello");
#directory stuff
"""current = current+'\\'+os.listdir(current)[0];
print(os.listdir(current));
os.chdir(current);"""
#new file stuff
"""newfile = open('test1.txt','w');
newfile.write('this is a brand new file.\nHello everyone!!!');
newfile.close();
newfile2 = open('test2.txt','w');
newfile2.write('this another file.\n777-632-0425');
newfile2.close();"""

class MenuItem(object):
	class MenuItemType(enum.Enum):
		choiceInList = 1
		numberInRange = 2
		storedString = 3
	#these are iterable
	print("The iterated enum values are : ")
	for itemtype in (MenuItemType):
		print(itemtype)

	#def __init__(self, numSides=0, color=input("Color of the die: ")): # don't do this
	def __init__(self, propertyTitle, propertyValue, itemType, propertyOptions=[]):
		self.title = propertyTitle
		self.chosen = propertyValue
		#ERROR check: if itemType == 1 then propertyValue should be a number bigger than 0 but no larger than length-1 of propertyOptions
		#ERROR check: if itemType == 2 then propertyValue should be a number between the two numbers in propertyOptions
		#ERROR check: if itemType == 3 then propertyValue should be a string, even an empty string
		self.itemType = self.MenuItemType(itemType)
		self.options = propertyOptions
		#ERROR check: if itemType == 1 then propertyOptions should be a list of several strings
		#ERROR check: if itemType == 2 then propertyOptions list should contain 2 numbers. The first smaller than the second
		#ERROR check: if itemType == 3 then propertyOptions list is useless and should be empty. 
		self.printsize = 0
		if(self.itemType.value == 1):
			for x in self.options:
				self.printsize = self.printsize + 4 + len(x)
		elif(self.itemType.value == 2):
			self.printsize = 4+len(self.chosen)
		elif(self.itemType.value == 3):
			self.printsize = 4+len(str(self.chosen))
		if((len(self.title)+4)>self.printsize):
			self.printsize = (len(self.title)+4)
			
	#def changeValue(newValue):
		#ERROR check: if itemType == 1 then newValue should be a number bigger than 0 but no larger than length of options
		#ERROR check: if itemType == 2 then newValue should be a number between the two numbers in options
		#ERROR check: if itemType == 3 then newValue should be a string
	
	def printTypes(self):
		print()
		print(self.title)
		print(type(self.title))
		print("This menu item is a ", self.itemType.name)
		print("options: ", self.options)
		print("propertyValue: ", self.chosen)
		print(type(self.chosen))
		print("size needed for printing ", self.printsize)
	
	def printMenuItem(self):
		if(self.itemType.value == 1):
			print()
			print('|',end='')
			print(self.title.center(self.printsize),end='')
			print('|')
			print('|',end='')
			for i in range(len(self.options)):
				if(i==self.chosen):
					print(('('+self.options[i]+')').center(4+len(self.options[i])),end='')
				else:
					print(self.options[i].center(4+len(self.options[i])),end='')
			print('|')

"""
	class MenuItemType(enum.Enum):
		choiceInList = 1
		numberInRange = 2
		storedString = 3
"""
print()

#(self, propertyTitle, propertyValue, itemType, propertyOptions=[]):

longest_menu_length = 0;
property_1_title = "border color";
property_1_values = ['black','blue','red','green'];
property_1_chosen = 0;

myBorderColor = MenuItem(property_1_title, property_1_chosen, 1, property_1_values);
print(myBorderColor.itemType.value)
print(myBorderColor.itemType.name)
myBorderColor.printTypes()
myBorderColor.printMenuItem()

property_2_title = "border color";
property_2_values = [];
property_2_chosen = "James";

myCharacterName = MenuItem(property_2_title, property_2_chosen, 3, property_2_values);
myCharacterName.printTypes()
