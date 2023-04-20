class User:
    count = 0
    
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
        
        User.count += 1

user1 = User("kim", "kim@tum.de", "12345")
user2 = User("park", "park@tum.de", "67890")
user3 = User("leek", "lee@tum.de", "54321")

# class variable counting
#print(User.count)

#User.count = 4

print(user2.count)
print(user1.count)