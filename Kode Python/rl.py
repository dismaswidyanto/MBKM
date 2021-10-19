import pygame
import random 
#from Q_Learning import Q_Learning
rdm = 0
reward = 0

#initialize pygame
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
pygame.init()
demon=8

#background
bgnd = pygame.image.load('background2.png')

#create the screen
screen = pygame.display.set_mode((600, 600))

#load asset
#Title and Icon
pygame.display.set_caption("Reinforcement Learning")

#player
agenIcon = pygame.image.load('walk.png')

demonIcon = pygame.image.load('demon.png')
demonX = [0]
demonY = [0]
goldIcon = pygame.image.load('ingots.png')


#generate demon table
demon_table = [[0 for i in range(5)] for j in range(5)]

#input start and goal
start = int(input("Masukkan posisi start: "))
goal = int(input("Masukkan posisi goal: "))

#mark start and goal position
demon_table[(start-1)//5][(start-1)%5] = "S"
agenPos = [((start-1)%5) *120, ((start-1)//5) *120]
demon_table[(goal-1)//5][(goal-1)%5] = "G"
goldPos = [((goal-1)%5) *120, ((goal-1)//5)*120]

#mark demon position
i=0
while (i<demon):
	pos = random.randint(1,25)
	if((demon_table[(pos-1)//5][(pos-1)%5]!=1) and not((pos==start) or (pos==goal))):
		demon_table[(pos-1)//5][(pos-1)%5]=1
		if(i==0):
			demonX=[((pos-1)%5) *120]
			demonY=[((pos-1)//5) *120]
		else:
			demonX.append( ((pos-1)%5) *120)
			demonY.append( ((pos-1)//5) *120)
		i+=1

#print demon table
print("Demon Table: ")
print(demonX)
print(demonY)
for i in range (5):
	print(demon_table[i])

def isCollision(x, y):
    if (x==120):
        if (y==120 or y==360 or y==480):
            return True
        else:
            return False
    elif (x==240):
        if (y==120):
            return True
        else:
            return False
    elif (x==360):
        if (y==240 or y==360):
            return True
        else:
            return False
    elif (x==480):
        if (y==0 or y==360):
            return True
        else:
            return False
    elif (x<0 or x>480 or y<0 or y>480):
        return True
    else:
        return False
def isGoal():
    if(agenPos[0]==480 and agenPos[1]==480):
        return True
    else:
        return False


#Game loop
running = True
while running:
	#clear screen
    screen.fill(WHITE)
    
    #draw object
    screen.blit(agenIcon, agenPos)
    screen.blit(demonIcon,(demonX[0],demonY[0]))
    screen.blit(demonIcon,(demonX[1],demonY[1]))
    screen.blit(demonIcon,(demonX[2],demonY[2]))
    screen.blit(demonIcon,(demonX[3],demonY[3]))
    screen.blit(demonIcon,(demonX[4],demonY[4]))
    screen.blit(demonIcon,(demonX[5],demonY[5]))
    screen.blit(demonIcon,(demonX[6],demonY[6]))
    screen.blit(demonIcon,(demonX[7],demonY[7]))
    screen.blit(goldIcon, goldPos)
    screen.blit(bgnd, (0, 0))
    
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                agenPos[1] += 120
            if event.key == pygame.K_UP:
                agenPos[1] -= 120
            if event.key == pygame.K_LEFT:
                agenPos[0] -= 120
            if event.key == pygame.K_RIGHT:
                agenPos[0] += 120

    collision = isCollision(agenPos[0], agenPos[1])
    if collision:
        agenPos[0]=0
        agenPos[1]=0
        reward -= 1
        print("reward = ")
        print(reward)
    goal = isGoal()
    if goal:
        agenPos[0]=0
        agenPos[1]=0
        reward += 1
        print("reward = ")
        print(reward)

    
    pygame.display.update()
