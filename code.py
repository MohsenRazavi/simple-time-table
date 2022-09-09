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
            return True
        return False


    def __lt__(self, other):
        if self.h < other.h:
            return True
        if self.m < other.m:
            return True
        if self.s < self.s:
            return True
        return False

    def __sub__(self, other):

        if self > other:
            s = self.s - other.s
            if s < 0:
                s += 60
                self.m -= 1
            m = self.m - other.m
            if m < 0:
                m += 60
                self.h -= 1
            h = self.h - other.h
        else :
            s = other.s - self.s
            if s < 0:
                s += 60
                other.m -= 1
            m = other.m - self.m
            if m < 0:
                m += 60
                other.h -= 1
            h = other.h - self.h

        return Time(h, m, s)


class TimePeriod:

    def __init__(self, start_time, end_time):
        if end_time < start_time or start_time > end_time:
            raise ValueError('Invalid times')
        self.start = start_time
        self.end = end_time

    def __len__(self):
        return self.end - self.start

    def __str__(self):
        return f'{self.start} - {self.end} ({self.__len__()})'



