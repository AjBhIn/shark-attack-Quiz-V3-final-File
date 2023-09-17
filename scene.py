import pygame as pg

class Island(pg.sprite.Sprite):
    def __init__(self, img, placement):
        super().__init__()
        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(bottomright = placement)

    def update(self):
        pass

island_sprities = pg.sprite.Group()

class Ocean(pg.sprite.Sprite):
    def __init__(self, img, placement):
        super().__init__()
        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(bottomright = placement)

    def update(self):
        pass

ocean_sprities = pg.sprite.Group()


class Shark(pg.sprite.Sprite):
    def __init__(self, img, placement):
        super().__init__()
        self.placement = placement
        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(midright = self.placement)

    def update(self, x):
            self.rect.x = x - self.image.get_width()


shark_sprite = pg.sprite.Group()

class Swimmer(pg.sprite.Sprite):
    def __init__(self, img, placement):
        super().__init__()
        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(midright = placement)

    def update(self, x):
         self.rect.x = x - self.image.get_width()


swimmer_sprite = pg.sprite.GroupSingle()
