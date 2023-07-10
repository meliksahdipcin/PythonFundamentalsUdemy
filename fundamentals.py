print("Hello World")

#Numbers & Mathmematical Operations
2+1 #addition
2-1 #substraction
2*3 #multiplication
4/2 #division
9%2 #mod operation
2 ** 3 #third power
4 ** 2 #second power

print(2+10*10+3)
print((2+10)*(10+3))

#Variables
a = 5
print(a)
a = 10
print(a)

a = a + a
print(a)

print(type(a))
b = 1.1
print(type(b))

myIncome = 100
myRate = 0.1
myTaxes = myIncome * myRate
print(myTaxes)

#Strings
a = "string"
b = 'this is a string, too.'
print("Hello \nWorld") #new line
print("Hello \tWorld") #tab
print(len("This string")) #length of the string

#Indexing and Slicing with Strings
string = "Hello World"
print(string[0])
print(string[1])
print(string[-1]) #negative indexing

alphabeticalString = "abcdefghijk"
print(alphabeticalString[2:])
print(alphabeticalString[:3])
print(alphabeticalString[2:4])
print(alphabeticalString[::2])
print(alphabeticalString[2:7:2])
print(alphabeticalString[::-1])

#String Properties & Methods
name = "Sam"
lastLetters = name[1:]
print("P" + lastLetters)

sentence = ", coding is cool!"
print("Hello World" + sentence)

letter = "z"
print(letter*10)

print(2+3)
print("2"+"3")

sentence = "Hello World"
print(sentence.upper()) #capitalise
print(sentence.split()) #split the words

string = "This is a string"
print(string.split("i")) # split for every "i" letter

#Print Formatting with Strings
print("This is a string {}".format("INSERTED"))
print("{} {} {}".format("fox", "brown", "quick"))
print("{2} {1} {0}".format("fox", "brown", "quick"))
print("{0} {0} {0}".format("fox", "brown", "quick"))
print("{b} {f} {q}".format(f="fox", b="brown", q="quick"))

#Float formatting
result = 100/777
print(result)
print("The result was {}".format(result))
print("The result was {r:1.2f}".format(r=result))
print("The result was {r:10.4f}".format(r=result))

name = "Melikşah"
print(f"Hello, my name is {name}") #(this is available in Pyhton 3.6)

name = "Melikşah"
age = 18
print(f"{name}'s age is {age}")

#Lists
myList = [1,2,3]
myList = [1,1.5,"String"]
print(len(myList))

myList = ["one","two","three"]
print(myList[0])
print(myList[1:])

anotherList = ["four","five"]
print(myList+anotherList)

myList[0] = "ONE"
print(myList)

myList.append("four")
print(myList)

myList.pop() #deletes theh last datum
print(myList)

myList = ["one","two","three","four","five"]
poppedItem = myList.pop()
print(poppedItem)

myList.pop(2)
print(myList)

newList = ["a","e","x","b","c"]
numList = [4,1,8,3]
newList.sort()
numList.sort()
print(newList)
print(numList)
numList.reverse()
print(numList)

#Dictionaries
myDictionary = {"key1":"value1","key2":"value2"}
print(myDictionary)

priceDictionary = {"apple":2.99,"orange":1.99,"milk":5.80}
print(priceDictionary["apple"])

d = {"k1":123,"k2":[0,1,2],"k3":{"insideKey":100}}
print(d["k1"])
print(d["k3"]["insideKey"])

d = {"key1":["a","b","c"]}
myList = d["key1"]
letter = myList[2]
print(letter.upper())
#or
print(d["key1"][2].upper())


d = {"k1":100,"k2":200}
d["k3"] = 300
print(d)
d["k1"] = 400
print(d)

print(d.keys())
print(d.values())

#Tuples
myTuple = (1,"two",3)
print(type(myTuple))
print(len(myTuple))
print(myTuple[0])
print(myTuple[-1])
#can't --> myTuple[0] = "NEW"


letterTuple = ("a","a","b")
print(letterTuple.count("a"))
print(letterTuple.index("a"))
print(letterTuple.index("b"))

#Sets
mySet = set()
print(mySet)
mySet.add(1)
print(mySet)
mySet.add(2)
# can't add the same object more than one mySet.add(2)

myList = [1,1,1,1,1,2,2,2,2,2,3,3,3]
settedList = set(myList)
print(settedList)

#Booleans
print(type(False))
print(type(True))

print(1>2)
print(2==2)

#Comparison Operations
print(2==1)
print(1==1)
print("hello"=="hello")
print(2.0==2)
print(1=="1")

print(3!=2)
print(3!=3)
print(1>2)
print(1<2)

print(2>=2)
print(3<=1)

print(1<2<3)
print(1<2>3)
print(1<2 and 2<3)
print("h"=="h" and 1==1)

print(100==1 or 2==2) #it is true if one of the statements is true

print(not(1==1)) #shows the oppesite boolean

#If statements
if True:
	print("It's true")

hungry = True
if hungry == True:
	print("I am hungy")
else:
	print("I am not hungry")


location = "Bank"
if location == "Auto shop":
	print("Cars are cleaned")
elif location == "Bank":
	print("Love money")
else:
	print("I don't know my location")

#For Loops
myList = [1,2,3,4,5,6,7,8,9,10]
for num in myList:
	print(num)

for num in myList:
	#Check for even
	if num % 2 == 0:
		print(num)
	else:
		print(f'Odd number: {num}')

listSum = 0
for num in myList:
	listSum = listSum + num
print(listSum)

myString = "Hello World"
for letter in myString:
	print(letter)

my List = [(1,2),(3,4),(5,6),(7,8)]
print(len(myList))
for item in myList:
	print(item)
for a,b in myList:
	print(b)

myList = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in range:
	print(b)

dictionary = {"k1":1,"k2":2,"k3":3}
for item in dictionary:
	print(item)
for item in dictionary.items():
print(item)
for item in dictionary.values():
print(item)

for _ in "loops":
	print("Interesting")

#While Loops
x = 0
while x < 5:
	print(f"the current value of x is {x}")
	x += 1
else:
	print("x is not less than 5")

x = [1,2,3]
for item in x:
	pass #pass prevents a syntax error as a placeholder
print("end")

string = "Apples"
for letter in string:
	if letter == "l":
		continue
	print(letter)

x = 0
while x < 5:
	if x == 2:
		break
	print(x)
	x += 1

#Some Useful Operators in Python
for num in range(10):
	print(num)

for num in range(3,10,2):
	print(num)

print(list(range(0,11,2)))

indexCount = 0
word = "abcde"
for letter in word:
	print(word[indexCount])
	indexCount += 1

word = "abcde"
for item in enumerate(word):
	print(item)

word = "abcde"
for index,letter in enumerate(word):
	print(index)
	print(letter)
	print("\n")

myList1 = [1,2,3,4,5,6]
myList2 = ["a","b","c"]
myList3 = [100,200,300]
for item in zip(myList1,myList2,myList3):
	print(item)

print("x" in [1,2,3])
print("x" in ["x","y","z"])
print("a" in "a world")
print("mykey" in {"mykey":123})

dictionary = {"mykey":123}
print(345 in dictionary.values())
print(345 in dictionary.keys())

myList = [10,20,30,40,50]
print(min(myList))
print(max(myList))

from random import shuffle
myList = [1,2,3,4,5,6,7,8,9,10]
shuffle(myList)
print(myList)

from random import randint
print(randint(0,100)) #gives a random integer

myNumber = randint(0,100)
print(myNumber)

result = input("What is your name? ") #always string
print(result)
print(float(result))

#List Comprehensions
myString = "Hello"
myList = []
for letter in myString:
	myList.append(letter)
print(myList)

myString = "Hello"
myList = []
myList = [letter for letter in myString]
print(myList)

myList = []
myList = [num for num in range(0,10)]
print(myList)

myList = []
myList = [num**2 for num in range(0,10)]
print(myList)

myList = []
myList = [x for x in range(0,11) if x%2 == 0]
print(myList)

celciusDegrees = [0,10,20,34.5]
fahrenheitDegrees = [(9/5) * temp + 32 for temp in celciusDegrees]
print(fahrenheitDegrees)

fahrenheitDegrees = []
for temp in celciusDegrees:
	fahrenheitDegrees.append(9/5 * temp + 32)
print(fahrenheitDegrees)

results = [x if x % 2 == 0 else "ODD" for x in range(0,11)]
print(results)

myList = []
for x in [2,4,6]:
	for y in [1,10,1000]:
		myList.append(x*y)
print(myList)

myList = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(myList)

#Functions
def say_hello():
	print("Hello")
	print("World")
say_hello()

def say_hello(name):
	print(f"Hello {name}")
say_hello("Melikşah")

def add_num(num1,num2):
	return num1 + num2
result = add_num(10,20)
print(result)

def add_num(num1,num2):
	print(num1 + num2)
add_num(10,20)
add_num("10","20")

def even_check(number):
	result = number % 2 == 0:
	return result
even_check(20)
even_check(21)

def check_even_list(num_list):
	#Return true if any number is even inside a list
	for number in num_list:
		if number % 2 == =:
			return True
		else:
			pass
		return False
check_even_list([1,2,3,4,5,6])

def check_even_list(num_list):
	#Return all the even numbers in a list
	#Placeholder variables
	even_numbers = []
	for number in num_list:
		if number % 2 == 0:
			even_numbers.append(number)
		else: pass
	print(even_numbers)
check_even_list([1,2,3,4,5,])

#Tuple Unpacking with Functions
stock_prices = [("AAPl",200),("GOOG",400),("MSFT",100)]
for item in stock_prices:
	print(item)

for ticker,price in stock_prices:
	print(ticker)
	print(price)
	print(price*1.1) #to see 10% price increase

work_hours = [("Abby",100),("Billy",400),("Cassie",800)]
#Let's see which employee worked most
def employee_check():
	current_max = 0
	employee_of_month = " "
 	for employee,hours in work_hours:
		if hours > current_max:
			current_max = hours
			employee_of_month = employee
		else:
			pass
	return (employee_of_month,current_max)
employee_check(work_hours)

#Shuffle
from random import shuffle
example = [1,2,3,4,5,6,7]
shuffle(example)
print(example)

def shuffle_list(myList):
	shuffle(myList)
	return myList
result = shuffle_list(example)
print(result)

#Combining functions
myList = [" ","O"," "]
shuffle_list(myList)
def player_guess():
	guess = " "
	while guess not in ["0","1","2"]:
		guess = input("Pick a number from 0 to 2: ")
	return int(guess)
def check_guess(myList,guess):
	if myList[guess] == "O":
		print("Correct!")
	else:
		print("Wrong!")
		print(myList)
#1) Initial list
myList = [" ","O"," "]
#2) Shuffle list
mixedup_list = shuffle_list(myList)
#3) User guess
guess = player_guess()
#4) Check guess
check_guess(mixedup_list,guess)

#*args -- Arbitrary numbers

def myfunc(a,b):
	#Return 5% of the sum
	return sum((a,b))*0.05
myfunc(40,50)

def myfunc(*args):
	return sum(*args)*0.05
myfunc(20,1,35,35,69,23,)

#**kwargs
def myfunc(**kwargs):
	if "fruit" in kwargs:
		print("My fruit of choice is {}".format(kwargs["fruit"]))
	else:
		print("I did not find any fruit here")
myfunc(fruit = "apple")

def myfunc(*args,**kwargs):
	print(args)
	print(kwargs)
	print("I would like {} {}".format(args[0],kwargs["food"]))
myfunc(10,20,30,fruit="orange",food="eggs",animal="dog")

#Map
def square(num):
	return num**2
my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
	print(item)
print(map(square,my_nums))
print(list(map(square,my_nums)))

def splicer(myString):
	if len(myString) % 2 == 0:
		return "Even"
	else:
		return myString[0]
names = ["Andy","Eve","Sally"]
print(list(map(splicer,names)))

def check_even(num):
	return num % 2 == 0
myNums = [1,2,3,4,5,6]
print(list(filter(check_even,myNums)))

#Lambda
def square(num): return num ** 2
print(square(3))

square = lambda num: num ** 2
print(square(3))

print(list(map(lambda num: num**2,myNums)))

print(list(filter(lambda num: num%2==0,myNums)))

print(list(map(lambda name: name[0],names)))





























































