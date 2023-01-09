#pygame_gui_coloured_themed_buttons.py
import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600), 'theme.json')

hello_button_red = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (150, 50)),
                                            text='Red Button',
                                            manager=manager,
                                            object_id=ObjectID( class_id='@friendly_buttons',
                                                                object_id='#red_button')
                                            
                                            )
hello_button_blue = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 275), (150, 50)),
                                            text='Blue Button',
                                            manager=manager,
                                            object_id=ObjectID( class_id='@friendly_buttons',
                                                                object_id='#blue_button')
                                            )

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button_red:
                print('Red button pressed.')
            if event.ui_element == hello_button_blue:
                print('Blue button pressed.')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()