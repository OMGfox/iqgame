import game_elements
from engine import Engine
import pygame
import sys

 
screen = pygame.display.set_mode((630, 520))
field = game_elements.Field("field")
engine = Engine(screen)
engine.set_field(field)
offset = engine.get_offset()
pygame.mouse.set_pos(150 + offset[0], 150 + offset[1])


engine.draw_background()

while True:
    engine.events_processing()
    engine.draw()
    pygame.display.update()
    pygame.time.delay(10)
