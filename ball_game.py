
# -*- coding: utf-8 -*-
"""
Created on thursday Jan 1 09:49:10 2024

@author: Bouadi Khadija
"""

import pygame
pygame.init()
class ball:
    def __init__(self,x,y,p):
        self.Px=x
        self.Py=y
        self.splote=p
        self.speed=.01
        self.sensX=True
        self.sensY=True

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
# Run until the user asks to quit
running = True
ball=ball(250,250,1)
while running:
    for event in pygame.event.get():
        # click on the window close button?
        if event.type == pygame.QUIT:
            running = False
        # start pressing ?
        if event.type == pygame.MOUSEBUTTONDOWN:
            posStart = pygame.mouse.get_pos()
            (ball.Px,ball.Py)=posStart
        # end pressing ?
        if event.type == pygame.MOUSEBUTTONUP:
            posEnd = pygame.mouse.get_pos()
            
              
    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    
    pygame.draw.circle(screen, (0, 0, 255), (ball.Px, ball.Py), 10)
        
    
    # Flip the display
    pygame.display.flip()
    
pygame.quit()