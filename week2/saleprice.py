# Prompt the user to enter a description for a product.
product = input("Please enter Product Description: ")
print(f"You added {product}")
# Prompt the user to enter the quantity being purchased stored as an integer. 
quantity = int(input("Enter the Quantity you would like: "))
print(f"You added {quantity}")
# Prompt the user to enter the regular price of the product. This value must be stored as a float.
reg_price = float(input("Add Items regular price: $"))
# print(f"Added Regular Price at: ${reg_price:.2f}")
# All of the products over $19.99 are 15% OFF
discount1 = reg_price * .15
# All of the products over $39.99 are 25% OFF
discount2 = reg_price * .25
# Assume a state sales tax rate of 6.5%.  
state_tax = 0.065
add_tax = 1.065
if reg_price < 20:
    print(f"Item price ${reg_price:.2f} x {quantity}")
    print(f"Sales Tax ${reg_price * state_tax:.2f}")
    print(f"Total ${quantity * reg_price * add_tax:.2f}")
elif reg_price > 19.99 and reg_price < 40:
    after_discount1 = float(reg_price - discount1)
    print(f"Item price ${reg_price:.2f}")
    print(f"After 15% discount: ${after_discount1:.2f} x {quantity}")
    print(f"Sales Tax ${quantity * after_discount1 * state_tax:.2f}")
    print(f"total ${quantity * after_discount1 * add_tax:.2f}")
    print(f"You saved ${quantity * reg_price * .25:.2f}")
elif reg_price > 39.99:
    after_discount2 = float(reg_price - discount2)
    print(f"Item price ${reg_price:.2f}")
    print(f"After 25% discount: ${after_discount2:.2f} x {quantity}")
    print(f"Sales Tax ${quantity * after_discount2 * state_tax:.2f}")
    print(f"total ${quantity * after_discount2 * add_tax:.2f}")
    print(f"You saved ${quantity * reg_price * .25:.2f}")
    
# Calculate the sales tax on the total purchase. 
 
# The rate should be calculated on the total price of the products after discount savings.
# Store this value as float in a variable.
# Display the total amount due from the customer.
# Format the output as a fixed point number with two-decimal places, a comma as a thousand separator and the dollar sign.
# Display the total amount saved.