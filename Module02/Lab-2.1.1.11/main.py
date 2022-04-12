from importlib.util import set_loader


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
        if isinstance(other,TimeInterval):
            return self.__toHourFormat(self.__toSeconds(self)+self.__toSeconds(other))
        elif isinstance(other, int):
            return self.__toHourFormat(self.__toSeconds(self)+other)
        else:
            raise TypeError() 

    def __sub__(self,other):
        if isinstance(other,TimeInterval):
            return self.__toHourFormat(self.__toSeconds(self)-self.__toSeconds(other))
        elif isinstance(other, int):
            return self.__toHourFormat(self.__toSeconds(self)-other)
        else:
            raise TypeError() 
        
    
    def __mul__(self,intval):
        if not isinstance(intval,int):
            raise TypeError()
        return self.__toHourFormat(self.__toSeconds(self)*intval)

    def __str__(self):
        return self.__toHourFormat(self.__toSeconds(self))

int1 = TimeInterval(hours=21, minutes=58, seconds=50)

print(int1+62)
print(int1-62)