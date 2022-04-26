import requests

class Contact:
    def __init__(self, first_name, last_name, email, mobile_number, digital_photo):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile_number = mobile_number
        self.digital_photo = digital_photo
        pass
    
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
    
    def set_mobile_number(self, mobile_number):
        self.mobile_number = mobile_number
    def get_mobile_number(self):
        return self.mobile_number
    
    def set_digital_photo(self, digital_photo):
        self.digital_photo = digital_photo
    def get_digital_photo(self):
        return self.digital_photo
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
           
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
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)

                
        return results
    
   