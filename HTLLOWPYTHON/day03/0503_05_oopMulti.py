class JindoDog:
    def __init__(self):
        self.power_bark = 0
        
    def train(self):
        self.power_bark += 1
        
class SokchoBird():
    def __init__(self):
        self.flag_fly = False
    
    def practice(self):
        self.flag_fly = True

class GaeSae(JindoDog,SokchoBird):
    def __init__(self):
        JindoDog.__init__(self)
        SokchoBird.__init__(self)
        self.barkFly = False
    
    def trainPractice(self):
        self.barkFly = True
        
gs = GaeSae()
print(gs.power_bark)
print(gs.flag_fly)
gs.train()
gs.practice()
print(gs.power_bark) 
print(gs.flag_fly)

print()

print(gs.barkFly)
gs.trainPractice()
print(gs.barkFly)
        