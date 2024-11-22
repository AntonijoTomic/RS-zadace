class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    
    def work(self):
        print(f"Radim na poziciji {self.pozicija}")


class Manager(Radnik):
    def __init__(self, ime, pozicija, placa,department):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
        super().__init__(ime, pozicija, placa)
        self.department = department 
    
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
        
    def give_raise(self, iznos):
        self.placa = self.placa + iznos
        print(f"Moja placa s povisicom je {self.placa}")
        

radnik1= Radnik("Antonijo","Programer",1000)
manager1 = Manager("Anita", "Manager",4000, "IT")

radnik1.work()
manager1.work()
manager1.give_raise(200)