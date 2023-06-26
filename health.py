import pygame
class hp():
    def __init__(self,x,y,w,h,maxhp):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.hp=maxhp
        self.maxhp=maxhp
        
    def draw(self,surface):
        ratio=self.hp/self.maxhp
        pygame.draw.rect(surface,"red",(self.x,self.y,self.w*ratio,self.h))
        pygame.draw.rect(surface,"dark green",(self.x,self.y,self.w,self.h),5)
       
