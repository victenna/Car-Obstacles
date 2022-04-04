import pygame,time
from math import *
pygame.init()
screen = pygame.display.set_mode((1200, 900))
road_img=pygame.image.load('road1.png')
clock = pygame.time.Clock()
class Car(pygame.sprite.Sprite):
    def __init__(self,img,pos):
        super().__init__()
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect(center=pos)
    def draw(self):
        screen.blit(self.image,self.rect)
        pygame.draw.rect(screen,'white',self.rect,3)
cars_position=[(500,650),(650,650),(500,500),(600,500),(700,500),(500,350),(580,350),\
          (660,350),(520,200),(630,200),(700,200),(500,70),(580,70),(660,70)]
Q=14
cars=[0]*Q
for i in range(Q):
    cars[i]=Car('car_2.png',cars_position[i])
class Main_Car(pygame.sprite.Sprite):
    def __init__(self,img,scale1,scale2,pos):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(scale1,scale2))
        self.rect=self.image.get_rect(center=pos)
    def draw(self):#,pos):
        screen.blit(self.image,self.rect)
a=400
Y,y=0,0
explosion=pygame.image.load('explosion.png')
start_time,end_time=0,0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('green')
    Y+=5
    y+=5
    if Y>1000: Y=0
    screen.blit(road_img,(0,Y-1000))
    for i in range(Q):
        cars[i].draw()
    button=pygame.key.get_pressed()
    if button[pygame.K_LEFT]:
        a=a-5
    if button[pygame.K_RIGHT]: a=a+5
    if a>720: a=700
    if a<480: a=500
    b=900-0.5*y
    if b<0: y=0
    mCar=Main_Car('car_4.png',35,55,(a,b))
    if start_time==0:
        mCar.draw()
    for i in range(Q):
        collision= pygame.sprite.collide_mask(mCar,cars[i])
        if collision!=None:
            ppos=cars_position[i]
            start_time=time.time()
    if start_time>0:
        end_time=round(time.time()-start_time,1)
        y=0
        screen.blit(explosion,explosion.get_rect(center=(ppos)))
    if end_time>=1:
        start_time=0
    pygame.display.update()
    clock.tick(200)