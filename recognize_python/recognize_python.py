num1 = 42 #variable declaration - primitive type - numbers (integer)
num2 = 2.3 #variable declaration - primitive type - numbers (float)
boolean = True #variable declaration - primitive type - boolean
string = 'Hello World' #variable declaration - primitive type - strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #composite type - lists
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #composite type - dictionaries
fruit = ('blueberry', 'strawberry', 'banana') #composite type - lists
print(type(fruit)) #type check - output: ('blueberry', 'strawberry', 'banana')
print(pizza_toppings[1]) #log statement - output: 'Sausage'
pizza_toppings.append('Mushrooms') #adding - output: ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives', 'Mushrooms']
print(person['name']) #log statement - output: 'John'
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2]) #log statement - output: 'banana'

#conditional
if num1 > 45: 
    print("It's greater")
else:
    print("It's lower") #output: It's lower - because num1 is 42 which is less than 45

#conditional
if len(string) < 5: #legnth check
    print("It's a short word!")
elif len(string) > 15: #legnth check
    print("It's a long word!")
else:
    print("Just right!") #output: Just right! - because string is 11 and it's more than 5 and less than 15

#for loop
for x in range(5):
    print(x) #output: 0,1,2,3,4
for x in range(2,5):
    print(x)  #output: 2,3,4
for x in range(2,10,3):
    print(x) #output: 2,5,8
x = 0
#while loop
while(x < 5):
    print(x) #output: 0,1,2,3,4 because 
    x += 1

pizza_toppings.pop() #to remove - remove the last string in the list which is 'Olives'
pizza_toppings.pop(1) #to remove - remove the position of 1 in the list which is 'Sausage'

print(person) #output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color') #to remove - remove the 'eye_color'
print(person) #output: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

#for loop
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue #for loop - continue - to continue the loop if topping is Pepperoni
    print('After 1st if statement') #output: 'After 1st if statement' because the Pepperoni is in the pizza_toppings
    if topping == 'Olives': #Olives is no longer in the pizza_toppings because it has been removed in line 43
        break #for loop - break - to break the loop if topping is Olives

#function
def print_hello_ten_times():
    for num in range(10): #for loop
        print('Hello') #output: Hello - 10 times

print_hello_ten_times()

#function
def print_hello_x_times(x):
    for num in range(x): #for loop
        print('Hello') #output: Hello - 4 times

print_hello_x_times(4)

#function
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #output: Hello - 14 times

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
print(num3) #NameError: name <variable name> is not defined

fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# fruit[0] = 'cranberry'

print(person['favorite_team']) #KeyError: 'favorite_team'
# print(person['favorite_team'])

print(pizza_toppings[7]) #IndexError: list index out of range
# print(pizza_toppings[7])

    print(boolean) #IndentationError: unexpected indent
#   print(boolean)

fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
# fruit.append('raspberry')
print(fruit)

fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'
# fruit.pop(1)