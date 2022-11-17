class Bird:
    #Initialise Bird class data attributes
    def __init__(self, sex):
        self.__feathers = "yes"
        self.__bones = "hollow"
        self.__eggs = "hard-shell"
        self.__sex = sex

    def set_sex(self,sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    def get_feathers(self):
        return self.__feathers

    def get_bones(self):
        return self.__bones

    def get_eggs(self):
        return self.__eggs
