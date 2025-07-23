import pygame
class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.__font=pygame.font.Font('../assets/04B_19.ttf',40)

    def displayScore(self,screen):
           self.surFace = pygame.font.Font('../assets/04B_19.ttf', 40).render(str(self.score), True, (255, 255, 255))
           self.rect = self.surFace.get_rect(center=(200, 50))
           screen.blit(self.surFace, self.rect)


    def displayHighScore(self,screen):
        self.surFace = pygame.font.Font('../assets/04B_19.ttf', 40).render(f"High Score: {str(self.high_score)}", True, (255, 255, 255))
        self.rect = self.surFace.get_rect(center=(200, 300))
        screen.blit(self.surFace, self.rect)