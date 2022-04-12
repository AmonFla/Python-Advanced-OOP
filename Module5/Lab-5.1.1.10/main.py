import time

def get_instantiation_time(self):
    return self.instantiation_time

class Meta(type):
    lista = []
    def __new__(mcs, name, bases, dictionary):
       Meta.lista.append(name)
       dictionary['get_instantiation_time'] = get_instantiation_time
       obj = super().__new__(mcs, name, bases, dictionary)
       obj.instantiation_time = time.time()
       return obj
    
class Test1(metaclass=Meta):
    pass

class Test2(metaclass=Meta):
    pass

ob1 = Test1()
ob2 = Test1()
ob3 = Test2()
ob4 = Test1()

print(Meta.lista)
print(ob1.get_instantiation_time())