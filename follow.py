class User:
    # setting instance variable
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.following_list = []    # user follows another
        self.followers_list = []    # someone follows user

    # follow
    def follow(self, another_user):
        if self.name not in another_user.followers_list:
            self.following_list.append(self)
            another_user.followers_list.append(self)


    # return how many people i follow
    def num_following(self):
        i = 0
        while i < len(self.following_list):
            i += 1
        
        return i
        

    # return how many people follows me
    def num_followers(self):
        j = 0
        while j < len(self.followers_list):
            j += 1
        return j


# creating user
user1 = User("Kim", "kim@follow.py", "67890")
user2 = User("Leeo", "lee@follow.py", "12345")
user3 = User("Park", "park@follow.py", "09876")
user4 = User("Choi", "choi@follow.py", "54321")

# follow state
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

# User name, number of followers, number of following
print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())
