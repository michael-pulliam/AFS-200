# Create a variable called "applePrice" and assign it the value of fifty cents.
applePrice = .50
# apple_price = '{:.2f}'.format(applePrice)
# Write the necessary code to prompt the user to enter their name.
user_name = input('What is your name? ')
# Store the response from the user in a variable as a string.
print(f'Hello, {user_name}')
# Tell the user the cost of an apple.
# Ask the user how many apples they would like to purchase and store this value in a variable as an integer.
buy_num_apples = int(input(f'Apples cost ${applePrice:.2f} ea. How many would you like to purchase? '))
# the number of apples they purchased and the cost of each apple.
total_price = applePrice * buy_num_apples
total_after_tax = total_price * 1.08
print( f"Your total today after tax is: ${total_after_tax:.2f}")
# how much they give to pay with
payment = float(input("How much are you paying with? "))
if payment < total_after_tax:
    print(f"Out of ${payment:.2f}... I'm Sorry {user_name}, this is not enough to pay for your apples.. Your total today after tax is: ${total_after_tax:.2f}.")
    payment = float(input("How much are you paying with? "))
elif payment >= total_after_tax:
# total_payment = "{:.2f}".format(payment)
    print(f"Out of ${payment:.2f}")
# How much change customer gets back
print(f"A total of ${payment - total_after_tax:.2f} is your change.") 
# Thank the user for their purchase.  The message should contain the users name,
print(f'Thank you for your purchase of {buy_num_apples} apples at a cost of ${applePrice:.2f} each. Have a Great Day {user_name}!')

