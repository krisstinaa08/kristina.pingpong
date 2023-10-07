from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Shooter Game')
background = transform.scale(image.load('fon08.jpg'), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed



speed_x = 3
speed_y = 3
finish = False

player1 = Player('krsk45.png', 0, 400, 2, 25, 150)
player2 = Player('krsk45.png', 680,400,2,25,150)
ball = GameSprite('krsk45.png', 250,400,1,80,80)

clock = time.Clock()
FPS = 360
RUN_GAME = True
run - True
Finish = False
font.init()
font1 = font.Font(None, 40)
lose1 = font1.render('PLAYER 1 LOSE!', True, (255,200,10))
lose2 = font1.render('PLAYER 2 LOSE!', True, (255,200,10))

while RUN_GAME:
    for e in event.get():
        if e.type == QUIT:
            RUN_GAME = False
    window.blit(background, (0,0))
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        player1.update_L()
        player2.update_R()
        player1.reset()
        player2.reset()
        player.reset()
        ball.update()
        ball.reset()

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x > win_width-50:
        finish = True
        window.blit(lose1, (200,200))

    display.update()
    clock.tick(FPS)
