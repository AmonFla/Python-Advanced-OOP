import copy

class Delicacy():
    def __init__(self, name, price, weight) -> None:
        self.__name = name
        self.__price = price
        self.weight = weight
    
    def __str__(self) -> str:
        return '{}-{}-{}'.format(self.name, self.price, self.weight)
        
warehouse = list()
warehouse.append(Delicacy( 'Lolly Pop',  0.4,  133))
warehouse.append(Delicacy( 'Licorice',  0.1,  251))
warehouse.append(Delicacy( 'Chocolate',  1,  601))
warehouse.append(Delicacy( 'Sours',  0.01,  513))
warehouse.append(Delicacy( 'Hard candies',  0.3,  433))

copynewlist = copy.copy(warehouse)
deepnewlist = copy.deepcopy(warehouse)

print(warehouse[1] is copynewlist[1])
print(warehouse[1] is deepnewlist[1])