import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje s nulom nije moguće!"
    
    def potenciranje(self):
        return self.a ** self.b
    
    def korijen(self):
        return math.sqrt(self.a)


calc = Kalkulator(10,4)

print(calc.oduzimanje())