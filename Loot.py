
class Loot:

    def __init__(self, value: int, describtion: str):
        self.lootValue = value
        self.lootDescribtion = describtion

    def getLoot(self) -> int:
        return self.lootValue
    
    def getDescribtion(self)-> str:
        return self.lootDescribtion