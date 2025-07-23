import pygame
from pygame.examples.scrap_clipboard import screen
from ListPipe import ListPipe
from Pipe import Pipe

#pipes = ListPipe()
class Bird:
    def __init__(self,images,x,y):
        self.images=images
        self.index=0
        self.image=self.images[self.index]
        self.rect=self.image.get_rect(center=(x,y))
        self.__movement=0
        self.__gravity=0.5
        self.pipes=ListPipe()

    def update(self):
        self.index=(self.index+1)%len(self.images)
        self.image=self.images[self.index]


    def move(self):
        self.__movement+=self.__gravity
        self.rect.centery+=self.__movement


    def jump(self):
        self.__movement=-7


    def checkcollision(self):
        for pipe in self.pipes:
            if self.rect.colliderect(pipe.top_pipe) or self.rect.colliderect(pipe.bottom_pipe):
                return True
            if self.rect.centery>=600 or self.rect.centery<=-75:
                return True

        return False

    def rotateBird(self):
        self.new_bird=pygame.transform.rotozoom(self.image,-self.__movement*3,1)
        return self.new_bird

    def draw(self,screen):
        rotate_bird=self.rotateBird()
        screen.blit(rotate_bird,self.rect)




