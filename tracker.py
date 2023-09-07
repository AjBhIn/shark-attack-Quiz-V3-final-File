import pygame as pg
pg.init()

# Text style
jura_regular = pg.font.Font("Jura-Regular.ttf", 18)
jura_semibold = pg.font.Font("Jura-SemiBold.ttf", 18)

# Text color
text_color = (26, 83, 92)

class Dashboard:
    def __init__(self, font_style, text_color):
        #Antialise
        self.anitalise = True
        self.font_style = font_style

        self.distance_text =  self.font_style.render("Away from Shore", self.anitalise, text_color)
        