import time
def printTimestamp(function):
    def internal_wrapper(*args):
        print(time.strftime("%Y-%m-%d %H:%M:%S"))
        function(*args)
    return internal_wrapper

@printTimestamp
def add(a,b):
    print(a+b)


add(1,2)