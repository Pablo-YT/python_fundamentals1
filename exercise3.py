print("What is Your Name")

user_name = input()

print("Hello, {}".format(user_name))

secret_password = 'please'

print("What's the password?")

password_attempt = input()

correct_or_not = (password_attempt == secret_password)

print("That's {}!".format(correct_or_not))


print("How Many cookies have been eaten?")

eaten = input()

remaining_cookies = 12 - int(eaten)

print("there are {} cookies left.".format(remaining_cookies))

#Bouns

print("How old are you?")

age = input()

print("lol you are {} years old".format(age))