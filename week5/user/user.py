
import requests

class User:
    
    def __init__(self, first_name, last_name, email, user_name, password, UUID, home_number, mobile_number, picture_large, picture_thumbnail):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.user_name=user_name
        self.password=password
        self.UUID=UUID
        self.home_number=home_number
        self.mobile_number=mobile_number
        self.picture_large = picture_large
        self.picture_thumbnail = picture_thumbnail
        
    def set_first_name(self, first_name):
        self.first_name = first_name
    def get_first_name(self):
        return self.first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    def get_last_name(self):
        return self.last_name
    
    def set_email(self, email):
        self.email = email
    def get_email(self):
        return self.email
    
    def set_user_name(self,user_name):
        self.user_name = user_name
    def get_user_name(self):
        return self.user_name
    
    def set_password(self, password):
        self.password = password
    def get_password(self):
        return self.password
    
    def set_UUID(self, UUID):
        self.UUID = UUID
    def get_UUID(self):
        return self.UUID
    
    def set_home_number(self,home_number):
        self.home_number = home_number
    def get_home_number(self):
        return self.home_number
    
    def set_mobile_number(self, mobile_number):
        self.mobile_number = mobile_number
    def get_mobile_number(self):
        return self.mobile_number
    
    def set_picture_large(self, picture_large):
        self.picture_large = picture_large
    def get_picture_large(self):
        return self.picture_large
    
    def set_picture_thumbnail(self, picture_thumbnail):
        self.picture_thumbnail = picture_thumbnail
    def get_picture_thumbnail(self):
        return self.picture_thumbnail
        
    def __str__(self):
        retStr = (f'{self.first_name} {self.last_name} ({self.email})') 
        return retStr

class AuthorizedUsers():
    def __int__(self):
        self.auth_users = []
        
    def add_user(self, users):
        self.auth_users.append(users)
    
    def show_auth_users(self):
        for users in self.auth_users:
            print(users)
        
    # def search_for_users(self, UUID):
    #     for users in self.auth_users:
    #         if(users.get_UUID() == UUID):
    #             return UUID
    #     return None
       

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
        
display_users = AuthorizedUsers()
json_users_data = getData(10, 'us')

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
    new_user = User(first_name, last_name, email, user_name, password, UUID, home_number, mobile_number, picture_large, picture_thumbnail)
    print(new_user)
#     display_users.add_user(new_user)
    
# display_users.show_auth_users()
    