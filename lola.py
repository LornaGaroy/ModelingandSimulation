import pygame
import sys
import math
import random

pygame.init()
pygame.mouse.set_visible(True)
font = pygame.font.Font("freesansbold.ttf", 32)


clock = pygame.time.Clock()
window = pygame.display.set_mode([800,600])
background_color = pygame.Color(240,25,255)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 10
        self.color = pygame.Color(0,0,0)

    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_x *= 0.99
        self.velocity_y *= 0.99

        self.x = int(self.x)
        self.y = int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1

        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y > 600):
            self.velocity_y *=-1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

list_of_balls = [Ball(50,300), 
                 Ball(115,280), 
                 Ball(100,300), 
                 Ball(115,320)]



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(background_color)

    mouse_pos = pygame.mouse.get_pos()
    msg = "%i %i" %(mouse_pos[0],mouse_pos[1])
    text = font .render(msg, False, pygame.Color(0,0,0))
    window.blit(text,[0,0])

    for ball in list_of_balls:    
        ball.update()
        
        ball.draw(window)

    pygame.display.update()
    clock.tick(30)
