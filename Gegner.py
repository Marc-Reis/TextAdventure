class Gegner:

    def __init__(self, value: int, damage: int, describtion: str):
        self.healthValue = value
        self.enemyDescribtion = describtion
        self.damage = damage 

    def getHealth(self) -> int:
        return self.healthValue
    
    def getDescribtion(self)-> str:
        return self.enemyDescribtion
    
    def getDamage(self)-> int:
        return self.damage
    
    def setHealth(self, value: int):
        self.healthValue = value