class personal_bio:
    def __init__(self, name, DOB, address, hobbies):
        self.name = name
        self.DOB = DOB
        self.address = address
        self.hobbies = hobbies
        
    def get_name(self):
        return self.name
    
    def get_DOB(self):
        return self.DOB
    
    def get_address(self):
        return self.address
    
    def get_hobbies(self):
        return self.hobbies
        
        
    

person = personal_bio(str(input("Enter your bio information, what is your name?\n")), \
        str(input("What is your Date of Bith in the MM-DD-YYYY format?\n")), str(input("What is your address?\n")), \
        str(input("What are your hobbies?\n")))



print("\nHere is the information you submitted, thank you.\n" + "-NAME: " + person.get_name() + "\n-DOB: "\
    + person.get_DOB() +  "\n-Address: " + person.get_address() + "\n-Hobbies: " + person.get_hobbies() )




