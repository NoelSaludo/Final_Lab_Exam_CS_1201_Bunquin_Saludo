from Models.User import User

class UserManager():
    users = []
    islogined = False
    curent_user = None
    
    def load_users():
        pass
    
    def save_user():
        pass
    
    def validate_username():
        pass
    
    def validate_password():
        pass
    
    def register(self, username, password):
        
       user = list(filter(lambda u: u.username == username, self.users))
       if user:
           print ("Username already used!")
       else:
           print ("Successfully registered!")
           self.users.append(User(username, password))
           
    def log_in(self, username, password):
        user = list(filter(lambda u: u.username == username and u.password == password, self.users))
        if not user:
            print ("Wrong username/password!")
        else:
           self.islogined = True
           self.curent_user = user [0]
           
    def log_out(self):
        self.islogined = False 
        self.curent_user = None
    