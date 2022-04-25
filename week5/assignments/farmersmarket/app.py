from flask import Flask
from flask import Request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the Farmers Market!"

@app.route("/home")
def home():
    return "Welcome to the home page"

@app.route("/products/<int:product_id")
def products(product_id):
    # show the products with the given id, the id is an integer
    return f"Here are the details on product with an ID of {product_id}"

@app.route('/cart', methods=['GET', 'POST'])
def shoppingCart():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        quantity = request.form.get('qnty')
        # return add2cart(product_id, quantity)
        return f"Added {quantity} fo item {product_id} to your cart"
    else:
        # return showCart()
        return "Show items in the cart"

if __name__ == "__main__":
    app.run()