from pygame import *

back = (23, 45, 125)
window = display.set_mode((500, 500))

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -50:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 520:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > -50:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 520:
            self.rect.y += self.speed

game = True
finish = False

rocket1 = Player('андайн2.png', 0, 200, 5, 150, 300)
rocket2 = Player('андайн3.png', 350, 200, 5, 150, 300)
ball = Player('душа.png', 175, 300, 5, 125, 75)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Игрок 1 проиграл!', True, (180, 0, 0))
lose2 = font.render('Игрок 2 проиграл!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rocket1.update_l()
        rocket2.update_r()
        rocket1.reset()
        rocket2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = True
        if ball.rect.x > 450:
            finish = True
            window.blit(lose2, (200, 200))
            game = True

    display.update()
    clock.tick(60)


