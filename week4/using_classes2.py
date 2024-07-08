class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        """ # ^-- Aside from the parameter self which is handled by Python, the arguments for the other parameters name, email, and password must be passed in when the User class is used to instantiate an object."""
    
    def change_password(self, password):
        self.password = password
        print("Your old password has been changed to", self.password)

        """"" ^--This instance method will be avaliable to be used by all objects instantiated from this class
        Like instance attributes, the method can be altered for a single object without affecting other objects
        of the same class.
        
        The first parameter of an instance method is self by default. As with the __init__ constructor method,
        Python handles passing in the argument for this parameter, and will always cause it to reference the relevant object.
        You can use the self argument without needing to do anything to set it yourself
         
          The second parameter is a new password
           Inside the method, we set the self.password attribute to the new password, then print a confirmation showing the current (changed) self.password. :) """
        
user1 = User("jane", "jane@nucamp.co","janespassword")
print(user1.password)
user1.change_password("bestpassword")
