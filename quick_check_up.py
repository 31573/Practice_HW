# Print Hello User!
user =  input("What is your name? ")
print ("Hello " + str(user))

# Take in User Input
last_name = input("What's your last name? ")

# Respond Back with User Input
print("Hello, " + str(user)+" " + str(last_name))

# Take in the User Favorite Number
number = input("What's your favorite number? ")

# Respond Back with a statement based on your favorite number
if (int(number) == 7):
    print ("It's the same as mine!")
elif (int(number) >7):
    print("It's higher than mine!")
else: 
    print("Its lower than mine!")
                