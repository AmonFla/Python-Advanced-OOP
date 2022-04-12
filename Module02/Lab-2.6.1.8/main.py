import abc
@abc.abstractclass
class AbstractScanner(abc.ABC): 
    
    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class AbstractPrinter(abc.ABC): 

    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MDF(AbstractScanner, AbstractPrinter):

    def __init__(self, sn, scan_reso, print_reso) -> None:
        self.__scan_resolution = scan_reso
        self.__print_resolution = print_reso
        self.__sn = sn
    
    def get_scanner_status(self):
        return self.__scan_resolution, self.__sn
    
    def get_printer_status(self):
        return self.__print_resolution, self.__sn

class MDF1(MDF):
    def __init__(self, sn) -> None:
        super().__init__(sn, 10,10)
    
    def scan_document(self):
        return 'texto'
    
    def print_document(self):
        return 'texto'

class MDF2(MDF):
    def __init__(self, sn) -> None:
        super().__init__(sn, 100,100)
    
    def scan_document(self):
        return 'texto'
    
    def print_document(self):
        return 'texto'

class MDF3(MDF):
    def __init__(self, sn) -> None:
        super().__init__(sn, 1000,1000)
    
    def scan_document(self):
        return 'texto'
    
    def print_document(self):
        return 'texto'

md1 = MDF1('123456')
print(md1.get_printer_status())
print(md1.get_scanner_status())

md2 = MDF2('223456')
print(md2.get_printer_status())
print(md2.get_scanner_status())

md3 = MDF3('323456')
print(md3.get_printer_status())
print(md3.get_scanner_status())


    