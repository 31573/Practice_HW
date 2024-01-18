# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = []

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the house of pies!")

for pie in pie_list:
    print(f"[{pie_list.index(pie)+1}] {pie}")

# While we are still shopping...
while shopping =="y":
    
   pie_choice = input("Which would you like? ")
   pie_purchases.append(pie_choice)
   
   print("Great!, we'll have the " + pie_list[int(pie_choice)-1] + " for you. ")
  
   shopping = input("Would you like another pie? (y /n): ")
   
print("You ordered a total of " + str(len(pie_purchases)) + " pies with us.")


# Loop through the full pie list
for pie_index in range(len(pie_purchases)):
      pie_name = str(pie_purchases[pie_index])

   
      print(pie_name)



  