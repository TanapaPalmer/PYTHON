#Countdown
for a in range (5, -1, -1):
    if a % 1 == 0:
        print(a)

##################################################

#Print and Return
list = [1,2]
print(list[0])

def print_and_return(list):
    return list[1]
print(list[1])
print_and_return(list)

##################################################

#First Plus Length
first_plus_length = [1,2,3,4,5]
first_value = first_plus_length[0]
print(first_value+len(first_plus_length))

##################################################

#Values Greater than Second
vg_list = [5,2,3,2,1,4]
        
def values_greater_than_second(vg_list):
    x = [num for num in vg_list if num > 2]
    print(len(x))
    print(x)

    if len(x) < 2:
        print("True")
    else:
        print("False")
        
        
values_greater_than_second(vg_list)

##################################################

#This Length, That Value
length_and_value = [4,7]

first=[length_and_value[1]]*length_and_value[0]
print(first)

length_and_value = [6,2]

second=[length_and_value[1]]*length_and_value[0]
print(second)

##################################################