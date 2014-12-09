class Time(object):
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return "%d:%d:%d" %(self.hours, self.minutes, self.seconds)

    def __cmp__(self,other):
        left_time = self.hours * 1000 + self.minutes * 100 + self.seconds
        right_time = other.hours * 1000 + other.minutes * 100 + other.seconds
        if left_time < right_time:
            return -1
        elif left_time > right_time:
            return 1
        return 0

then = (4 , 12, 32)
now = (7, 32, 54)

print now
print then

print now > then
print now < then
print now == then