from Birds import Bird
    
class SouthAfricanSwallow(Bird):

    def __init__(self,sex,flock_size):
        Bird.__init__(self,sex)
        self.__migratory = "no"
        self.__flock_size = flock_size

    def set_flock_size(self,flock_size):
        self.__flock_size = flock_size

    def get_migratory(self):
        return self.__migratory

    def get_flock_size(self):
        return self.__flock_size
