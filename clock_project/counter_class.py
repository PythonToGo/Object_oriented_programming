class Counter:
    # class, will be used to represent the hours, minutes, seconds of the clock

    def __init__(self, limit):
        """
        set instance variable: limit as a parameter,
        set instance variable: value as 0 ,initial value.
        """
        self.limit = limit
        self.value = 0 


    def set(self, new_value):
        """
        set new_value = value if 0 <= new_value <= limit
        else: new_value = 0 
        """
        self.value = new_value if 0 <=  new_value < self.limit else 0


    def tick(self):
        """
        increase value by +1
        if: value reaches limit, value become 0, return True.
        else: return False
        """
        self.value += 1
        if self.value == self.limit:
            self.value = 0
            return True
        else:
            return False


    def __str__(self):
        """
        return value as a str
        transfer value as str and call zfill method
        """
        return str(self.value).zfill(2)
    
    
# create a counter instance that can count up to 30
counter = Counter(30)


# TEST


# count from 0 to 13
print("count from 0 to 13")
for i in range(13):
    counter.tick()
    print(counter)

# Set the count value as 0
print("Set the count value as 0")
counter.set(0)
print(counter)


# set count value as 42
print("set count value as 42")
counter.set(27)
print(counter)

# if count value become 30, will be changed to 0?
print("Counter value becomes 0 if it reaches to 30")
for i in range(5):
    counter.tick()
    print(counter)       