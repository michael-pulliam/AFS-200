from flask import Flask
from flask import request, render_template
import requests
import addressbook
# import json

app = Flask(__name__)

def getData(quantity, nat):
    
    URL = f"https://randomuser.me/api/?results={quantity}&nat={nat}"
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
        
display_users = addressbook.AddressBook()
json_users_data = getData(25, 'us')

for user in json_users_data['results']:
    first_name = user['name']['first']
    last_name = user['name']['last']
    email = user['email']
    user_name = user['login']['username']
    password = user['login']['password']
    UUID = user['login']['uuid']
    home_number = user['phone']
    mobile_number = user['cell']
    picture_large = user['picture']['large']
    picture_thumbnail = user['picture']['thumbnail']
    
    # print(f'{first_name} {last_name} ({email})')
    new_user = addressbook.Contact(first_name, last_name, email, user_name, password, UUID, home_number, mobile_number, picture_large, picture_thumbnail)
    display_users.addAddress(new_user)


@app.route("/", methods=['GET'])
def contacts():
    return render_template('index.html', contacts=display_users.addresses)
# GET ONE
@app.route("/search", methods=['POST'])
def search_contacts():
    search_input = request.form.get('search')
    search_result = display_users.findAllMatching(search_input)
    return render_template('index.html', contacts=search_result)

if __name__ == "__main__":
    app.run()
    


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