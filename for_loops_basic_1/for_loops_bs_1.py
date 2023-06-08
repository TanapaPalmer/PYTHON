#Basic
for x in range (1, 101):
    if x % 1 == 0:
        print(x)

#Multiples of Five
for x in range (5, 1000):
    if x % 5 == 0:
        print(x)

#Counting, the Dojo Way
for x in range (1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#Whoa. That Sucker's Huge
sum = 0
for x in range (0, 500001):
    if x % 2 != 0:
        print(x)
        sum = sum + x
print(sum)

#Countdown by Fours
for x in range (2018, 0, -1):
    if x % 4 == 2:
        print(x)

#Flexible Counter
lowNum = 2
highNum = 9
multNum = 3
x = multNum

for x in range (lowNum, highNum+1):
    if x % 3 == 0:
        print(x)
