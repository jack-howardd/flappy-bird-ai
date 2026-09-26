import pygame
import random
import numpy as np
pygame.init()
x=0
y=0
v=0
pipesx=[]
pipesy=[]
score=0
instnum=-1
players=[]
#inputs=[(pipesx[0]-x)/500,(pipesx[1]-x)/500,(pipesy[0]-y)/500,(pipesy[1]-y)/500,v/20]
bestweights1=[[random.uniform(-1,1) for _ in range(5)] for _ in range(10)]
bestbiases1=[random.uniform(-1,1) for _ in range(10)]
bestweights2=[[random.uniform(-1,1) for _ in range(10)] for _ in range(10)]
bestbiases2=[random.uniform(-1,1) for _ in range(10)]
bestweightsout=[random.uniform(-1,1) for _ in range(10)]
bestbiasout=random.uniform(-1,1)
values=[]
max_value=0

displaynum=50

open('mean.txt', 'w').close()
open('max.txt', 'w').close()
for _ in range(50):
    players.append([[[random.uniform(-1, 1) for _ in range(5)] for _ in range(10)],
                     [random.uniform(-1, 1) for _ in range(10)],
                     [[random.uniform(-1, 1) for _ in range(10)] for _ in range(10)],
                     [random.uniform(-1, 1) for _ in range(10)],
                     [random.uniform(-1, 1) for _ in range(10)],
                     random.uniform(-1, 1),0])

def instance():
    global x,y,v,pipesx,pipesy,score,instnum,bestweights1,bestbiases1,bestweights2,bestbiases2,bestweightsout,bestbiasout,players,values,displaynum,max_value
    instnum+=1
    if instnum%displaynum==0:
        screen=pygame.display.set_mode((1000,600))
        pygame.display.set_caption('neural network')
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)
        clock=pygame.time.Clock()
    x=100
    y=300
    v=0
    pipesx=[1000,1500,2000,2500]
    pipesy=[random.randint(110,490) for _ in range(4)]
    score = 0
    # if instnum%50==0 and instnum!=0:
    #     players = sorted(players,key=lambda player: player[-1])
    #     bestweights1,bestbiases1,bestweights2,bestbiases2,bestweightsout,bestbiasout = players[-1][:-1]
    #     for n in range(0,45):
#             players[n]=[[[(int(random.randint(1, 5) < 5) * random.random() * 0.1 - 0.05) + j for j in i] for i in bestweights1],
#                 [(int(random.randint(1, 5) < 5) * random.random() * 0.1 - 0.05) + i for i in bestbiases1],
#                 [[(int(random.randint(1, 5) < 5) * random.random() * 0.1 - 0.05) + j for j in i] for i in bestweights2],
#                 [(int(random.randint(1, 5) < 5) * random.random() * 0.1 - 0.05) + i for i in bestbiases2],
#                 [(int(random.randint(1, 5) < 5) * random.random() * 0.1 - 0.05) + i for i in bestweightsout],
#                 (int(random.randint(1, 5) < 5) * random.random() * 0.1 - 0.05) + bestbiasout,0]
    if instnum%50==0 and instnum!=0:
        # print([players[g][-1] for g in range(len(players))])
        players = sorted(players,key=lambda player: player[-1])
        options=[]
        for a in range(len(players)-5,len(players)):
            for _ in range(players[a][-1]):
                options.append(a)
        # print('\n scores:')
        # print([players[g][-1] for g in range(len(players))])
        # print('ave: ')
        # print(np.mean([players[g][-1] for g in range(len(players))]))
        with open("max.txt") as f:
            try:
                max_value = max(int(line.strip()) for line in f if line.strip())
            except:
                max_value=0
        if players[-1][-1] > max_value:
            bestweights1, bestbiases1, bestweights2, bestbiases2, bestweightsout, bestbiasout = players[-1][:-1]
            print('\n scores:')
            print([players[g][-1] for g in range(len(players))])
            print(players[-1][:-1])
        with open('mean.txt', 'a') as file:
            file.write(f'{np.mean([players[g][-1] for g in range(len(players))])}\n')
        with open('max.txt', 'a') as file:
            file.write(f'{players[-1][-1]}\n')
        # print('\n')
        for h in range(len(players)):
            players[h][-1] = 0
        for n in range(0,46):
            choice=random.choice(options)
            players[n]=[[[(int(random.randint(-2, 5) < 5)) * random.uniform(-0.999 ** max_value, 0.999 ** max_value) + j for j in i] for i in players[choice][0]],
                [(int(random.randint(-2, 5) < 5)) * random.uniform(-0.999 ** max_value, 0.999 ** max_value) + i for i in players[choice][1]],
                [[(int(random.randint(-2, 5) < 5)) * random.uniform(-0.999 ** max_value, 0.999 ** max_value) + j for j in i] for i in players[choice][2]],
                [(int(random.randint(-2, 5) < 5)) * random.uniform(-0.999 ** max_value, 0.999 ** max_value) + i for i in players[choice][3]],
                [(int(random.randint(-2, 5) < 5)) * random.uniform(-0.999 ** max_value, 0.999 ** max_value) + i for i in players[choice][4]],
                (int(random.randint(-2, 5) < 5)) * random.uniform(-0.999 ** max_value, 0.999 ** max_value) + players[choice][5],0]
        # players[-1]=[bestweights1,bestbiases1,bestweights2,bestbiases2,bestweightsout,bestbiasout,0]
        # print(len(options))
    weights1 = players[instnum%50][0]
    biases1 = players[instnum%50][1]
    weights2 = players[instnum%50][2]
    biases2 = players[instnum%50][3]
    weightsout = players[instnum%50][4]
    biasout = players[instnum%50][5]



    while True:
        if instnum%displaynum==0:
            clock.tick(60)
            screen.fill((75,150,250))

        pipespassed=int(pipesx[0]+100<x)
        values1=np.array([np.dot(np.array([(pipesx[0+pipespassed]-x)/50,(pipesx[1+pipespassed]-x)/50,(pipesy[0+pipespassed]-y)/50,(pipesy[1+pipespassed]-y)/50,v/2]),np.array(j)) for j in weights1]) + np.array(biases1)
        values1=1/(1+np.exp(-1*values1))
        values2=np.array([np.dot(values1,np.array(j)) for j in weights2]) + np.array(biases2)
        values2=1/(1+np.exp(-1*values2))
        output=np.dot(values2,np.array(weightsout)) + biasout
        output=1/(1+np.exp(-1*output))
        #print(output)

        if instnum%displaynum==0:
            for event in pygame.event.get():
                # if event.type == pygame.QUIT:
                #     pygame.quit()
                #     quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        v = -10
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
        if output>0.5:
            v=-10
        v+=0.5
        y+=v if 0<y+v<600 else 0
        if pipesx[0]<-100:
            pipesx.append(pipesx.pop(0))
            pipesy.append(pipesy.pop(0))
        pipesy=[random.randint(110,490) if pipesx[i]<-100 else pipesy[i] for i in range(0,len(pipesx))]
        pipesx=[i-3 + 2000 * int(i<-100) for i in pipesx]
        score+=1
        if score>max_value and score%1000==0:
            print(score)
            print(players[instnum%50])
        players[instnum%50][-1]=score

        if instnum%displaynum==0:
            pygame.draw.circle(screen,(255,255,0), (x,int(y)),20)
            for i in range(0,len(pipesx)):
                pygame.draw.rect(screen,(0,150,0),(pipesx[i],pipesy[i]+100,100,600))
                pygame.draw.rect(screen,(0,150,0),(pipesx[i],pipesy[i]-700,100,600))

            screen.blit(font.render(f'Score: {round(score / 10)}', True, (0, 0, 0)), (10, 10))
            screen.blit(font.render(f'Gen: {int(np.floor(instnum / 50))+1}', True, (0, 0, 0)), (10, 40))
            screen.blit(font.render(f'Num: {instnum % 50+1}', True, (0, 0, 0)), (10, 70))

        if y < 20 or y > 580 or ((pipesx[0]<x<pipesx[0]+100) and (y<pipesy[0]-100 or pipesy[0]+100<y)):
            pygame.quit()
            break

        # print(x,y,v,pipesx,pipesy,score)
        if instnum%displaynum==0:
            pygame.display.update()

while True:
    instance()