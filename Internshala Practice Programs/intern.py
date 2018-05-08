##class Rectangle:
##    pass
##def print_area(rectangle_object):
##    a = rectangle_object.width * rectangle_object.length
##    print(a)
##react1 = Rectangle()
##react1.width = 5
##react1.length = 4
##print_area(react1)
##react2 = Rectangle()
##react2.width = 6
##react2.length = 7
##print_area(react2)


##class rectangle:
##    def print_area(self):
##        a = self.width * self.length
##        print(a)
##react1 = rectangle()
##react1.width = 5
##react1.length = 4
##react1.print_area()       


##class BankAccount:
##    def __init__(self):
##        self.balance = 0
##
##    def withdraw(self, amount):
##        self.balance -= amount
##        print (self.balance)
##
##    def deposit(self, amount):
##        self.balance += amount
##        print (self.balance)
##
##a = BankAccount()
##b = BankAccount()



def main():
	try:
		f = open('intern.txt')
		for line in f:
			print (line, end="")
	except IOError as e:
		print ("Couln't open the file")
		print (e)
	except ValueError as e:
		print ("Incorrect filename")
		print (e)

if __name__ == '__main__' : main()
