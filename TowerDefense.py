"""
Todd Bajzek,
William Morris,
Owen Schuldt
"""


class Board:
    def __init__(self, towerCount, monsterCount):
        self.towerCount = towerCount
        self.monsterCount = monsterCount
    
    def play(self):
        self.passedMonsterHealth = 0
        
        self.towerGameList = []
        towerNumber=int(input("Please input the amount of towers to create "))
        towerValList=[]
        for i in range(towerNumber):
            towerVal= input("input the " + str(i+1) +"st tower's values ")
            towerVal=towerVal.split()
            towerValList.append(towerVal)
        for i in range(len(towerValList)):
            for j in range(len(towerValList[i])):
                towerValList[i][j]=int(towerValList[i][j])
        
        currentPosition = 1
        for lst in towerValList:
            self.towerGameList.append(Tower(currentPosition,lst[0],lst[1]))
            currentPosition += 1
        
        self.monsterGameList = []
        monsterNumber=int(input("Please input the amount of monsters to create "))
        monsterValList=[]
        for i in range(monsterNumber):
            monsterVal= input("input the " + str(i+1) +"st monster's values ")
            monsterVal=monsterVal.split()
            monsterValList.append(monsterVal)
        for i in range(len(monsterValList)):
            for j in range(len(monsterValList[i])):
                monsterValList[i][j]=int(monsterValList[i][j])
        
        for lst in monsterValList:
            self.monsterGameList.append(Monster(1 - lst[0],lst[1]))
            
        while len(self.monsterGameList) > 0:
            for tower in self.towerGameList:
                for monster in self.monsterGameList:
                    if monster.getPosition() == tower.getPosition():
                        tower.attack(monster)
                    
            for monster in self.monsterGameList:
                if monster.getHealth() <= 0:
                    self.monsterGameList.remove(monster)
                else:
                    monster.move()
                    if monster.getPosition() > towerNumber:
                        self.passedMonsterHealth += monster.getHealth()
                        self.monsterGameList.remove(monster)       
            
            for tower in self.towerGameList:
                tower.regenerate()
                
        print(self.passedMonsterHealth)
        
            
                    
                
        
            
                
        

        
        
    def getTowerCount(self):
        return self.towerCount
    
    def getTimeCount(self):
        return self.timeCount
    

class Monster():
    def __init__(self, position, health):
        self._health = health
        self._position = position
    
    def move(self):
        self._position += 1
    
    def getPosition(self):
        return self._position
    
    def damage(self, damage):
        self._health -= damage
    
    def getHealth(self):
    	return self._health

class Tower():
    
    def __init__(self, position, capacity, regen):
        self._position = position
        self._maxCapacity = capacity
        self._currentCapacity = capacity
        self._regen = regen
    
    def getPosition(self):
        return self._position
   	 
    def regenerate(self):
        if self._currentCapacity < self._maxCapacity:
            self._currentCapacity += self._regen
   	 
        if self._currentCapacity > self._maxCapacity:
            self._currentCapacity = self._maxCapacity
    
    def attack(self, monster):
    	damage = min(monster.getHealth(), self._currentCapacity)
    	monster.damage(damage)
    	self.loseCapacity(damage)
   	 
    def loseCapacity(self, damage):
    	self._currentCapacity -= damage
    

    

game = Board(5,2)

game.play()
    
    
    
    

    
    
        
