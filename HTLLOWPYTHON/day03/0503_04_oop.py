class Animal:
    def __init__(self): # 생성자
        self.fullness = 0 # 전역변수 생성 방법
        
    def eat(self): # 함수 생성방법
        # self.fullness = self.fullness + 1
        self.fullness += 1
    
    def mantang(self):
        # self.fullness = self.fullness + 10
        self.fullness += 10
        
    def a(self):
        # self.fullness = self.fullness - 1
        self.fullness -= 1
        
    def atang(self):
        # self.fullness = self.fullness - 10
        self.fullness -= 10
    
class Human(Animal):
    def __init__(self):
        # pass # 작업할 것이 아무것도 없을 때 pass 작성
        super().__init__() # 상속 받았을 때 부모를 init 단계에서 부모를 호출해야 한다.
        self.flag_cook = False
        self.flag_think = False
    
    def goHakwon(self):
        self.flag_cook = True
        
    def backHakwon(self):
        self.flag_cook = False
    
    def think(self):
        self.flag_think = True
    
    def backThink(self):
        self.flag_think = False
        
        
hum = Human() # new가 없지만 ()로 인하여 객체 생성됨
print(hum.fullness)
hum.eat()
print(hum.fullness)
hum.mantang()
print(hum.fullness)

print()

hum.a()
print(hum.fullness)
hum.atang()
print(hum.fullness)

print()

print(hum.flag_cook)
hum.goHakwon()
print(hum.flag_cook)

print()

print(hum.flag_think)
hum.think()
print(hum.flag_think)
hum.backThink()
print(hum.flag_think)
