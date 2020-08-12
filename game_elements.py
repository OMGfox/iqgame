import pygame


class Block: 
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))


class Figure:
    def __init__(self, name):
        self.default_scheme = self.get_default_scheme()
        self.current_scheme = [list(i) for i in self.default_scheme]
        self.init_blocks()
        self.offset = 10
        self.pos = (0, 0)
        self.name = name

    def get_name(self):
        return self.name

    def is_mouseover(self):
        mouse_pos = pygame.mouse.get_pos()
        x = self.pos[0]
        y = self.pos[1]
        i_range = len(self.current_scheme)
        j_range = len(self.current_scheme[0])
        for i in range(i_range):
            for j in range(j_range):
                if not self.current_scheme[i][j] == 0:
                    if ((mouse_pos[0] >= x + 100 * j  and  mouse_pos[1] >= y + 100 * i) and
                            (mouse_pos[0] <= x + 100 * j + 100  and  mouse_pos[1] <= y + 100 * i + 100)):
                        return True        
        return False

    def get_default_scheme(self):
        default_scheme = ((1, 0),
                          (2, 0),
                          (3, 1))
        return default_scheme

    def get_current_scheme(self):
        return self.current_scheme
    
    def init_blocks(self):
        self.block_1 = Block("img/green_1.png")
        self.block_2 = Block("img/green_2.png")
        self.block_3 = Block("img/green_3.png")

    def draw(self, screen, x, y):
        self.pos = (x, y)
        i_range = len(self.current_scheme)
        j_range = len(self.current_scheme[0])
        for i in range(i_range):
            for j in range(j_range):
                if self.current_scheme[i][j] == 1:
                    self.block_1.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 2:
                    self.block_2.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 3:
                    self.block_3.draw(screen, x + 100 * j, y + 100 * i)

    def set_pos(self, x, y):
        self.pos = (x, y)

    def get_pos(self):
        return self.pos

    def rotate(self):
        temp_scheme = self.current_scheme
        temp_scheme.reverse()
        width = len(temp_scheme[0])
        hight = len(temp_scheme)
        new_scheme = [[0] * hight for i in range(width)]
        for i in range(len(temp_scheme)):
            for j in range(len(temp_scheme[i])):
                if temp_scheme[i][j] == 1:
                    new_scheme[j][i] = 2    
                elif temp_scheme[i][j] == 2:
                    new_scheme[j][i] = 1
                else:
                    new_scheme[j][i] = temp_scheme[i][j]
        self.current_scheme = new_scheme

    def turn(self):
        for i in self.current_scheme:
            i.reverse() 

    def get_matrix_pos(self):
        matrix = list()
        x = self.get_pos()[0] + 50 - (self.get_pos()[0] + 50) % 100 
        y = self.get_pos()[1] + 50 - (self.get_pos()[1] + 50) % 100
        w = len(self.current_scheme[0])
        h = len(self.current_scheme)

        if x + w * 100 > 500 + self.offset:
            x = (500 + self.offset) - w * 100 
        if y + h * 100 > 500 + self.offset:
            y = (500 + self.offset) - h * 100 

        for i in range(len(self.current_scheme)):
            for j in range(len(self.current_scheme[0])):
                if self.current_scheme[i][j] == 0:
                    continue
                matrix_element = int((x + 100 * j) / 100 + 5 * 
                        (y + 100 * i) / 100) 
                matrix.append(matrix_element)
        
        return matrix

class GreenFigure(Figure):
    def get_default_scheme(self):
        default_scheme = ((1, 0),
                          (2, 0),
                          (3, 1))
        return default_scheme

    def init_blocks(self):
        self.block_1 = Block("img/green_1.png")
        self.block_2 = Block("img/green_2.png")
        self.block_3 = Block("img/green_3.png")


class RedFigure(Figure):
    def get_default_scheme(self):
        default_scheme = ((1, 0),
                          (3, 0),
                          (2, 2))
        return default_scheme

    def init_blocks(self):
        self.block_1 = Block("img/red_1.png")
        self.block_2 = Block("img/red_2.png")
        self.block_3 = Block("img/red_3.png")


class YellowFigure(Figure):
    def get_default_scheme(self):
        default_scheme = ((3, 0),
                          (2, 2),
                          (1, 0))
        return default_scheme

    def init_blocks(self):
        self.block_1 = Block("img/yellow_1.png")
        self.block_2 = Block("img/yellow_2.png")
        self.block_3 = Block("img/yellow_3.png")


class BlueFigure(Figure):
    def get_default_scheme(self):
        default_scheme = ((2, 0),
                          (3, 1))
        return default_scheme

    def init_blocks(self):
        self.block_1 = Block("img/blue_1.png")
        self.block_2 = Block("img/blue_2.png")
        self.block_3 = Block("img/blue_3.png")


class PurpulFigure(Figure):
    def get_default_scheme(self):
        default_scheme = ((3, 0),
                          (1, 2))
        return default_scheme

    def init_blocks(self):
        self.block_1 = Block("img/purpul_1.png")
        self.block_2 = Block("img/purpul_2.png")
        self.block_3 = Block("img/purpul_3.png")


class PinkFigure(Figure):
    def get_default_scheme(self):
        default_scheme = ((3, 0),
                          (2, 1),
                          (0, 1))
        return default_scheme

    def init_blocks(self):
        self.block_1 = Block("img/pink_1.png")
        self.block_2 = Block("img/pink_2.png")
        self.block_3 = Block("img/pink_3.png")


class OrangeFigure(Figure):
    def get_default_scheme(self):
        default_scheme = ((3,),
                          (1,),
                          (2,))
        return default_scheme

    def init_blocks(self):
        self.block_1 = Block("img/orange_1.png")
        self.block_2 = Block("img/orange_2.png")
        self.block_3 = Block("img/orange_3.png")


class Field(Figure):
    # 0 - field_0
    # 1 - field_1
    # 2 - field_2
    # 3 - field_0_green
    # 4 - field_1_green
    # 5 - field_2_green
    # 6 - field_0_red
    # 7 - field_1_red
    # 8 - field_2_red

    def get_default_scheme(self):
        default_scheme = ((0, 1, 0, 1, 0),
                          (0, 1, 0, 2, 0),
                          (1, 2, 0, 1, 1),
                          (0, 0, 1, 0, 0),
                          (2, 0, 1, 2, 0))
        
        return default_scheme
    
    def init_blocks(self):
        self.block_0 = Block("img/field_0.png")
        self.block_1 = Block("img/field_1.png")
        self.block_2 = Block("img/field_2.png")
        self.block_0_green = Block("img/field_0_green.png")
        self.block_1_green = Block("img/field_1_green.png")
        self.block_2_green  = Block("img/field_2_green.png")
        self.block_0_red = Block("img/field_0_red.png")
        self.block_1_red = Block("img/field_1_red.png")
        self.block_2_red = Block("img/field_2_red.png")

    def draw(self, screen, x, y):
        for i in range(0, 5):
            for j in range(0, 5):
                if self.current_scheme[i][j] == 0:
                    self.block_0.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 1:
                    self.block_1.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 2:
                    self.block_2.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 3:
                    self.block_0_green.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 4:
                    self.block_1_green.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 5:
                    self.block_2_green.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 6:
                    self.block_0_red.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 7:
                    self.block_1_red.draw(screen, x + 100 * j, y + 100 * i)
                elif self.current_scheme[i][j] == 8:
                    self.block_2_red.draw(screen, x + 100 * j, y + 100 * i)

    def reset_default_scheme(self):
        self.current_scheme = [list(i) for i in self.default_scheme]

    def set_green_shadow(self, figure):
        self.reset_default_scheme()
        figure_scheme = figure.get_current_scheme()

        start_x_index = int((figure.get_pos()[1] + 50) / 100)
        if start_x_index > 5 - len(figure_scheme):
            start_x_index = 5 - len(figure_scheme)
        
        start_y_index = int((figure.get_pos()[0] + 50) / 100)
        if start_y_index > 5 - len(figure_scheme[0]):
            start_y_index = 5 - len(figure_scheme[0])
        
        i_range = len(figure_scheme)
        j_range = len(figure_scheme[0])
        for i in range(i_range):
            for j in range(j_range):
                if figure_scheme[i][j] == 0:
                    continue

                x = i + start_x_index
                y = j + start_y_index

                if self.current_scheme[x][y] == 0:
                    self.current_scheme[x][y] = 3
                elif self.current_scheme[x][y] == 1:
                    self.current_scheme[x][y] = 4
                elif self.current_scheme[x][y] == 2:
                    self.current_scheme[x][y] = 5

    def set_red_shadow(self, figure):
        self.reset_default_scheme()
        figure_scheme = figure.get_current_scheme()

        start_x_index = int((figure.get_pos()[1] + 50) / 100)
        if start_x_index > 5 - len(figure_scheme):
            start_x_index = 5 - len(figure_scheme)

        start_y_index = int((figure.get_pos()[0] + 50) / 100)
        if start_y_index > 5 - len(figure_scheme[0]):
            start_y_index = 5 - len(figure_scheme[0])
        
        i_range = len(figure_scheme)
        j_range = len(figure_scheme[0])
        for i in range(i_range):
            for j in range(j_range):
                if figure_scheme[i][j] == 0:
                    continue

                x = i + start_x_index
                y = j + start_y_index

                if self.current_scheme[x][y] == 0:
                    self.current_scheme[x][y] = 6
                elif self.current_scheme[x][y] == 1:
                    self.current_scheme[x][y] = 7
                elif self.current_scheme[x][y] == 2:
                    self.current_scheme[x][y] = 8


""" states:
        clicked,
        unclicked,
        blocked
"""

class Button:
    def __init__(self, main_sprite):
        self.state = "unclicked"
        self.pos = (0, 0)
        self.set_main_sprite(main_sprite)
        self.init_sprites()
        self.visibility = True
        self.name = None
        self.width = 50
        self.hight = 50

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

    def is_visible(self):
        return self.visibility

    def set_visibility(self, boolean: bool):
        self.visibility = boolean

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
    
    def set_screen(self, screen):
        self.screen = screen

    def is_mouseover(self):
        mouse_pos = pygame.mouse.get_pos()
        if ((mouse_pos[0] >= self.pos[0] and mouse_pos[1] >= self.pos[1]) and
            (mouse_pos[0] <= self.pos[0] + self.width and mouse_pos[1] <= self.pos[1] + self.hight)):
                return True
        else:
            return False

    def draw(self):
        x = self.pos[0]
        y = self.pos[1]
        self.screen.blit(self.unclicked_sprite, (x, y))
        if self.state == "clicked":
            self.screen.blit(self.clicked_sprite, (x, y))
        if self.state == "blocked":
            self.screen.blit(self.blocked_sprite, (x, y))
        if self.is_mouseover(): 
            self.screen.blit(self.mouseover_sprite, (x, y))

    def set_pos(self, x, y):
        self.pos = (x, y)

    def get_pos(self):
        return self.pos

    def set_mouseover_sprite(self, mouseover_sprite):
        self.mouseover_sprite = pygame.image.load(mouseover_sprite).convert_alpha()

    def init_sprites(self): 
        self.unclicked_sprite = self.main_sprite
        self.clicked_sprite = pygame.image.load("img/icons/clicked.png").convert_alpha()
        self.mouseover_sprite = pygame.image.load("img/icons/mouseover.png").convert_alpha()
        self.blocked_sprite = pygame.image.load("img/icons/blocked.png").convert_alpha()

    def set_main_sprite(self, main_sprite):
        self.main_sprite = pygame.image.load(main_sprite).convert_alpha()
    
class ButtonPanel:
    def __init__(self):
       self.green_button = Button("img/icons/green_icon.png")
       self.green_button.set_name("green")
       self.pink_button = Button("img/icons/pink_icon.png")
       self.pink_button.set_name("pink")
       self.purpul_button = Button("img/icons/purpul_icon.png")
       self.purpul_button.set_name("purpul")
       self.blue_button = Button("img/icons/blue_icon.png")
       self.blue_button.set_name("blue")
       self.yellow_button = Button("img/icons/yellow_icon.png")
       self.yellow_button.set_name("yellow")
       self.red_button = Button("img/icons/red_icon.png")
       self.red_button.set_name("red")
       self.orange_button = Button("img/icons/orange_icon.png")
       self.orange_button.set_name("orange")
       self.buttons = [self.green_button,
               self.pink_button,
               self.purpul_button,
               self.blue_button,
               self.yellow_button,
               self.red_button,
               self.orange_button]

    def get_buttons(self):
        return self.buttons

    def draw(self, screen, x, y):
        def_x = x
        i = 0
        for button in self.buttons:
            if button.is_visible():
                button.set_screen(screen)
                button.set_pos(x, y)
                button.draw()
                if i % 2 == 0:
                    x += 55        
                elif i % 2 == 1:
                    x = def_x
                    y += 60
                else:
                    x = def_x

                i += 1
                
    def reset_visibility(self):
        for button in self.buttons:
            button.set_visibility(True)


class ManagementButtonPanel:
    def __init__(self):
        self.rotate_button = Button("img/icons/rotate_icon.png")
        self.rotate_button.set_name("rotate")
        
        self.turn_button = Button("img/icons/turn_icon.png")
        self.turn_button.set_name("turn")

        self.clear_button = Button("img/icons/clear_icon.png")
        self.clear_button.set_name("clear")
        
        self.exit_button = Button("img/icons/exit_icon.png")
        self.exit_button.set_name("exit")
        self.exit_button.set_width(75)
        self.exit_button.set_height(30)
        self.exit_button.set_mouseover_sprite("img/icons/mouseover_exit_icon.png")

        self.buttons = [self.rotate_button,
                        self.turn_button,
                        self.clear_button,
                        self.exit_button]

    def get_buttons(self):
        return self.buttons

    def draw(self, screen, x, y):
        self.rotate_button.set_pos(x, y)
        self.turn_button.set_pos(x + 55, y)
        self.clear_button.set_pos(x + 25, y + 60)
        self.exit_button.set_pos(x + 10, y + 165)
        
        for button in self.buttons:
            button.set_screen(screen)
            button.draw() 


