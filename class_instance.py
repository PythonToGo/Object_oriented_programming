class User:
    count = 0
    def __init__(self, name, email, password):  # setting all variables of user instance
        self.name = name
        self.email = email
        self.password = password
        
        User.count += 1
    
    def say_hello( self):
        print("Hi, I am {}".format(self.name))
    
    def __str__(self) -> str:
        ## __str__ : dunder method
        return "user: {} email: {}, password: {}".format(self.name, self.email, self.password)

    @classmethod
    # class method -> first parameter is cls!!
    def number_of_users(cls):
        print("all users are: {}".format(cls.count))

#    instant variable이 사용되지 않을때는 class method로만 표기하기.
#    def number_of_users(self):
#        print("all users are: {}".format(User.count))
    
    
user1 = User("kim", "kim@tum.de", "12345")
user2 = User("park", "park@tum.de", "67890")
user3 = User("leek", "lee@tum.de", "54321")

User.number_of_users()


 