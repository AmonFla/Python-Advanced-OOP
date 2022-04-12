class MobilePhone:
    def __init__(self,number):
        self.number = number
    
    def turn_on(self):
        return "Mobile phone {} is turned on".format(self.number)
    
    def turn_off(self):
        return "Mobile phone is turned off"
    
    def call(self, number):
        return "Calling {}".format(number)


def main():
    phone1 = MobilePhone('01632-960004')
    phone2 = MobilePhone('01632-960012')

    print(phone1.turn_on())
    print(phone2.turn_on())
    print(phone1.call('555-34343'))
    print(phone1.turn_off())
    print(phone2.turn_off())

main()

