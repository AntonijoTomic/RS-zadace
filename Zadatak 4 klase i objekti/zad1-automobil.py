import datetime
class automobil():
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model= model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
    
    def ispis(self):
        print(f"{self.marka} - model: {self.model} proizveden {self.godina_proizvodnje} ima {self.kilometraza}km")
    
    def starost(self):
        return f"Automobil je star {datetime.datetime.now().year - self.godina_proizvodnje}g" 
        
auto = automobil("Audi","A4", 2020, 120000)

auto.ispis()        
print(auto.starost())

        