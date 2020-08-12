import pygame
from game_elements import *
import sys


class Engine:
    def __init__(self, screen):
        self.offset_x = 10
        self.offset_y = 10
        self.screen = screen 
        self.button_panel = ButtonPanel()
        self.managment_button_panel = ManagementButtonPanel()
        self.figures = [OrangeFigure("orange"), RedFigure("red"), 
                        YellowFigure("yellow"), BlueFigure("blue"), 
                        PurpulFigure("purpul"), PinkFigure("pink"), 
                        GreenFigure("green")]
        self.focus = None
        self.next_figure()
        self.figures_on_field = []

    def get_offset(self):
        return (self.offset_x, self.offset_y)

    def next_figure(self):
        if self.focus:
            if len(self.figures):
                self.figures.insert(0, self.focus)
                self.focus = self.figures.pop()
            else:
                print("There are no object in list")
        else:
            if len(self.figures):
                self.focus = self.figures.pop() 
            else:
                print("There are no object in list")
        if len(self.figures) > 0:
            focus_name = self.focus.get_name()
            buttons = self.button_panel.get_buttons()
            for button in buttons:
                if not button.get_state() == "blocked":
                    if button.get_name() == focus_name:
                        button.set_state("clicked")
                    else:
                        button.set_state("unclicked")

    def is_out_field(self):
        result = False
        mouse_pos = pygame.mouse.get_pos()        
        if ((mouse_pos[0]) > (500 + self.offset_x) or
                (mouse_pos[1]) > (500 + self.offset_y)):
            result = True
        
        if (mouse_pos[0] < self.offset_x or
                mouse_pos[1] < self.offset_y):
            result = True
 

        return result

    def is_correct_position(self):
        result = True

        if self.is_out_field():
            result = False
        
        figure_scheme = self.focus.get_current_scheme()
        field_scheme = self.field.get_default_scheme()

        start_x_index = int((self.focus.get_pos()[1] + 50) / 100)
        if start_x_index > 5 - len(figure_scheme):
            start_x_index = 5 - len(figure_scheme)

        start_y_index = int((self.focus.get_pos()[0] + 50) / 100)
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

                if ((figure_scheme[i][j] == 1 and field_scheme[x][y] == 2) or 
                        (figure_scheme[i][j] == 2 and field_scheme[x][y] == 1)):
                    result = False
                    break
        if self.is_across_figures():
           result = False 
                
        return result
    
    def is_across_figures(self):
        result = False
        matrix = list()
        for figure in self.figures_on_field:
            [matrix.append(i) for i in figure.get_matrix_pos()]
        
        for i in self.focus.get_matrix_pos():
            if i in matrix:
                result = True
        return result

    def is_elements_set(self):
        if self.field and self.focus:
            return True
        else:
            return False

    def events_processing(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_e:
                    self.turn_focus()
                elif event.key == pygame.K_r:
                    self.rotate_focus()
                elif event.key == pygame.K_q:
                    self.next_figure()
                elif event.key == pygame.K_c:
                    self.clear_field()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.focus:
                        self.set_to_field()
                    else:
                        self.get_from_field()
                    self.button_actions_processing()
                    self.management_button_actions_processing()
                elif event.button == 3:
                    self.clear_focus()

    def get_from_field(self):
        for figure in self.figures_on_field:
            if figure.is_mouseover():
                figure_name = figure.get_name() 
                self.focus = self.pull_figure_from_field_by_name(figure_name)
                for button in self.button_panel.get_buttons():
                    if button.get_name() == figure_name:
                        button.set_visibility(True)
                        button.set_state("clicked")

    def button_actions_processing(self):
        buttons = self.button_panel.get_buttons()
        mouse_pos = pygame.mouse.get_pos()
        mouseover_button = None
        for button in buttons:
            if button.is_mouseover() and button.is_visible():
                mouseover_button = button
                break
       
        if mouseover_button:
            mouseover_button_state = mouseover_button.get_state()
            self.clear_focus()
            for button in buttons:
                button.set_state("unclicked")
                
            if mouseover_button_state == "unclicked":               
                mouseover_button.set_state("clicked")
                self.focus = self.pull_figure_by_name(mouseover_button.get_name()) 
            elif mouseover_button_state == "clicked":               
                mouseover_button.set_state("unclicked")          

    def management_button_actions_processing(self):
        buttons = self.managment_button_panel.get_buttons()
        mouse_pos = pygame.mouse.get_pos()
        mouseover_button = None
        for button in buttons:
            if button.is_mouseover() and button.is_visible():
                mouseover_button = button
                break

        if mouseover_button:
            mouseover_button_name = mouseover_button.get_name()
            if mouseover_button_name == "rotate":
                self.rotate_focus()
            elif mouseover_button_name == "turn":
                self.turn_focus()
            elif mouseover_button_name == "clear":
                self.clear_field()
                self.clear_focus()
            elif mouseover_button_name == "exit":
                sys.exit(0)
 
    def pull_figure_by_name(self, name):
        for i in range(len(self.figures)):
            if self.figures[i].get_name() == name:
                return self.figures.pop(i)
    
    def pull_figure_from_field_by_name(self, name):
        for i in range(len(self.figures_on_field)):
            if self.figures_on_field[i].get_name() == name:
                return self.figures_on_field.pop(i)

    def draw(self):
        if self.is_elements_set():
            self.draw_background()
            self.field.draw(self.screen, self.offset_x, self.offset_y)
            self.draw_buttons()
            self.draw_management_buttons()
            if self.is_correct_position():
                self.field.set_green_shadow(self.focus)
            else:
                if not self.is_out_field():
                    self.field.set_red_shadow(self.focus)
                else:
                    self.field.reset_default_scheme()
            self.draw_fields_figures()
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0] - 50
            y = mouse_pos[1] - 50
            self.focus.set_pos(x, y)

            if not self.is_out_field():
                self.focus.draw(self.screen, x, y)
            else:
                figure_w = len(self.focus.get_current_scheme()[0]) * 100
                figure_h = len(self.focus.get_current_scheme()) * 100
                self.focus.draw(self.screen, 250 - figure_w / 2, 
                        250 - figure_h / 2)
                self.field.reset_default_scheme()

        elif self.field:
            self.draw_background()
            self.field.draw(self.screen, self.offset_x, self.offset_y)
            self.draw_fields_figures()
            self.draw_buttons()
            self.draw_management_buttons()

    def draw_fields_figures(self):
        for figure in self.figures_on_field:
            x = figure.get_pos()[0] + 50 - (figure.get_pos()[0] + 50) % 100 + self.offset_x
            y = figure.get_pos()[1] + 50 - (figure.get_pos()[1] + 50) % 100 + self.offset_y
            figure.draw(self.screen, x, y)

    def draw_background(self):
        background = pygame.image.load("img/background.png").convert_alpha()
        self.screen.blit(background, (0, 0))

    def draw_management_buttons(self):
        self.managment_button_panel.draw(self.screen, 520, 300)
 
    def draw_buttons(self):
        self.button_panel.draw(self.screen, 520, 20)

    def set_to_field(self):
        if self.focus and not self.is_out_field():
            if self.is_correct_position():
                
                w = len(self.focus.get_current_scheme()[0])
                h = len(self.focus.get_current_scheme())
                x = self.focus.get_pos()[0]
                y = self.focus.get_pos()[1]

                if (x + w * 100) > (500 + self.offset_x):
                    x = (500 + self.offset_x) - w * 100
                if (y + h * 100) > (500 + self.offset_y):
                    y = (500 + self.offset_y) - h * 100
                
                self.focus.set_pos(x, y)

                self.figures_on_field.append(self.focus)
                self.focus = None
                self.field.reset_default_scheme()
#                self.next_figure()

                buttons = self.button_panel.get_buttons()
                for figure in self.figures_on_field:
                    figure_name = figure.get_name()
                    for button in buttons:
                        if button.get_name() == figure_name:
                            button.set_visibility(False)

    def clear_focus(self):
        if self.focus:
            self.figures.append(self.focus)
            self.field.reset_default_scheme()
            focus_name = self.focus.get_name()
            self.focus = None
            buttons = self.button_panel.get_buttons()
            for button in buttons:
                if button.get_name() == focus_name:
                    button.state = "unclicked"

    def clear_field(self):
        for i in range(len(self.figures_on_field)):
            self.figures.append(self.figures_on_field.pop())
        if not self.focus:
            self.next_figure()
        self.button_panel.reset_visibility()
        
    def set_field(self, field):
        self.field = field

    def set_focus(self, figure):
        self.focus = figure

    def rotate_focus(self):
        if self.focus:
            self.focus.rotate()

    def turn_focus(self):
        if self.focus:
            self.focus.turn()

