from flask import Flask
from flask import Request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the Address Book"
# GET ALL
@app.route("/contacts")
def about():
    return "This is what we are all about!!"
# GET ONE
# @app.route("/contacts/<int:contact_id>")
# def get_one_contact():
#     return f"Here are the details on contact with a UUID of {contact_id}"

@app.route("/home")
def home():
    return "Welcome to the Home page!!"

# @app.route('/cart', methods=['GET', 'POST'])
# def shoppingCart():
#     if request.method == 'POST':
#         product_id = request.form.get('product_id')
#         quantity = request.form.get('qnty')
#         # return add2cart(product_id, quantity)
#         return f"Added {quantity} fo item {product_id} to your cart"
#     else:
#         # return showCart()
#         return "Show items in the cart"

if __name__ == "__main__":
    app.run()