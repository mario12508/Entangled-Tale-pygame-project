import os
import random

import pygame
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Player(pygame.sprite.Sprite):
    image = load_image('m.c.front_stop.jpg')
    image = pygame.transform.scale(image, (40, 60))

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect().move(
            pos_x, pos_y)
        self.x = pos_x + 20
        self.y = pos_y + 60
        self.step = 1
        self.back = False
        self.last_skin_change_time = 0
        self.direction = ''

    def stop(self):
        image = self.image
        if self.direction == 'left':
            image = load_image(f'm.c.left_stop.jpg')
        elif self.direction == 'right':
            image = load_image(f'm.c.right_stop.jpg')
        elif self.direction == 'down':
            image = load_image(f'm.c.front_stop.jpg')
        elif self.direction == 'up':
            image = load_image(f'm.c.back_stop.jpg')
        self.image = pygame.transform.scale(image, (40, 60))


class PlayerAct1(Player):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)

    def update(self, move_up, move_down, move_left, move_right):
        global all_sprites, background, player, player_group
        image = self.image
        current_time = pygame.time.get_ticks()
        if move_left:
            self.direction = 'left'
            self.rect.x -= 6
            self.x -= 6
            if background.get_rgb(self.x, self.y) == (2, 0, 0):
                self.rect.x += 6
                self.x += 6
            if current_time - self.last_skin_change_time > 150:
                self.last_skin_change_time = current_time
                if self.step == 1:
                    self.step += 1
                    self.back = False
                elif self.step == 2:
                    if self.back:
                        self.step -= 1
                    else:
                        self.step += 1
                elif self.step == 3:
                    self.step -= 1
                    self.back = True

            image = load_image(f'm.c.left_walk_{self.step}.jpg')
        if move_right:
            self.direction = 'right'
            self.rect.x += 6
            self.x += 6
            if background.get_rgb(self.x, self.y) == (2, 0, 0):
                self.rect.x -= 6
                self.x -= 6
            if current_time - self.last_skin_change_time > 150:
                self.last_skin_change_time = current_time
                if self.step == 1:
                    self.step += 1
                    self.back = False
                elif self.step == 2:
                    if self.back:
                        self.step -= 1
                    else:
                        self.step += 1
                elif self.step == 3:
                    self.step -= 1
                    self.back = True

            image = load_image(f'm.c.right_walk_{self.step}.jpg')
        if move_up:
            self.direction = 'up'
            self.rect.y -= 6
            self.y -= 6
            if background.get_rgb(self.x, self.y) == (2, 0, 0):
                self.rect.y += 6
                self.y += 6
            if current_time - self.last_skin_change_time > 150:
                self.last_skin_change_time = current_time
                if self.step == 1:
                    self.step += 1
                    self.back = False
                elif self.step == 2:
                    if self.back:
                        self.step -= 1
                    else:
                        self.step += 1
                elif self.step == 3:
                    self.step -= 1
                    self.back = True

            image = load_image(f'm.c.back_walk_{self.step}.jpg')
        if move_down:
            self.direction = 'down'
            self.rect.y += 6
            self.y += 6
            if background.get_rgb(self.x, self.y) == (2, 0, 0):
                self.rect.y -= 6
                self.y -= 6
            if current_time - self.last_skin_change_time > 150:
                self.last_skin_change_time = current_time
                if self.step == 1:
                    self.step += 1
                    self.back = False
                elif self.step == 2:
                    if self.back:
                        self.step -= 1
                    else:
                        self.step += 1
                elif self.step == 3:
                    self.step -= 1
                    self.back = True

            image = load_image(f'm.c.front_walk_{self.step}.jpg')
        self.image = pygame.transform.scale(image, (40, 60))
        if background.get_rgb(self.x, self.y) == (10, 0, 0):
            all_sprites = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            background = Background('a1_m2.jpg', (600, 1300))
            all_sprites.add(background)
            player = PlayerAct1(285, 950)
            wizardRus.rect.x = 300
            wizardRus.rect.y = 600
            wizardRus.canRun = False
            wizardRus.y = 600
            all_sprites.add(wizardRus)
        elif background.get_rgb(self.x, self.y) == (9, 0, 0):
            all_sprites = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            background = Background('a1_m3.jpg', (1300, 600))
            all_sprites.add(background)
            player = PlayerAct1(750, 500)
        elif background.get_rgb(self.x, self.y) == (8, 0, 0):
            all_sprites = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            background = Background('a1_m4.jpg', (700, 500))
            all_sprites.add(background)
            player = PlayerAct1(375, 300)
            mathGame()

        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)


def printTextMag(m, y=0):
    m2 = ''
    font = pygame.font.Font(None, 30)
    for i in m:
        m2 += i
        t = font.render(m2, True, (255, 255, 255))
        screen.blit(t, (230, 85 + y))
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(15)


def mathGame():
    global background, all_sprites, player_group, player
    fon = pygame.transform.scale(load_image('a1_m4.jpg'), (800, 500))
    screen.blit(fon, (0, 0))
    printTextMag('Я великий маг этого подземелья,')
    printTextMag('и я никому не дам ходить по нему', y=30)
    printTextMag('без моего разрешения!', y=60)
    clock.tick(FPS // 4)
    screen.fill((0, 0, 0))
    screen.blit(fon, (0, 0))
    printTextMag('Но ты можешь попытать удачу,')
    printTextMag('и решить мою задачу', y=30)
    printTextMag('сколько будет:', y=60)

    n1 = random.randint(0, 100)
    n3 = random.randint(0, 9)
    n2 = n3 - n1
    if n2 < 0:
        m = f"{n1}{n2}"
    else:
        m = f"{n1}+{n2}"
    printTextMag(m, y=90)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                m = event.key - 48
                if m == n3:
                    screen.fill((0, 0, 0))
                    screen.blit(fon, (0, 0))
                    printTextMag('Я вижу, что ты силен в математике')
                    printTextMag('на этот раз я тебя пропукаю,', y=30)
                    printTextMag('но мы еще встретимся!', y=60)
                    clock.tick(FPS // 4)
                    all_sprites = pygame.sprite.Group()
                    player_group = pygame.sprite.Group()
                    background = Background('a1_m5.jpg', (1200, 700))
                    all_sprites.add(background)
                    player = PlayerAct1(600, 450)
                    camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
                    return
                else:
                    screen.fill((0, 0, 0))
                    screen.blit(fon, (0, 0))
                    printTextMag('Я вижу, что ты слаб,')
                    printTextMag('возвращайся,', y=30)
                    printTextMag('лишь когда будешь достоен', y=60)
                    clock.tick(FPS // 4)
                    act1()
                    all_sprites = pygame.sprite.Group()
                    player_group = pygame.sprite.Group()
                    background = Background('a1_m1.jpg', (1360, 520))
                    all_sprites.add(background)
                    player = PlayerAct1(400, 100)
                    camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
                    return
        clock.tick(FPS)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_path, size):
        super().__init__()
        self.image = load_image(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

    def get_rgb(self, x, y):
        pixel = pygame.PixelArray(self.image)
        return self.image.unmap_rgb(pixel[x][y])


clock = pygame.time.Clock()
FPS = 60


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(0.7)
    fon = pygame.transform.scale(load_image('blackfon.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.KEYDOWN or event.type ==
                  pygame.MOUSEBUTTONDOWN):
                if True:
                    act1()
                    return
        clock.tick(FPS)


# группы спрайтов
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
background = Background('a1_m1.jpg', (1360, 520))
all_sprites.add(background)
player = Player(400, 100)


class wizardRus(pygame.sprite.Sprite):
    image = load_image('wizardRus.jpg')
    image = pygame.transform.scale(image, (80, 90))

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = wizardRus.image
        self.rect = self.image.get_rect().move(
            pos_x, pos_y)
        self.canRun = False
        self.y = pos_y

    def update(self):
        if self.canRun:
            self.rect.y -= 10
            self.y -= 10
            if self.y <= 300:
                self.rect.y = -1000
        if player.y <= 800:
            self.canRun = True


wizardRus = wizardRus(2000, 2000)


def act1():
    global all_sprites, player_group, player, background
    fon = pygame.transform.scale(load_image('act1.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    background = Background('a1_m1.jpg', (1360, 520))
    all_sprites.add(background)
    player = PlayerAct1(400, 100)


def act2():
    fon = pygame.transform.scale(load_image('act2.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)


def act3():
    fon = pygame.transform.scale(load_image('act3.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)


def menu():
    fon = pygame.transform.scale(load_image('Menu.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    act1()
                    return
                if event.key == pygame.K_2:
                    act2()
                    return
                if event.key == pygame.K_3:
                    act3()
                    return
                if event.key == pygame.K_p:
                    return

        clock.tick(FPS)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


camera = Camera()
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Entangled Tale')
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    start_screen()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    menu()
            if event.type == pygame.KEYUP:
                player.stop()
        keys = pygame.key.get_pressed()

        screen.fill((0, 0, 0))
        # Обновление игровых объектов
        player.update(keys[pygame.K_UP], keys[pygame.K_DOWN],
                      keys[pygame.K_LEFT], keys[pygame.K_RIGHT])
        player.update(keys[pygame.K_w], keys[pygame.K_s],
                      keys[pygame.K_a], keys[pygame.K_d])
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        camera.update(player)
        wizardRus.update()
        all_sprites.draw(screen)
        player_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
