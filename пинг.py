from pygame import*
window = display.set_mode((600,600))
back = (14,6,56)
window.fill(back)

clock = time.Clock()
display.update()
clock.tick(60)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
            window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > - 50:
            self.rect.y -= self.speed
        if [K_s] and  self.rect.y < 520:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > - 50:
            self.rect.y -= self.speed
        if [K_DOWN] and  self.rect.y < 520:
            self.rect.y += self.speed