import pygame as pg

# Button styles
main_play_bt_colr = (78, 205, 196)
help_play_bt_colr = (255, 107, 107)
play_text_colr = (247, 255, 247)
play_text_size = 30
help_text_size = 20
jura_light = "Jura-Light.ttf"
jura_bold = "Jura-Bold.ttf"
jura_regular = "Jura-Regular.ttf"
jura_medium = "Jura-Medium.ttf"
jura_semibold = "Jura-SemiBold.ttf"
title_font_size =  110
help_title_font_size = 60
help_line_font_size = 20

class Playbt(pg.sprite.Sprite):
    def __init__(self, img, x_pos, y_pos, text, font_color = play_text_colr, font_size = play_text_size, font_style = jura_light):
        super().__init__()

        # Button settings
        self.img = img
        self.y_pos =  y_pos
        self.x_pos = x_pos
        self.bt_state = False

        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

        # Font
        self.text = text
        self.antialise = True
        self.font_colr = font_color
        # Using font initial
        pg.font.init()
        # Font style
        self.font_size = font_size
        self.font_style = pg.font.Font(font_style, self.font_size)
        # Text
        self.text_rendering = self.font_style.render(self.text, self.antialise, self.font_colr)
        self.text_pos = self.text_rendering.get_rect(center = (int(self.image.get_width()/2), int(self.image.get_height()/2)))
        # Rendering the Text
        self.image.blit(self.text_rendering, self.text_pos)
    
    def update(self):
        bt_pressed = self.cliked()
        return bt_pressed
    
    def cliked(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_left_bt_state = pg.mouse.get_pressed()[0]
        if self.rect.collidepoint(mouse_pos):
            if mouse_left_bt_state == True:
                self.bt_state = True
        if self.bt_state:
            return True
        else:
            return False

play_bt_sprite = pg.sprite.Group()

class HelpPlaybt(pg.sprite.Sprite):
    def __init__(self, img, x_pos, y_pos, text, font_color = play_text_colr, font_size = play_text_size, font_style = jura_light):
        super().__init__()

        # Button settings
        self.img = img
        self.y_pos =  y_pos
        self.x_pos = x_pos
        self.bt_state = False

        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

        # Font
        self.text = text
        self.antialise = True
        self.font_colr = font_color
        # Using font initial
        pg.font.init()
        # Font style
        self.font_size = font_size
        self.font_style = pg.font.Font(font_style, self.font_size)
        # Text
        self.text_rendering = self.font_style.render(self.text, self.antialise, self.font_colr)
        self.text_pos = self.text_rendering.get_rect(center = (int(self.image.get_width()/2), int(self.image.get_height()/2)))
        # Rendering the Text
        self.image.blit(self.text_rendering, self.text_pos)
    
    def update(self):
        bt_pressed = self.cliked()
        return bt_pressed
    
    def cliked(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_left_bt_state = pg.mouse.get_pressed()[0]
        if self.rect.collidepoint(mouse_pos):
            if mouse_left_bt_state == True:
                self.bt_state = True
        if self.bt_state:
            return True
        else:
            return False

help_play_bt_sprite = pg.sprite.Group()


class Helpbt(pg.sprite.Sprite):
    def __init__(self, img, x_pos, y_pos, text, font_color = play_text_colr, font_size = play_text_size, font_style = jura_light):
        super().__init__()

        # Button settings
        self.img = img
        self.y_pos =  y_pos
        self.x_pos = x_pos
        self.bt_state = False

        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

        # Font
        self.text = text
        self.antialise = True
        self.font_colr = font_color
        # Using font initial
        pg.font.init()
        # Font style
        self.font_size = font_size
        self.font_style = pg.font.Font(font_style, self.font_size)
        # Text
        self.text_rendering = self.font_style.render(self.text, self.antialise, self.font_colr)
        self.text_pos = self.text_rendering.get_rect(center = (int(self.image.get_width()/2), int(self.image.get_height()/2)))
        # Rendering the Text
        self.image.blit(self.text_rendering, self.text_pos)
    
    def update(self):
        bt_pressed = self.cliked()
        return bt_pressed
    
    def cliked(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_left_bt_state = pg.mouse.get_pressed()[0]
        if self.rect.collidepoint(mouse_pos):
            if mouse_left_bt_state == True:
                self.bt_state = True
        if self.bt_state:
            return True
        else:
            return False

help_bt_sprite = pg.sprite.Group()

class Introtext(pg.sprite.Sprite):
    def __init__(self, text, font_size, font_style, x_pos, y_pos, font_color = play_text_colr):
        super().__init__()
        # Font
        self.text = text
        self.antialise = True
        self.font_colr = font_color
        self.x_pos = x_pos
        self.y_pos = y_pos
        # Using font initial
        pg.font.init()
        # Font style
        self.font_size = font_size
        self.font_style = pg.font.Font(font_style, self.font_size)
        # Text
        self.image = self.font_style.render(self.text, self.antialise, self.font_colr)
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

intro_text_sprite = pg.sprite.Group()

class Introhelptext(pg.sprite.Sprite):
    def __init__(self, text, font_size, font_style, x_pos, y_pos, font_color = play_text_colr):
        super().__init__()
        # Font
        self.text = text
        self.antialise = True
        self.font_colr = font_color
        self.x_pos = x_pos
        self.y_pos = y_pos
        # Using font initial
        pg.font.init()
        # Font style
        self.font_size = font_size
        self.font_style = pg.font.Font(font_style, self.font_size)
        # Text
        self.image = self.font_style.render(self.text, self.antialise, self.font_colr)
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

intro_help_text_sprite = pg.sprite.Group()

class Helpbg(pg.sprite.Sprite):
    def __init__(self, img, x_pos, y_pos):
        super().__init__()
                # Button settings
        self.img = img
        self.y_pos =  y_pos
        self.x_pos = x_pos
        self.bt_state = False

        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

intro_help_sprite = pg.sprite.Group()
