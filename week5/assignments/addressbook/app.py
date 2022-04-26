from flask import Flask
from flask import Request
# import requests
app = Flask(__name__)

# def getData(subject):
#     URL = "https://randomuser.me/api/"+subject+".json"
#     try:
#         response = requests.get(URL, timeout=5)
#         response.raise_for_status()
#         response_JSON = response.json()
#         return response_JSON
#     except requests.exceptions.HTTPError as errh:
#         print(errh)
#     except requests.exceptions.ConnectionError as errc:
#         print(errc)
#     except requests.exceptions.Timeout as errt:
#         print(errt)
#     except requests.exceptions.RequestException as err:
#         print(err)
        
# json_users_data = getData("results")

@app.route("/")
def hello():
    return "Welcome to the Address Book"
# GET ALL
@app.route("/contacts")
def about():
    return "This is what we are all about!!"

@app.route("/home")
def home():
    return "Welcome to the Home page!!"

if __name__ == "__main__":
    app.run()
    
# GET ONE
# @app.route("/contacts/<int:contact_id>")
# def get_one_contact():
#     return f"Here are the details on contact with a UUID of {contact_id}"

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