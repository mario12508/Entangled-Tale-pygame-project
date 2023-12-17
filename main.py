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
        self.mask = pygame.mask.from_surface(self.image)

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
        self.loc = 0

    def update(self, move_up, move_down, move_left, move_right):
        global all_sprites, background, player, player_group, door_group, door
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
        if pygame.sprite.collide_mask(self, door):
            if self.loc == 0:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a1_m2.jpg', (600, 1300))
                all_sprites.add(background)
                player = PlayerAct1(285, 950)
                player.loc = 1
                wizardRus.rect.x = 285
                wizardRus.rect.y = 600
                wizardRus.canRun = False
                wizardRus.y = 600
                all_sprites.add(wizardRus)
                door = Door(260, 300)
            elif self.loc == 1:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a1_m3.jpg', (1300, 600))
                all_sprites.add(background)
                door = Door(80, 60)
                player = PlayerAct1(650, 300)
                player.loc = 2
            elif self.loc == 2:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                background = Background('a1_m4.jpg', (700, 500))
                all_sprites.add(background)
                player = PlayerAct1(375, 300)
                player.loc = 3
                mathGame()

        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)


def newDialog():
    font = pygame.font.Font(None, 30)
    t1 = font.render('', True, (255, 255, 255))
    t2 = font.render('', True, (255, 255, 255))
    t3 = font.render('', True, (255, 255, 255))
    return t1, t2, t3


def mathGame():
    global background, all_sprites, player_group, player, door, door_group
    fon = pygame.transform.scale(load_image('a1_m4.jpg'), (800, 500))
    screen.blit(fon, (0, 0))

    n1 = random.randint(0, 100)
    n3 = random.randint(0, 9)
    n2 = n3 - n1
    m = 'Я великий маг этого подземелья,'
    m2 = 'и я никому не дам ходить по нему'
    m3 = 'без моего разрешения!'
    screen.fill((0, 0, 0))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    t1, t2, t3 = newDialog()

    win = False
    i = 1
    a = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and a == 0:
                    screen.fill((0, 0, 0))
                    screen.blit(fon, (0, 0))
                    if n2 < 0:
                        m1 = f"{n1}{n2}"
                    else:
                        m1 = f"{n1}+{n2}"
                    m = 'Но ты можешь попытать удачу,'
                    m2 = 'и решить мою задачу'
                    m3 = 'сколько будет:' + m1
                    t1, t2, t3 = newDialog()
                    i = 1
                    a = 1
                elif 48 <= event.key <= 58 and a == 1:
                    m = event.key - 48
                    t1, t2, t3 = newDialog()
                    if m == n3:
                        screen.fill((0, 0, 0))
                        screen.blit(fon, (0, 0))
                        m = 'Я вижу, что ты силен в математике'
                        m2 = 'на этот раз я тебя пропукаю,'
                        m3 = 'но мы еще встретимся!'
                        win = True
                    else:
                        screen.fill((0, 0, 0))
                        screen.blit(fon, (0, 0))
                        m = 'Я вижу, что ты слаб,'
                        m2 = 'возвращайся,'
                        m3 = 'лишь когда будешь достоен'
                    i = 1
                    a = 2
                elif event.key == pygame.K_z and a == 2:
                    if win:
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
                        act1()
                        return

        if i <= len(m):
            t1 = font.render(m[:i], True, (255, 255, 255))
        elif i <= len(m) + len(m2):
            t2 = font.render(m2[:i - len(m)], True, (255, 255, 255))
        elif i <= len(m) + len(m2) + len(m3):
            t3 = font.render(m3[:i - len(m) - len(m2)], True, (255, 255, 255))
        i += 1
        screen.blit(t1, (230, 85))
        screen.blit(t2, (230, 115))
        screen.blit(t3, (230, 145))
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(20)
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


class Door(pygame.sprite.Sprite):
    image = load_image('exit-enter_a1.png', colorkey=-1)
    image = pygame.transform.scale(image, (140, 120))

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = Door.image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)


# группы спрайтов
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
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
    global all_sprites, player_group, player, background, door, door_group
    fon = pygame.transform.scale(load_image('act1.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    background = Background('a1_m1.jpg', (1360, 520))
    door = Door(1200, 200)
    all_sprites.add(background)
    door_group.add(door)
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
        door_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
