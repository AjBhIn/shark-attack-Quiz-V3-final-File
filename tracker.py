from typing import Any
import pygame as pg
pg.init()

# Text style
jura_regular = pg.font.Font("Jura-Regular.ttf", 18)
jura_semibold = pg.font.Font("Jura-SemiBold.ttf", 18)
jura_medium = pg.font.Font("Jura-Medium.ttf", 25)

# Text color
text_color = (26, 83, 92)

# Colors
display_text_color = (247, 255, 247)

class Dashboard:
    def __init__(self, window, text_placement, font_style, var, text_color = text_color):

        #Text settings
        self.anitalise = True
        self.font_style = font_style
        self.var = var
        self.window = window

        self.text =  self.font_style.render(self.var, self.anitalise, text_color)
        self.text_placement = self.text.get_rect(midleft = text_placement)
        self.window.blit(self.text, self.text_placement)


# class Display:
#     def __init__(self, font_style, display_text, text_color, display_color = display_color):

#         # Text Settings
#         self.display_text = display_text
#         self.anitalise = True
#         self.display = pg.image.load()
#         self.display.fill(display_color)
#         self.rect = self.display.get_rect(midleft = (435, 368))
#         self.font_style = font_style

#         self.display_text =  self.font_style.render(self.display_text, self.anitalise, text_color)
#         self.display_text_placement = self.display_text.get_rect(center = (int(self.display.get_width()/2), int(self.display.get_height()/2)))
#         self.display.blit(self.display_text, self.display_text_placement)


