import math

class krug():
    def __init__(self,radijus):
        self.radijus = radijus
    
    def opseg(self):
        return(2*self.radijus*math.pi)
    
    def povrsina(self):
        return(self.radijus **2 * math.pi)
    
krugic = krug(10)

print(krugic.opseg())         
print(krugic.povrsina()) 