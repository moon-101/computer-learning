from random import randint

class Die:
    def __init__(self,num_sides=6):
        """模拟六面的骰子"""
        self.num_sides=num_sides
    
    def roll(self):
        result=randint(1,self.num_sides)
        return result
