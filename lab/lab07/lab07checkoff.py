class VendingMachine:
	v = 0
	def __init__(self):
		self.soda = JunkDrink(self)

class JunkDrink:
	v = 0 
	def __init__(self, machine):
		self.machine= machine 
		self.machine.v += 1
		machine.v += 1
		self.v += 1

# python tutor: http://pythontutor.com/composingprograms.html#mode=display

>>>a=VendingMachine()
>>>a.v
2
>>>JunkDrink.v
0
>>>a.soda.v
1
>>>x=VendingMachine.__init__(a)
>>>x
(Nothing gets displayed)
>>>a.v
4
>>>JunkDrink.v
0
>>>a.soda.v

# A very good example, be sure to review 
