from Birds import Bird
    
class BarnSwallow(Bird):

    #Initialise Barn Swallow, data attributes and obtain Bird inheritance
    def __init__(self, sex,flock_size):
        #Obtain base class data attributes & methods (inheritance)
        Bird.__init__(self,sex)

        #Initialise subclass data attributes
        self.__migratory = "yes"
        self.__flock_size = flock_size

    def set_flock_size(self,flock_size):
        self.__flock_size = flock_size

    def get_migratory(self):
        return self.__migratory

    def get_flock_size(self):
        return self.__flock_size
