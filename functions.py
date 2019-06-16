#(""""""""FUNCTIONS"""""""")
#def greet():
    #print("good morning")
#greet()
#print("i m out side the funtions")
#greet()
#print("completed")

#def addition():
    #a = 2
    #b= 3
    #my_sum = a + b
    #print(my_sum)
#addition()

#a = int(input("enter thenumber"))
#b = int(input("enter the second number"))
#def add(num1,num2): # recieve information/data called parameter
    #my_sum = num1 + num2
    #print(my_sum)
#add(a,b) #passins data called argument
#print("...... calculator .......")
#first = int(input("enter the first number :"))
#sec = int(input("enter the second number: "))
#opr = input("enter the funtion:")

#if opr == "-":
    #def subtract(num1,num2):
        #sub = num1 - num2
        #print(sub)
    #subtract(first,sec)
#elif opr == "*":
    #def multiply(num1,num2):
        #mul = num1*num2
        #print(mul)
    #multiply(first,sec)
#elif opr == "/":
    #def divide(num1, num2):
        #div = num1/num2
        #print(div)
    #divide(first,sec)0
'''
def pizza(crust, *topping): # single * means is aa tuple
    print("you have orderd pizza with", crust, "crust and the following toppings :")
    for each in topping:
        print(each)
pizza("thick","green olives","chicken","jalepeno")
'''

def pizza(crust, **topping): # double * means is a dictionary
    print("you have orderd pizza with", crust, "crust and the following toppings :")
    for key, value in topping.items():
        print(key,":",value)
pizza("thick",topping1 ="green olives", topping2 ="chicken",topping3 ="jalepeno")



