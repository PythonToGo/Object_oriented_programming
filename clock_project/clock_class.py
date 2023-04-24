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
    

class Clock:    #class clock
    HOURS = 24      # hours limit
    MINUTES = 60     # minutes limit
    SECONDS = 60    # second limit

    def __init__(self, hour, minute, second):
        """
        define Counter instance representing hours, minutes, seconds
        define current time(self.set) as parameters(hour,minute,second)
        """
        
        self.hour = Counter(Clock.HOURS)
        self.minute = Counter(Clock.MINUTES)
        self.second = Counter(Clock.SECONDS)
        
        self.set(hour, minute, second)  #current time


    def set(self, hour, minute, second):
        # set self.set as parameter hour, minute, seconds
        
        self.hour.set(hour)
        self.minute.set(minute)
        self.second.set(second)


    def tick(self):

        if self.second.tick():
            if self.minute.tick():
                self.hour.tick()
        

    def __str__(self):

        return "Now is {}:{}:{}".format(self.hour, self.minute, self.second)
        
        

# check seconds over 60 exceeds
print("set the time 10:32:39")
clock = Clock(10, 32, 39)
print(clock)

# passed 26 seconds
print("passed 26 seconds")
for i in range(26):
    clock.tick()
print(clock)

# check minutes over 60 exceeds
print("set the time 10:59:59")
clock.set(10, 59, 59)
print(clock)

# passed 10 seconds
print("passed 10 seconds")
for i in range(10):
    clock.tick()
print(clock)

# check time if 23:59:59 to 00:00:00
print("set the time 23:59:59")
clock.set(23, 59, 59)
print(clock)

# passed 3 seconds
print("passed 3 seconds")
for i in range(3):
    clock.tick()
print(clock)