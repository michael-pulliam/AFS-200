# Create a variable called "applePrice" and assign it the value of fifty cents.
applePrice = .50
apple_price = '{:.2f}'.format(applePrice)
# Write the necessary code to prompt the user to enter their name.
user_name = input('What is your name? ')
# Store the response from the user in a variable as a string.
print('Hello, ' + user_name)

# Tell the user the cost of an apple.
# Ask the user how many apples they would like to purchase and store this value in a variable as an integer.
buy_num_apples = int(input(f'Apples cost ${apple_price} ea. How many would you like to purchase? '))
# the number of apples they purchased and the cost of each apple.
total_price = applePrice * buy_num_apples
total_after_tax = total_price * 1.08
print( f"Your total today after tax is: ${total_after_tax:.2f}")
# how much they give to pay with
payment = float(input("How much are you paying with? "))
print("Out of $" + str(payment))
# How much change customer gets back
changeReturn = payment - total_after_tax
change_return = "{:.2f}".format(changeReturn)
print(f"A total of $" + str(change_return) +" is your change." )
# Thank the user for their purchase.  The message should contain the users name,
print(f'Thank you for your purchase of ' + str(buy_num_apples) + ' apples at a cost of $' + str(apple_price) + ' each. ' 'Have a Great Day ' + user_name + '!')

