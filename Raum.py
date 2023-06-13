from Loot import Loot
from Gegner import Gegner

class Raum:
    def __init__(self, beschreibung):
        self.beschreibung = beschreibung
        self.richtungen = {}
        self.lootList = [] #neu
        self.enemyList = [] #neu

    def geh(self, richtung):
        if richtung in self.richtungen:
            return self.richtungen[richtung]
        else:
            return None

    def füge_hinzu_richtung(self, richtung, raum):
        self.richtungen[richtung] = raum

    def addLoot(self, loot): #neu
        self.lootList.append(loot)
    
    def getLoot(self) -> Loot:      # neu
        if len(self.lootList) > 0:
            return self.lootList.pop()
        else:
            return None
        
    def addEnemy(self, enemy): #neu
        self.enemyList.append(enemy)
    
    def getEnemy(self) -> Gegner:      # neu
        if len(self.enemyList) > 0:
            return self.enemyList.pop()
        else:
            return None
        
    def getEnemyCount(self) -> int:# neu
        return len(self.enemyList)