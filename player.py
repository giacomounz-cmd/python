
def nome_player():
    name=str(input("dammi il nome del tuo player"))
    return name


def race():
    razze={
        "1":(f"elfo hp iniziali : 80 buff armi: +5 mana:+15 abilità "),
        "2":"negromante hp iniziali:60 buff armi +2 mana+20 abilità " 
    }
    for key,value in razze.items():
        print(f"{key} {value}")
    scelta=input()
    
    match scelta:
        case "1":
            elfo={
                "hp":80,
                "buff-armi":5,
                "mana":15,
                "abilita":[
                    {"nome":"linfa_vitale","uso_mana":13,"cura":30},
                    {"nome":"freccia_destiny","uso_mana":20,"danno":50},
                    {"nome":"carica_arzilla","uso_mana":20,"buff_armi":15}
                ]
            }
            return elfo
        
        case "2":
            negromante={
                "hp":60,
                "buff-armi":2,
                "mana":20,
                "abilita":[
                    {"nome":"succhia_anime","uso_mana":20,"cura":30},
                    {"nome":"esplosione_del_caos","uso_mana":10,"danno":30},
                    {"nome":"rinforzi_dell'ade","uso_mana":5,"buff_armi":25}
                ]
            }
            return negromante
        case _:
            print("inserito numero non valido ")
            return race()
        
          
            

 
class Player:

    def __init__(self):

        self.nome=nome_player()
        self.razza=race()
        self.stats_player={
        "hp":self.razza["hp"],
        "buff-armi":self.razza["buff-armi"],
        "mana":self.razza["mana"],
        "abilita":self.razza["abilita"]
        }
    def danno(self,quantità_danno):
        self.stats_player["hp"] -=quantità_danno
    
    def cura(self,quantità_cura):
        self.stats_player["hp"] +=quantità_cura
    

    
player=Player()
#print(player.stats_player) #per stampare le atatistiche
print(player.stats_player["abilita"][0]["cura"])#per accedere ad ogni buff dell'abilità
#print(player.stats_player)


    
    
    
        
    


