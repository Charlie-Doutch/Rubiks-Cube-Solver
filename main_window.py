import sys

import pygame
    
pygame.init()

pygame.display.set_caption('RCS')

screen = pygame.display.set_mode((1024, 768))

clock = pygame.time.Clock()

class Block:
    def __init__(self, x, y, width, height, block_colours):
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = 0
        self.block_colours = block_colours

    def change_colour(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = (self.clicked + 1) % len(self.block_colours)

    def draw(self, screen):
        pygame.draw.rect(screen, self.block_colours[self.clicked], self.rect)

class Blocks:
    def __init__(self):
        self.block_colours = ['White', 'Green', 'Red', 'Blue', 'Orange', 'Yellow']
        self.blocks = [
            #White Side
            Block(347, 50, 50, 50, self.block_colours),
            Block(402, 50, 50, 50, self.block_colours),
            Block(457, 50, 50, 50, self.block_colours),
            Block(347, 105, 50, 50, self.block_colours),
            Block(457, 105, 50, 50, self.block_colours),
            Block(347, 160, 50, 50, self.block_colours),
            Block(402, 160, 50, 50, self.block_colours),
            Block(457, 160, 50, 50, self.block_colours),
            #Red Side
            Block(347, 220, 50, 50, self.block_colours),
            Block(402, 220, 50, 50, self.block_colours),
            Block(457, 220, 50, 50, self.block_colours),
            Block(347, 275, 50, 50, self.block_colours),
            Block(457, 275, 50, 50, self.block_colours),
            Block(347, 330, 50, 50, self.block_colours),
            Block(402, 330, 50, 50, self.block_colours),
            Block(457, 330, 50, 50, self.block_colours),
            #Green Side
            Block(177, 220, 50, 50, self.block_colours),
            Block(232, 220, 50, 50, self.block_colours),
            Block(287, 220, 50, 50, self.block_colours),
            Block(177, 275, 50, 50, self.block_colours),
            Block(287, 275, 50, 50, self.block_colours),
            Block(177, 330, 50, 50, self.block_colours),
            Block(232, 330, 50, 50, self.block_colours),
            Block(287, 330, 50, 50, self.block_colours),
            #Blue Side
            Block(517, 220, 50, 50, self.block_colours),
            Block(572, 220, 50, 50, self.block_colours),
            Block(627, 220, 50, 50, self.block_colours),
            Block(517, 275, 50, 50, self.block_colours),
            Block(627, 275, 50, 50, self.block_colours),
            Block(517, 330, 50, 50, self.block_colours),
            Block(572, 330, 50, 50, self.block_colours),
            Block(627, 330, 50, 50, self.block_colours),
            #Orange Side
            Block(687, 220, 50, 50, self.block_colours),
            Block(742, 220, 50, 50, self.block_colours),
            Block(797, 220, 50, 50, self.block_colours),
            Block(687, 275, 50, 50, self.block_colours),
            Block(797, 275, 50, 50, self.block_colours),
            Block(687, 330, 50, 50, self.block_colours),
            Block(742, 330, 50, 50, self.block_colours),
            Block(797, 330, 50, 50, self.block_colours),
            #Yellow Side
            Block(347, 390, 50, 50, self.block_colours),
            Block(402, 390, 50, 50, self.block_colours),
            Block(457, 390, 50, 50, self.block_colours),
            Block(347, 445, 50, 50, self.block_colours),
            Block(457, 445, 50, 50, self.block_colours),
            Block(347, 500, 50, 50, self.block_colours),
            Block(402, 500, 50, 50, self.block_colours),
            Block(457, 500, 50, 50, self.block_colours),
        ]

    def change_colour(self, event):
        for block in self.blocks:
            block.change_colour(event)

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)

blocks = Blocks()

cube_net = pygame.image.load("Rubiks-Cube-Solver/Assets/Cube_Net.png").convert_alpha()
 

while True:

    screen.fill((255, 184, 179))

    screen.blit(cube_net, (0, 0))

    blocks.draw(screen)

    mouse_pos = pygame.mouse.get_pos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                blocks.change_colour(event)
    
    pygame.display.update()
    clock.tick(60)
