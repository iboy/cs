class Product:
    description = "new product"
    price = 1.00
    inventory = 10
    
	def set_description(self, desc):
        self.__description = desc
        
    def get_description(self):
        return self.__description
    def set_price(self, price):
        
    def get_price(self):
        return self.__price
        
    def set_inventory(self, inventory):
        self.__inventory = inventory
        
    def get_inventory(self):
        return self.__inventory