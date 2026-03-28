class Enemy:
    def __init__(self,nome,hp,danno,):
        self.enemy_nome=nome
        self.enemy_hp=hp
        self.enemy_danno=danno
        


class arduino(Enemy):

    def __init__(self):
        super().__init__(nome="arduino",hp=30,danno=20)
    
    def attacco1(self):
        print(f"{self.enemy_nome} scaglia led_abbagliante")
        return self.enemy_danno

class sigmaboy(Enemy):

    def __init__(self):
        super().__init__(nome="er sigma",hp=50,danno=35,move="ululato_raccapriciante")




    
