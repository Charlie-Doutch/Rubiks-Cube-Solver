import sys
import pygame

from main import SolveCube

pygame.init()

pygame.display.set_caption("Charlie's 3x3 Cube Solver")

screen = pygame.display.set_mode((1024, 768))

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)

# colour to letter mapping
colour_to_letter = {
    'White': 'w',
    'Green': 'g',
    'Red': 'r',
    'Blue': 'b',
    'Orange': 'o',
    'Yellow': 'y'
}

class Block:
    """
    Creates the individual blocks that the user clicks on to change the initial state of the cube
    """
    def __init__(self, x, y, width, height, initial_colour, block_colours):
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = block_colours.index(initial_colour)
        self.block_colours = block_colours

    def change_colour(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = (self.clicked + 1) % len(self.block_colours)

    def draw(self, screen):
        pygame.draw.rect(screen, self.block_colours[self.clicked], self.rect)

    def get_colour(self):
        return self.block_colours[self.clicked]

class Blocks:
    """
    Takes the block template from the Block class, and gives them the inital values and position on the screen
    """
    def __init__(self):
        self.block_colours = ['White', 'Green', 'Red', 'Blue', 'Orange', 'Yellow']
        self.blocks = [
            # White Side
            Block(347, 50, 50, 50, 'White', self.block_colours),
            Block(402, 50, 50, 50, 'White', self.block_colours),
            Block(457, 50, 50, 50, 'White', self.block_colours),
            Block(347, 105, 50, 50, 'White', self.block_colours),
            Block(457, 105, 50, 50, 'White', self.block_colours),
            Block(347, 160, 50, 50, 'White', self.block_colours),
            Block(402, 160, 50, 50, 'White', self.block_colours),
            Block(457, 160, 50, 50, 'White', self.block_colours),
            # Green Side
            Block(177, 220, 50, 50, 'Green', self.block_colours),
            Block(232, 220, 50, 50, 'Green', self.block_colours),
            Block(287, 220, 50, 50, 'Green', self.block_colours),
            Block(177, 275, 50, 50, 'Green', self.block_colours),
            Block(287, 275, 50, 50, 'Green', self.block_colours),
            Block(177, 330, 50, 50, 'Green', self.block_colours),
            Block(232, 330, 50, 50, 'Green', self.block_colours),
            Block(287, 330, 50, 50, 'Green', self.block_colours),
            # Red Side
            Block(347, 220, 50, 50, 'Red', self.block_colours),
            Block(402, 220, 50, 50, 'Red', self.block_colours),
            Block(457, 220, 50, 50, 'Red', self.block_colours),
            Block(347, 275, 50, 50, 'Red', self.block_colours),
            Block(457, 275, 50, 50, 'Red', self.block_colours),
            Block(347, 330, 50, 50, 'Red', self.block_colours),
            Block(402, 330, 50, 50, 'Red', self.block_colours),
            Block(457, 330, 50, 50, 'Red', self.block_colours),
            # Blue Side
            Block(517, 220, 50, 50, 'Blue', self.block_colours),
            Block(572, 220, 50, 50, 'Blue', self.block_colours),
            Block(627, 220, 50, 50, 'Blue', self.block_colours),
            Block(517, 275, 50, 50, 'Blue', self.block_colours),
            Block(627, 275, 50, 50, 'Blue', self.block_colours),
            Block(517, 330, 50, 50, 'Blue', self.block_colours),
            Block(572, 330, 50, 50, 'Blue', self.block_colours),
            Block(627, 330, 50, 50, 'Blue', self.block_colours),
            # Orange Side
            Block(687, 220, 50, 50, 'Orange', self.block_colours),
            Block(742, 220, 50, 50, 'Orange', self.block_colours),
            Block(797, 220, 50, 50, 'Orange', self.block_colours),
            Block(687, 275, 50, 50, 'Orange', self.block_colours),
            Block(797, 275, 50, 50, 'Orange', self.block_colours),
            Block(687, 330, 50, 50, 'Orange', self.block_colours),
            Block(742, 330, 50, 50, 'Orange', self.block_colours),
            Block(797, 330, 50, 50, 'Orange', self.block_colours),
            # Yellow Side
            Block(347, 390, 50, 50, 'Yellow', self.block_colours),
            Block(402, 390, 50, 50, 'Yellow', self.block_colours),
            Block(457, 390, 50, 50, 'Yellow', self.block_colours),
            Block(347, 445, 50, 50, 'Yellow', self.block_colours),
            Block(457, 445, 50, 50, 'Yellow', self.block_colours),
            Block(347, 500, 50, 50, 'Yellow', self.block_colours),
            Block(402, 500, 50, 50, 'Yellow', self.block_colours),
            Block(457, 500, 50, 50, 'Yellow', self.block_colours),
        ]
        self.centres = {
            'White': 'w',
            'Green': 'g',
            'Red': 'r',
            'Blue': 'b',
            'Orange': 'o',
            'Yellow': 'y'
        }

    def change_colour(self, event):
        for block in self.blocks:
            block.change_colour(event)

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)

    def get_colours_string(self):
        # Insert centre pieces at the correct position within each face string
        def insert_center(colour_string, centre):
            return colour_string[:4] + centre + colour_string[4:]

        colors_string = [
            insert_center(''.join(colour_to_letter[block.get_colour()] for block in self.blocks[0:8]), self.centres['White']),
            insert_center(''.join(colour_to_letter[block.get_colour()] for block in self.blocks[8:16]), self.centres['Green']),
            insert_center(''.join(colour_to_letter[block.get_colour()] for block in self.blocks[16:24]), self.centres['Red']),
            insert_center(''.join(colour_to_letter[block.get_colour()] for block in self.blocks[24:32]), self.centres['Blue']),
            insert_center(''.join(colour_to_letter[block.get_colour()] for block in self.blocks[32:40]), self.centres['Orange']),
            insert_center(''.join(colour_to_letter[block.get_colour()] for block in self.blocks[40:48]), self.centres['Yellow']),
        ]
        return ''.join(colors_string)

class Buttons:
    """
    Creates the button that the user presses to start the solving process of the program
    """
    def __init__(self):
        pass

    def solve_button(self, screen):
        x = 724
        y = 640
        width = 200
        height = 80
        self.rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


blocks = Blocks()

buttons = Buttons()

cube_net = pygame.image.load("Rubiks-Cube-Solver/Assets/Cube_Net.png").convert_alpha()

solve_button_text = font.render('Solve', True, 'Black')

instructions_text1 = font.render('Click the individual squares', True, 'Black')

instructions_text2 = font.render('on the net of the cube to', True, 'Black')

instructions_text3 = font.render('match your own, then press solve.', True, 'Black')

while True:
    screen.fill((255, 209, 245))

    screen.blit(cube_net, (0, 0))

    blocks.draw(screen)

    buttons.solve_button(screen)

    screen.blit(solve_button_text, (775, 665))

    screen.blit(instructions_text1, (20, 630))
    
    screen.blit(instructions_text2, (20, 665))
    
    screen.blit(instructions_text3, (20, 700))

    # Get the colour string
    colours_string = blocks.get_colours_string()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = event.pos  # Get mouse position
                if buttons.is_clicked(pos):
                    solve_cube = SolveCube(colours_string)
                    solve_cube.solve()
                else:
                    blocks.change_colour(event)  # Change color if not on button


    pygame.display.update()
    clock.tick(60)
