from typing import Any
import pygame as pg

# Font styles
jura_bold = "Jura-Bold.ttf"
    # Font Colours
ending_string_colr = (26, 83, 92)

class Endingtext(pg.sprite.Sprite):
    def __init__(self, text, text_x, text_y, font_size = 60, font_style = jura_bold, font_colr = ending_string_colr):
        super().__init__()

        # Font
        self.text = text
        self.antialise = True
        self.font_colr = font_colr
            # Using font initial
        pg.font.init()
            # Font style
        self.ending_font_size = font_size
        self.jura_bold = pg.font.Font(font_style, self.ending_font_size)

        # Variables
        self.text_x = int(text_x/2)
        self.text_y = text_y

        # Text
        self.image = self.jura_bold.render(self.text, self.antialise, self.font_colr)
        self.rect = self.image.get_rect(center = (self.text_x, self.text_y))

# Sprite for text
ending_string_sprit = pg.sprite.Group()


class Scoretext(pg.sprite.Sprite):
    def __init__(self, text, text_x, text_y, font_size = 35, font_style = jura_bold, font_colr = ending_string_colr):
        super().__init__()

        # Font
        self.text = text
        self.antialise = True
        self.font_colr = font_colr
            # Using font initial
        pg.font.init()
            # Font style
        self.ending_font_size = font_size
        self.jura_bold = pg.font.Font(font_style, self.ending_font_size)

        # Variables
        self.text_x = int(text_x/2)
        self.text_y = text_y

        # Text
        self.image = self.jura_bold.render(self.text, self.antialise, self.font_colr)
        self.rect = self.image.get_rect(center = (self.text_x, self.text_y))

    def update(self, updated_text):
        self.text = updated_text

        #updating the text with score and time
        self.image = self.jura_bold.render(self.text, self.antialise, self.font_colr)
        self.rect = self.image.get_rect(center = (self.text_x, self.text_y))

# Sprite for text
ending_score_sprit = pg.sprite.Group()


# Dead image sprite
class Deadscene(pg.sprite.Sprite):
    def __init__(self, img, placement):
        super().__init__()
        self.placement = placement
        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft = self.placement)

    def update(self, y):
            self.rect.y = y

dead_sprite = pg.sprite.GroupSingle()