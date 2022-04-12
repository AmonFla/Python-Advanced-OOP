class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    try:
        print('Battery Charged {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with batteries') from e

def circuits_check(): 
    try:
        assert(circuits == True)
        print('Circuits On')
    except AssertionError as e:
        raise RocketNotReadyError('Cictuis ') from e



crew = ['John', 'Mary', 'Mike']
fuel = 100
battery = 100
circuits = False
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
