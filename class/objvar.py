class Robot():
    """meetting robots."""
    #variable of class, numbers of robots
    population = 0
    def __init__(self, name):
        '''Inicialization'''
        self.name = name
        print('(Inicialization {0})'.format(self.name))

        #+1 to population
        Robot.population += 1

    def __del__(self):
        '''I am die'''
        print('{0} destroid'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} were last'.format(self.name))
        else:
            print('{0:d} robots works'.format(Robot.population))

    def sayHi(self):
        '''hello by robot'''

        print('hi! my people say me {0}'.format(self.name))

    def howMany():
        '''sum robots'''
        print('we have {0:d} robots'.format(Robot.population))

    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print('_'*40)

print('Robots fucked people in the ass!|')

print('-'*40)

print('go to kill robots')
del droid1
del droid2

Robot.howMany()
print('we save your ass')
