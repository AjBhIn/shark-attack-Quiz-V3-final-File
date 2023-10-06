import pygame as pg

class Exitbutton(pg.sprite.Sprite):
    def __init__(self, x_pos):
        super().__init__()

        # Button settings
        self.bt_width = 1043
        self.bt_height  = 50
        self.y_pos =  697
        self.x_pos = x_pos
        self.bt_color = (78, 205, 196)

        self.image = pg.surface.Surface((self.bt_width, self.bt_height))
        self.image.fill(self.bt_color)
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))

exit_bt_sprite = pg.sprite.Group()

# Font Galary
jura_bold = "Jura-Bold.ttf"
jura_medium = "Jura-Medium.ttf"
jura_regular = "Jura-Regular.ttf"
exit_font_size = 30
exit_button_font_colr =  (247, 255, 247)
exit_message_font_colr =  (0,0,0)

class Exittext:
    def __init__(self):
        pass