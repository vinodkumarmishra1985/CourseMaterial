print ("hello world")

#input prompts user to provide input

#name = input("Name: ")

#print ("Hello, "+name)

#Fstring in later version of python
#f  => substitue the value of name varaible in formatted string
# it uses varaibles names in {}

#print (f"Hello, {name}")

#By default input gives string. We need to convert to integer.
#n = int(input("Number: "))
#n =0 
#if n > 0:
 #   print ("n is positive")
#elif n <0:
 #   print ("n is negative")
#else:
 #   print ("n is zero")
    
    
#sequence. Unlike array sequence gives positional character
#name = "Hennry"
#print (name[1])
#names = ["Harry", "Ron", "Vinod"]

#print (names)

#coordinateX = 10.0
#coordinateY = 20.0

#coordianate = (10.0, 20.0)

#print (coordianate)

#Define a list of names
names = ["Vinod", "Kumar", "Mishra", "BEIT"]

#print (names[0])

#Append is a method to add the value in the existing list in the end
#names.append("Draco")

#names.sort() #automatically sort the names in python

#print (names)


#Create an empty set

s = set()

#Add elements to set.
#No elements appear twice in set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
#s.add(5)

s.remove(2)
#print (s)

#print (f"The set has {len(s)} elements.")

#loop

#for i in [0, 1, 2, 3, 5]:
 #   print (i)

#for i in range(6):
 #   print (i)


names = ["Vinod", "Kumar", "mishra"]

#for name in names:
 #   print (name)

#name = "Harry"

#for char in name:
 #   print (char)


#****************************#
houses={"Harry":"Gryffindor", "Vinod":"NC"}

#del houses["Harry"]

for key in houses:
    print (f"Key is {key} and value is {houses[key]}")

#print (houses["Harry"])
#print (houses["SD"])


#def square(x):
 #   return x * x

#from functions import square

#for i in range(10):
 #   print (f"The square of {i} is {square(i)}")


import functions

for i in range(10):
    print (f"The square of {i} is {functions.square(i)}")





    





































