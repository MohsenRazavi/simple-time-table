from random import random


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
        elif self.h < other.h:
            return False

        if self.m > other.m:
            return True
        elif self.m < other.m:
            return False

        if self.s > other.s:
            return True
        elif self.s < other.s:
            return False
        return False

    def __lt__(self, other):
        if self.h < other.h:
            return True
        elif self.h > other.h:
            return False

        if self.m < other.m:
            return True
        elif self.m > other.m:
            return False

        if self.s < other.s:
            return True
        elif self.s > other.s:
            return False
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
        else:
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

    def __repr__(self):
        return f'{self.start} - {self.end} ({self.__len__()})'


class Day:
    busy_times = []
    days = [
        'saturday',
        'sunday',
        'monday',
        'tuesday',
        'wedensday',
        'thursday',
        'friday'
    ]

    def __init__(self, day_name, start_day_time, end_day_time, is_closed):
        if day_name.lower() not in self.days:
            raise Exception('This day does not exists')
        self.day = day_name
        self.start = start_day_time
        self.end = end_day_time
        self.closed = is_closed

    def __str__(self):
        return f'{self.day} plan : {self.busy_times}'

    def check_time(self, **kwargs):
        res = True

        time_period = kwargs['time_period']
        last_time_period_in_day = kwargs['last_time_period_in_day']
        try:
            second_last_time_period_in_day = kwargs['second_last_time_period_in_day']
        except:
            pass
        else:
            if second_last_time_period_in_day.start < time_period.start < second_last_time_period_in_day.end:
                res = False
            if second_last_time_period_in_day.start < time_period.end < second_last_time_period_in_day.end:
                res = False

        if time_period.start < self.start:
            res = False
        if time_period.end > self.end or time_period.start > self.end:
            res = False
        if last_time_period_in_day.end > time_period.start > last_time_period_in_day.start:
            res = False
        if last_time_period_in_day.end > time_period.end > last_time_period_in_day.start:
            res = False
        print(res)
        return res

    def add(self, time_period):
        if self.closed:
            print('This day is shutdown')
        else:
            try:
                last_time_period_in_day = self.busy_times[-1]
                # try:
                #     second_last_time_period_in_day = self.busy_times[-2]
                # except:
                #     pass
            except:
                if not(time_period.start < self.start):
                    if not(time_period.end > self.end or time_period.start > self.end):
                        self.busy_times.append(time_period)
                    else:
                        print(f'This time is busy ({time_period})')
                else:
                    print(f'This time is busy ({time_period})')
                        
            else:
                if self.check_time(time_period=time_period, last_time_period_in_day=last_time_period_in_day,):
                    self.busy_times.append(time_period)
                else:
                    print(f'This time is busy ({time_period})')
    
    def cancel(self, time_period):
        if time_period in self.busy_times:
            self.busy_times.remove(time_period)
        else:
            print('this period is free')


a = Day('saturday', Time(7, 0, 0), Time(12, 0, 0), False)

b = TimePeriod(Time(9,0,0), Time(9,30,0))
# a.add(TimePeriod(Time(1, 0, 0), Time(2, 30, 0)))
a.add(b)
# a.add(TimePeriod(Time(13,0,0), Time(13,30,0)))

print(a.busy_times)

a.cancel(b)

print(a.busy_times)