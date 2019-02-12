#1.

print("Please Enter A Number")

Number = input()

if int(Number) > 100: 
	print("That's a big number")

else: 
	print("Why not dream a little bigger")


#2.

print("What is Your Age?")

Age = int(input()) 


if int(Age) >= 105:
	print("lol i don't think that's your that age")

else: print("We are {} years apart".format((((Age) - 21)**2)**0.5))
#3

name = "Josh"

print("What Is Your Name?")

user_name = input()
if user_name == name:
	print("We have the same name!")

else: print("Get a better name!!!!!!")


#4
secret_number = 7
print("What is the SECRET NUMBER?")
user_input = int(input())

if secret_number == (user_input):
	print("YOU! WIN!!!")
elif user_input == 6 or user_input == 8:
	print("SOO CLOSE!")
else: print("Try Again!")