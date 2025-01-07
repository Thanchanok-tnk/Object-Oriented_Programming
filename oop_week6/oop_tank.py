class Tank:
    def __init__(self,ชื่อ,กระสูน,พลังชีวิต):
        self.name =  ชื่อ
        self.ammo =  กระสูน
        self.hp =  พลังชีวิต
    def add_ammo(self,กระสูน):
        if self.ammo >= 10:
            print('กระสูนยังเต็มอยู่')
        else :
            self.ammo+=กระสูน
            print("รีโหลด")
    def fire_ammo(felf,enemy):
        felf.ammo -=1
        enemy.hp -=1

Tank1 = Tank("A1",10,5)
Tank2 = Tank("A2",7,5)
Tank3 = Tank("A3",9,5)
Tank2.fire_ammo(Tank3)
print(Tank2.ammo)
print(Tank3.hp)