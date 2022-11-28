class Cookie :
    def __init__(self, name, shape, chips = 'Chocolate'):
      self.name = name
      self.shape = shape
      self.chips = chips
    
    def bake(self):
        print(f'This {self.name}, is being baked with the shape {self.shape} and chips of {self.chips}')
        print("Enjoy your cookie!")
              
cookie2 = Cookie('Black', 'Rond')
cookie2.bake()


	  