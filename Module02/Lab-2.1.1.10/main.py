

class TimeInterval:
    def __init__(self, hours = 0,minutes = 0,seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __toSeconds(self,obj):
        return obj.hours * 3600 + obj.minutes * 60 + obj.seconds

    def __toHourFormat(self, seconds):
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return '{}:{}:{}'.format(hours,minutes,seconds)
        
    def __add__(self,other):
        if not isinstance(other,TimeInterval):
            raise TypeError()
        return self.__toHourFormat(self.__toSeconds(self)+self.__toSeconds(other))

    def __sub__(self,other):
        if not isinstance(other,TimeInterval):
            raise TypeError()
        return self.__toHourFormat(self.__toSeconds(self)-self.__toSeconds(other))
    
    def __mul__(self,intval):
        if not isinstance(intval,int):
            raise TypeError()
        return self.__toHourFormat(self.__toSeconds(self)*intval)

    def __str__(self):
        return self.__toHourFormat(self.__toSeconds(self))

int1 = TimeInterval(hours=21, minutes=58, seconds=50)
int2 = TimeInterval(hours=1, minutes=45, seconds=22)

print(int1+int2)
print(int1-int2)
print(int1*2)
print(int1)
assert(str(int1) == "21:58:50")