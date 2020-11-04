import math
print(math.pi)

import pygame
import numpy as np
from time import sleep

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((height, width))

bg = 50, 50, 50

screen.fill(bg)

nxC, nyC = 50, 50

dimCW = width/ nxC
dimCH = height/ nyC

#estado de celdas
gameState = np.zeros((nxC, nyC))

gameState[11, 11] = 1
gameState[12, 12] = 1
gameState[12, 13] = 1
gameState[11, 13] = 1
gameState[10, 13] = 1

gamePause = False

while True:
    newGameState = np.copy(gameState)
    ev = pygame.event.get()


    for event in ev:
        if event.type == pygame.KEYDOWN:
            gamePause = not gamePause

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor((posY / dimCH)))
            
            newGameState[celX, celY] = not mouseClick[2]


    

    screen.fill(bg)
    sleep(0.05)

    pygame.event.get()
    strokeColorEMT = 125, 125, 125
    strokeColorLive = 200, 200, 200

    for x in range(0, nxC):
        for y in range(0, nyC):

            if gamePause:
                n_neigh =   gameState[(x-1) % nxC, (y-1) % nyC ] + \
                            gameState[(x-1) % nxC, (y)   % nyC ] + \
                            gameState[(x-1) % nxC, (y+1) % nyC ] + \
                            gameState[(x)   % nxC, (y+1) % nyC ] + \
                            gameState[(x+1) % nxC, (y+1) % nyC ] + \
                            gameState[(x+1) % nxC, (y)   % nyC ] + \
                            gameState[(x+1) % nxC, (y-1) % nyC ] + \
                            gameState[(x)   % nxC, (y-1) % nyC ]

                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                if gameState[x, y] == 1 and (n_neigh > 3 or n_neigh < 2):
                    newGameState[x, y] = 0

            poly = [(x * dimCW,         (y+1) * dimCH),
                    ((x+1) * dimCW,     (y+1) * dimCH),
                    ((x+1) * dimCW,     (y) * dimCH),
                    (x * dimCW,         (y) * dimCH)]

            if gameState[x, y] == 1:
                pygame.draw.polygon(screen, strokeColorLive, poly, 0)
            else:
                pygame.draw.polygon(screen, strokeColorEMT, poly, 1)
            
    gameState = np.copy(newGameState)
    pygame.display.flip()

        #pygame.quit()