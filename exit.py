import pygame as pg

# Font Galary
jura_bold = "Jura-Bold.ttf"
jura_medium = "Jura-Medium.ttf"
jura_regular = "Jura-Regular.ttf"
exit_font_size = 30
exit_button_font_colr =  (247, 255, 247)
exit_message_font_colr =  (0,0,0)

class Exitbutton(pg.sprite.Sprite):
    def __init__(self, x_pos, font_color = exit_button_font_colr, font_size = exit_font_size, font_style = jura_regular):
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

        # Font
        self.text = "Exit"
        self.antialise = True
        self.font_colr = font_color
        # Using font initial
        pg.font.init()
        # Font style
        self.ending_font_size = font_size
        self.font_style = pg.font.Font(font_style, self.ending_font_size)
        # Text
        self.text_rendering = self.font_style.render(self.text, self.antialise, self.font_colr)
        self.text_pos = self.text_rendering.get_rect(center = (int(self.image.get_width()/2), int(self.image.get_height()/2)))
        # Rendering the Text
        self.image.blit(self.text_rendering, self.text_pos)

exit_bt_sprite = pg.sprite.Group()

class Exitmessage(pg.sprite.Sprite):
    def __init__(self, text, text_2, img, font_color = exit_message_font_colr, font_size = exit_font_size, font_style = jura_bold):
        super().__init__()

        # Button settings
        self.big_container_height  = 242
        self.y_pos =  399
        self.x_pos = int(1042/2)
        self.container_color = (247, 255, 247)
        # Using font initial
        pg.font.init()
        # Font
        self.text = text
        self.text_2 = text_2
        self.antialise = True
        self.font_colr = font_color
        # Font style
        self.ending_font_size = font_size
        self.font_style = pg.font.Font(font_style, self.ending_font_size)
        # Text Container
        self.text_container_width = self.font_style.size(self.text)[0] + 20
        self.text_container_height = (self.font_style.size(self.text)[1]*2) + 10
        # Container widther according to other widgets
        self.big_container_width = 336 + self.text_container_width

        self.image = pg.surface.Surface((self.big_container_width, self.big_container_height))
        self.image.fill(self.container_color)
        self.rect = self.image.get_rect(midtop = (self.x_pos, self.y_pos))

        # Image message
        self.image_message = pg.image.load(img).convert_alpha()
        self.image_message_rect = self.image_message.get_rect(topleft = (33, 4))
        self.image.blit(self.image_message, self.image_message_rect)

        # Making the Text container
        self.text_container = pg.surface.Surface((self.text_container_width, self.text_container_height))
        self.text_container.fill(self.container_color)
        self.text_container_rect = self.text_container.get_rect(midleft = (314, int(self.big_container_height/2)))

        # Text 1
        self.text_rendering = self.font_style.render(self.text, self.antialise, self.font_colr)
        self.text_pos = self.text_rendering.get_rect(midtop = (int(self.text_container.get_width()/2), 5))
        # Rendering the Text
        self.text_container.blit(self.text_rendering, self.text_pos)

        # Text 2
        self.text_rendering_2 = self.font_style.render(self.text_2, self.antialise, self.font_colr)
        self.text_pos_2 = self.text_rendering_2.get_rect(midtop = (int(self.text_container.get_width()/2), 40))
        # Rendering the Text
        self.text_container.blit(self.text_rendering_2, self.text_pos_2)

        # Putting the text container
        self.image.blit(self.text_container, self.text_container_rect)

exit_message_sprite = pg.sprite.Group()

