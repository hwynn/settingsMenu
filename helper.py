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

class Menu(object):
	def __init__(self):
		self.width = 0;
		self.items = [];

	def addItem(self, pTitle, pValue, iType, pOptions=[]):
		f_menuItem = MenuItem(pTitle, pValue, iType, pOptions)
		if(f_menuItem.outerprintsize < self.width):
			f_menuItem.outerprintsize = self.width		#adjusting padding on the smaller new menu item
		elif(f_menuItem.outerprintsize > self.width):
			self.width = f_menuItem.outerprintsize
			for(x in Menu.items):						#adjusting padding on all past menu items to fit this new big item
				Menu.items.outerprintsize = self.width
		self.items.append(f_menuItem)
		#deep copy lists if needed
	
	def printMenu(self):
		for(x in Menu.items):
			x.printMenuItem()

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
		self.outerprintsize = self.printsize
			
	#def changeValue(newValue):
		#ERROR check: if itemType == 1 then newValue should be a number bigger than 0 but no larger than length of options
		#ERROR check: if itemType == 2 then newValue should be a number between the two numbers in options
		#ERROR check: if itemType == 3 then newValue should be a string

	def printMenuItem(self):
		f_indent = 2;
		f_title = ((' '*f_indent)+ self.title.ljust(self.printsize-f_indent))
		print('|',f_title.ljust(self.outerprintsize),'|',sep='')	
	
		if(self.itemType.value == 1):
			f_options1 = ''
			for i in range(len(self.options)):
				if(i==self.chosen):
					f_options1= f_options1 + ('('+self.options[i]+')').center(4+len(self.options[i]))
				else:
					f_options1= f_options1 + self.options[i].center(4+len(self.options[i]))
			print('|', f_options1.ljust(self.outerprintsize), '|',sep='')


print()

#(self, propertyTitle, propertyValue, itemType, propertyOptions=[]):

longest_menu_length = 0;
property_1_title = "border color";
property_1_values = ['black','blue','red','green'];
property_1_chosen = 0;

myBorderColor = MenuItem(property_1_title, property_1_chosen, 1, property_1_values);
print(myBorderColor.itemType.value)
print(myBorderColor.itemType.name)
print()



property_2_title = "test speed";
property_2_values = ['slow','medium','fast'];
property_2_chosen = 1;

myTextSpeed = MenuItem(property_2_title, property_2_chosen, 1, property_2_values);


myBorderColor.printMenuItem()
myTextSpeed.printMenuItem()

property_5_title = "border color";
property_5_values = [];
property_5_chosen = "James";
