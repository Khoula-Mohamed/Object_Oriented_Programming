class Person:
    # conststructor to creat object
    # initialize instance variables
    def __init__(self,name, p_age=20):
        self.name = name
        self.age = p_age
    #use term of encapsueltion
        #accessor methods
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    #setter methoeds
    def set_name(self,newName):
        self.name = newName
    def set_age(self,newAge):
        self.age = newAge
    
    def run(self):
        print(self.name , "is running")
    def descrip(self):
        return f'Person name {self.name} is {self.age} years old'
    
    def say_hi(self):
        return f"Hi as {self.name} as person"
    
    
