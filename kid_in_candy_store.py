# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for candy in candy_list:
    print(f"[{str(candy_list.index(candy))}] {candy}")
     
    
answer = "yes"

while answer == "yes":
    print("Which candy would you like to bring home?")
    selected = input("Input the number associated with the candy you want: ")
    
    candy_cart.append(candy_list[int(selected)])

    answer = input("would you like another candy? (yes or no): ")
        
print("I  brought honw with me: ")
for candy in candy_cart:
    print (candy)
    