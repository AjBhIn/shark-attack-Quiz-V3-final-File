import pygame as pg

class Scene(pg.sprite.Sprite):
    def __init__(self, img, placement):
        super().__init__()
        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(bottomright = placement)

    def update(self):
        pass

scene_sprities = pg.sprite.Group()


class Shark(pg.sprite.Sprite):
    def __init__(self, img, placement):
        super().__init__()
        self.placement = placement
        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(midright = self.placement)

    def update(self, x):
            self.rect.x = x - self.image.get_width()
            print(self.rect.x)


shark_sprite = pg.sprite.GroupSingle()

class Swimmer(pg.sprite.Sprite):
    def __init__(self, img, placement):
        super().__init__()
        self.image = pg.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(midright = placement)

    def update(self, x):
         self.rect.x = x - self.image.get_width()


swimmer_sprite = pg.sprite.GroupSingle()
