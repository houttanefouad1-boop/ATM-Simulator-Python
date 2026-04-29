class car:
    def __init__(self, color, price, model):
        self.carColor = color 
        self.carPrice = price
        self.carModel = model 
    def mycar (self):
        
        if self.carModel >= 2018:
            self.carPrice += 1000
            print(f"my new price {self.carPrice}")
        else :
            self.carPrice -= 1000
            print(f"my new price {self.carPrice}")       
BMW =car("red ", 2000, 2019)
FORD =car("black", 3500, 2020)
DACIA =car("dragon", 2500, 2013)


BMW.mycar() 
FORD.mycar()
DACIA.mycar()
############################################HELLO WORLD ###########################################

#_____________________________              HOW ARE YOU                   ________________________#
                             #____________________________________________#

