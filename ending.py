import pygame as pg

# Font styles
jura_bold = "Jura-Bold.ttf"
    # Font Colours
ending_string_colr = (26, 83, 92)

class Endingtext(pg.sprite.Sprite):
    def __init__(self, text, text_x, text_y, font_style = jura_bold, font_colr = ending_string_colr):
        super().__init__()

        # Font
        self.text = text
        self.antialise = True
            # Using font initial
        pg.font.init()
            # Font style
        self.ending_font_size = 60
        self.jura_bold = pg.font.Font(font_style, self.ending_font_size)

        # Variables
        self.text_x = int(text_x/2)
        self.text_y = text_y

        # Text
        self.image = self.jura_bold.render(self.text, self.antialise, font_colr)
        self.rect = self.image.get_rect(center = (self.text_x, self.text_y))


# Instance of class
failed_string =  Endingtext("YOU DIED", 1042, 165)
passed_string =  Endingtext("JAWS ESCAPED", 1042, 155)

# Sprite for text
ending_string_sprit = pg.sprite.GroupSingle()