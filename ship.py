import pygame
class Ship():
    def __init__(self, screen):

        self.screen = screen

        self.image = pygame.image.load('images/pangzi1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = 600
        #self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 2
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 2
        if self.moving_up and self.rect.top>500:
            self.rect.bottom -= 5
        
    def blitme(self):

        self.screen.blit(self.image, self.rect)