import requests

class Contact:
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
        return f"{self.first_name} {self.last_name} {self.email} {self.picture_large}"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.picture_large}"
           
class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.get_first_name().lower().startswith(searchStr.lower()) or address.get_last_name().lower().startswith(searchStr.lower()):
                results.append(address)

                
        return results
    
