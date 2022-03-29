# products = ["apple", "orange", "Pear"]
# Prompt the user to enter a description for a product.
product = input("Please enter Product Description: ")
print(f"You added {product}")
# Prompt the user to enter the quantity being purchased stored as an integer. 
quantity = int(input("Enter the Quantity you would like: "))
print(f"You added {quantity}")
# Prompt the user to enter the regular price of the product. This value must be stored as a float.
reg_price = float(input("Add Items regular price: "))
print(f"Added Regular Price at: ${reg_price:.2f}")
# All of the products over $19.99 are 15% OFF
if reg_price > 19.99:
    reg_price - reg_price * .15
print(f"total: {reg_price}")
# if reg_price > 19.99 - {reg_price * .15}
# All of the products over $39.99 are 25% OFF
# Calculate the sales tax on the total purchase. 
 
# Assume a state sales tax rate of 6.5%.  
# The rate should be calculated on the total price of the products after discount savings.
# Store this value as float in a variable.
# Display the total amount due from the customer.
# Format the output as a fixed point number with two-decimal places, a comma as a thousand separator and the dollar sign.
# Display the total amount saved.