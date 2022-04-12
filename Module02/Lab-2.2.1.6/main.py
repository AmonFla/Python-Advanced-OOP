class Scanner:
    def scan(self):
        print('scan scanner')

class Printer:
    def print(self):
        print('print printer')

class Fax:
    def send(self):
        print('send fax') 

    def print(self):
        print('print fax')

class MDF_SPF(Scanner, Printer, Fax):
    pass

class MDF_SFP(Scanner, Fax, Printer):
    pass

spf = MDF_SPF()
spf.print()
spf.scan()
spf.send()

sfp = MDF_SFP()
sfp.print()
sfp.scan()
sfp.send()