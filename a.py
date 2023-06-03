from pygame import*
window = display.set_mode((600,600))
back = (14,6,56)
window.fill(back)

clock = time.Clock()


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

game = True
finif = False

speed_x = 3
speed_y = 3

rocket1 = Player('андайн2.png', 20,250,5,100,200)
rocket2 = Player('андайн3.png', 400,250,5,100,200)
ball = Player('душа.png',250,250,5,50,50)
while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finif != True:
        rocket1.reset()
        rocket2.reset()
        ball.reset()
        rocket1.update_l()
        rocket2.update_r()
    display.update()
    clock.tick(60)



font.init()
font = font.Font(None,50)
lose1 = font.render('1 игрок проиграл', True,(150,7,34))
lose2 = font.render('2 игрок проиграл', True,(150,7,34))


    