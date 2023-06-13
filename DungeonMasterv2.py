from Raum import Raum
from Loot import Loot
from Gegner import Gegner
import random

class DungeonMaster:
    def __init__(self):
        self.erstelle_raeume()
        self.aktuellerGegner = None
        self.gold = 0
    
    def erstelle_raeume(self):
        r1 = Raum("Du bist in Raum 1. Es gibt Ausgänge nach Osten und Westen.")
        r2 = Raum("Du bist in Raum 2. Es gibt einen Ausgang nach Westen.")
        r3 = Raum("Du bist in Raum 3. Es gibt einen Ausgang nach Osten.")
        
        self.generiereLoot(r1)
        self.generiereLoot(r2)
        self.generiereLoot(r3)

        self.generieregegner(r2)
        self.generieregegner(r3)

        r1.füge_hinzu_richtung("Osten", r2)
        r1.füge_hinzu_richtung("Westen", r3)
        r2.füge_hinzu_richtung("Westen", r1)
        r3.füge_hinzu_richtung("Osten", r1)
        
        self.aktueller_raum = r1
    
    def generiereLoot(self, raum):
        newLoot = Loot(1000, "Goldtaler")
        raum.addLoot(newLoot)
    
    def generieregegner(self, raum):
        count = random.randint(1,3)
        myEnemyType = ["Dragon", "Skeleton", "Orc"]
        while count > 0:
            describtion = random.choices(myEnemyType, weights = [1, 10, 5], k = 1)            
            print(describtion)
            health = random.randint(10, 100)
            damage = random.randint(1, 20)
            newGegner = Gegner(health, damage, describtion.pop())
            raum.addEnemy(newGegner)
            count = count - 1

    def spiel_loop(self):
        while True:
            
            i = self.aktueller_raum.getEnemyCount()
            if self.aktuellerGegner != None:
                i=i+1

            print(self.aktueller_raum.beschreibung)
            print("Gegner im Raum: " + str(i) )
            print("Gold im Inventar: " + str(self.gold) )
            befehl = input("> ")
            if befehl in ["Osten", "Westen", "Norden", "Süden"]:
                nächster_raum = self.aktueller_raum.geh(befehl)
                if nächster_raum is not None:
                    self.aktueller_raum = nächster_raum
                else:
                    print("Du kannst in diese Richtung nicht gehen.")
            else:
                if befehl in ["loot"]:                                        
                    if self.aktueller_raum.getEnemyCount() <= 0 and self.aktuellerGegner == None:                    
                        myLoot = self.aktueller_raum.getLoot()                         
                        if myLoot != None:
                            print ( myLoot.getDescribtion() )
                            print ( str(myLoot.getLoot()) )
                            self.gold += myLoot.lootValue
                        else:
                            print("Alles leer! :-(")
                    else:                        
                        print (" Es sind noch Gegner da! ")
                      
                else:
                    if befehl in ["Angriff"]:
                        if self.aktuellerGegner == None:
                            if self.aktueller_raum.getEnemyCount() > 0:
                                self.aktuellerGegner = self.aktueller_raum.getEnemy()

                        if  self.aktuellerGegner != None:
                            angriff = random.randint(0, 100)                            
                            self.aktuellerGegner.setHealth(self.aktuellerGegner.getHealth() - angriff)
                            if  self.aktuellerGegner.healthValue < 0:
                                print("Besiegt: " + str(self.aktuellerGegner.getDescribtion()) )
                                self.aktuellerGegner = None
                            else:
                                print("Immer noch: "+ str(self.aktuellerGegner.healthValue) )
                        else:
                            print("Keine Gegner mehr da!")
                            
                    else:
                        if befehl in ["Exit!"]:
                            break
                        else:
                            print("Ungültiger Befehl.")
            


if __name__ == "__main__":
    DungeonMaster().spiel_loop()