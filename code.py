class Time:
    def __init__(self, hours, minutes, seconds):
        if hours < 0 or hours > 23:
            raise ValueError("A hour must be a postive integer less than 24")
        if minutes < 0 or minutes > 60:
            raise ValueError("A minute must be a postive integer less than 60")
        if seconds < 0 or seconds > 60:
            raise ValueError("A second must be a postive integer less than 60")
        
        self.h = hours
        self.m = minutes
        self.s = seconds

    def __str__(self):
        return f'{self.h:02d}:{self.m:02d}:{self.s:02d}'
    
    def __repr__(self):
        # returns seconds
        return self.h*3600+self.m*60+self.s

    def __gt__(self, other):
        if self.h > other.h:
            return True
        if self.m > other.m:
            return True
        if self.s > self.s:
            return True``
        return False


    def __lt__(self, other):
        if self.h < other.h:
            return True
        if self.m < other.m:
            return True
        if self.s < self.s:
            return True
        return False

