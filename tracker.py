from typing import Any
import pygame as pg
pg.init()

# Text style
jura_regular = pg.font.Font("Jura-Regular.ttf", 18)
jura_semibold = pg.font.Font("Jura-SemiBold.ttf", 18)
jura_medium = pg.font.Font("Jura-Medium.ttf", 25)

# Text color
text_color = (26, 83, 92)


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



