
import pygame
import random

class Pipe:
    def __init__(self,img):
        self.__height=[200,300,400]
        self.__img = img
        self.__speed = 5
        self.top_pipe=None
        self.bottom_pipe=None

    def create(self):
        height=random.choice(self.__height)
        self.bottom_pipe=self.__img.get_rect(midtop=(500,height))
        self.top_pipe=self.__img.get_rect(midtop=(500,height-650))

    def move(self):
        if self.top_pipe.x:
            self.top_pipe.x-=self.__speed
        if self.bottom_pipe.x:
            self.bottom_pipe.x-=self.__speed

    def draw(self,screen):
        if self.top_pipe and self.bottom_pipe:
            flipped_img=pygame.transform.rotate(self.__img,180)
            screen.blit(flipped_img,self.top_pipe)

            screen.blit(self.__img,self.bottom_pipe)

