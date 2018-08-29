""" Abstract Ant factory """


class BaseAnt(object):
    """
    This is a base class for all ant that we have
    """
    def __init__(self):
        self.species = 'Ant'
        self.taxonomic_class = 'Insect'
        self.role = 'not assigned'
        self.hp = 150

    def show_role(self):
        print("My role is to be a %s" % self.role)


class Queen(BaseAnt):
    def __init__(self):
        super().__init__()
        self.role = 'Queen'
        self.hp += 1400


class Worker(BaseAnt):
    def __init__(self):
        super().__init__()
        self.role = 'Worker'


class Soldier(BaseAnt):
    def __init__(self):
        super().__init__()
        self.role = 'Soldier'
        self.hp += 400


class Drone(BaseAnt):
    """
    Ant: male reproductive
    """
    def __init__(self):
        super().__init__()
        self.role = 'Drone'
        self.hp -= 50


class Alate(BaseAnt):
    """
    Ant: winged reproductive [male or female]
    """
    def __init__(self, sex):
        super().__init__()
        self.role = 'Alate'
        self.sex = sex
        self.hp += 50

    def is_male(self):
        self.sex == 'Male'

# Create an Ant factory
class AntFactory(object):

    @staticmethod
    def new_ant(ant_type):
        if ant_type == 'Queen':
            return Queen()
        elif ant_type == 'Worker':
            return Worker()
        elif ant_type == 'Soldier':
            return Soldier()
        elif ant_type == 'Drone':
            return Drone()
        elif ant_type == 'Alate':
            return Alate('Female')
        else:
            print("Ant type does not exist.")


ANT_TYPES = ['Queen', 'Worker', 'Soldier', 'Drone', 'Alate']

ANT_OBJS = [AntFactory().new_ant(ant) for ant in ANT_TYPES]

import pdb;pdb.set_trace()
for each_object in ANT_OBJS:
    print(each_object.show_role())