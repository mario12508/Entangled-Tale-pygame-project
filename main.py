import datetime
import os
import random
import sys

import pygame
import sqlite3


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


def newDialog():
    font_path = os.path.join("data/fonts", "comic.ttf")
    font = pygame.font.Font(font_path, 20)
    render_fraze_1 = font.render('', True, (255, 255, 255))
    render_fraze_2 = font.render('', True, (255, 255, 255))
    render_fraze_3 = font.render('', True, (255, 255, 255))
    return render_fraze_1, render_fraze_2, render_fraze_3


def mathGame(m):
    global background, all_sprites, player_group, player, door, \
        door_group, rectangle_group, loc5, loc11, loc14, x, y
    if player.loc == 10:
        fon = pygame.transform.scale(load_image(m), (800, 505))
    else:
        fon = pygame.transform.scale(load_image(m), (800, 505))
    screen.blit(fon, (0, 0))

    a = random.randint(0, 100)
    difference = random.randint(0, 9)
    b = difference - a
    if m == 'a1_m4.png':
        fraze_1 = 'Я великий маг этого подземелья,'
        fraze_2 = 'и я никому не дам ходить по нему'
        fraze_3 = 'без моего разрешения!'
    elif m == 'a2_m5.png':
        fraze_1 = 'Вот мы снова встретились,'
        fraze_2 = 'и в этот раз ты в моем лесу'
        fraze_3 = 'дальше я тебя не пропущу!'
    else:
        fraze_1 = 'Вот мы снова встретились,'
        fraze_2 = 'и в этот раз ты далеко прошел'
        fraze_3 = 'дальше я тебя не уйдешь!'

    if player.loc <= 5:
        screen.fill((2, 0, 0))
    elif 5 < player.loc <= 12:
        screen.fill((34, 177, 76))
    else:
        screen.fill((153, 217, 234))
    screen.blit(fon, (0, 0))
    font_path = os.path.join("data/fonts", "comic.ttf")
    font = pygame.font.Font(font_path, 20)
    render_fraze_1, render_fraze_2, render_fraze_3 = newDialog()

    win = False
    i = 1
    k = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_z or event.key == pygame.K_RETURN)
                        and k == 0):
                    if player.loc <= 5:
                        screen.fill((2, 0, 0))
                    elif 5 < player.loc <= 12:
                        screen.fill((34, 177, 76))
                    else:
                        screen.fill((153, 217, 234))
                    screen.blit(fon, (0, 0))
                    if b < 0:
                        question = f"{a}{b}"
                    else:
                        question = f"{a} + {b}"
                    fraze_1 = 'Но ты можешь попытать удачу,'
                    fraze_2 = 'и решить мою задачу'
                    fraze_3 = 'сколько будет: ' + question
                    render_fraze_1, render_fraze_2, render_fraze_3 = (
                        newDialog())
                    i = 1
                    k = 1
                elif 48 <= event.key <= 58 and k == 1:
                    fraze_1 = event.key - 48
                    render_fraze_1, render_fraze_2, render_fraze_3 = (
                        newDialog())
                    if fraze_1 == difference:
                        if player.loc <= 5:
                            screen.fill((2, 0, 0))
                        elif 5 < player.loc <= 12:
                            screen.fill((34, 177, 76))
                        else:
                            screen.fill((153, 217, 234))
                        screen.blit(fon, (0, 0))
                        if m == 'a1_m4.png':
                            fraze_1 = 'Я вижу, что ты неплох в математике'
                            fraze_2 = 'на этот раз я тебя пропускаю,'
                            fraze_3 = 'но мы еще встретимся!'
                        elif m == 'a2_m5.png':
                            fraze_1 = 'Я вижу, что ты до сих пор неплох в \
                                       математике'
                            fraze_2 = 'в этот раз я тебя пропускаю,'
                            fraze_3 = 'но еще одна наша встреча неизбежна!'
                        else:
                            fraze_1 = 'Я вижу, что ты также силен в математике'
                            fraze_2 = 'на этот раз покажи себя в равном бою,'
                            fraze_3 = 'с истинным магом!'
                        win = True
                    else:
                        if player.loc <= 5:
                            screen.fill((2, 0, 0))
                        elif 5 < player.loc <= 12:
                            screen.fill((34, 177, 76))
                        else:
                            screen.fill((153, 217, 234))
                        screen.blit(fon, (0, 0))
                        fraze_1 = 'Я вижу, что ты слаб,'
                        fraze_2 = 'возвращайся,'
                        fraze_3 = 'лишь когда будешь достоин'
                    i = 1
                    k = 2
                elif ((event.key == pygame.K_z or event.key == pygame.K_RETURN)
                      and k == 2):
                    if win:
                        if m == 'a1_m4.png':
                            all_sprites = pygame.sprite.Group()
                            player_group = pygame.sprite.Group()
                            rectangle_group = pygame.sprite.Group()
                            background = Background('a1_m5.png', (839, 1300))
                            all_sprites.add(background)
                            sign1.rect.y = 1000
                            sign2.rect.y = 1000
                            sign3.rect.y = 700
                            sign4.rect.y = 700
                            sign5.rect.y = 400
                            sign6.rect.y = 400
                            all_sprites.add(sign1, sign2, sign3, sign4, sign5,
                                            sign6)
                            sign_group.add(sign1, sign2, sign3, sign4, sign5,
                                           sign6)
                            player = Player(419, 1100, 1)
                            door = Door(362, 30, 1, 2)
                            player.loc = 3
                            loc5 = 0
                        elif m == 'a2_m5.png':
                            all_sprites = pygame.sprite.Group()
                            player_group = pygame.sprite.Group()
                            rectangle_group = pygame.sprite.Group()
                            background = Background('a2_m6.png', (1667, 1000))
                            all_sprites.add(background)
                            player = Player(850, 506, 2)
                            player.loc = 11
                            door.rect.x = 20000
                            door2.rect.x = 20000
                            door3.rect.x = 20000
                            x = player.x
                            y = player.y
                            loc11 = 0
                            pygame.mixer.music.load("data/"
                                                    "mus_undynetruetheme.ogg")
                            pygame.mixer.music.set_volume(0.3)
                            pygame.mixer.music.play(loops=-1)
                        else:
                            all_sprites = pygame.sprite.Group()
                            player_group = pygame.sprite.Group()
                            rectangle_group = pygame.sprite.Group()
                            background = Background('a3_m3.jpg', (2210, 1300))
                            all_sprites.add(background)
                            player = Player(1105, 650, 3)
                            player.loc = 15
                            door.rect.x = 20000
                            x = player.x
                            y = player.y
                            loc14 = 0
                            pygame.mixer.music.load("data/act3_boss.ogg")
                            pygame.mixer.music.set_volume(0.3)
                            pygame.mixer.music.play(loops=-1)
                        camera.update(player)
                        for sprite in all_sprites:
                            camera.apply(sprite)
                        return
                    else:
                        if m == 'a1_m4.png':
                            end_screen(1, False)
                        elif m == 'a2_m5.png':
                            end_screen(2, False)
                        else:
                            end_screen(3, False)
                        return

        if i <= len(fraze_1):
            render_fraze_1 = font.render(fraze_1[:i], True, (255, 255, 255))
        elif i <= len(fraze_1) + len(fraze_2):
            render_fraze_2 = font.render(fraze_2[:i - len(fraze_1)], True,
                                         (255, 255, 255))
        elif i <= len(fraze_1) + len(fraze_2) + len(fraze_3):
            render_fraze_3 = font.render(
                fraze_3[:i - len(fraze_1) - len(fraze_2)], True,
                (255, 255, 255))
        i += 1
        if m == 'a1_m4.png':
            screen.blit(render_fraze_1, (230, 85))
            screen.blit(render_fraze_2, (230, 115))
            screen.blit(render_fraze_3, (230, 145))
        elif m == 'a2_m5.png':
            screen.blit(render_fraze_1, (250, 33))
            screen.blit(render_fraze_2, (250, 51))
            screen.blit(render_fraze_3, (250, 69))
        else:
            screen.blit(render_fraze_1, (230, 85))
            screen.blit(render_fraze_2, (230, 115))
            screen.blit(render_fraze_3, (230, 145))
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(20)
        clock.tick(FPS)


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


def end_screen(n, winOrdie):
    fon = pygame.transform.scale(load_image('gameover.jpg'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.display.flip()

    font_path = os.path.join("data/fonts", "comic.ttf")
    font = pygame.font.Font(font_path, 35)
    tm = (datetime.datetime.now() - time).total_seconds()
    t2 = font.render(f"{int(tm // 60)} min {int(tm - (tm // 60) * 60)} sec",
                     True, (0, 0, 0))

    if winOrdie:
        t = font.render(f"Win", True, (0, 0, 0))
        font = pygame.font.Font(font_path, 50)
        t0 = font.render(f"{n} Act", True, (0, 0, 0))

        con = sqlite3.connect("data/bd.sqlite")
        cur = con.cursor()
        cur.execute(
            f"INSERT INTO player(act, time) VALUES({n - 1}, '{int(tm // 60)} "
            f"min {int(tm - (tm // 60) * 60)} sec')")
        con.commit()
        con.close()
    else:
        t = font.render(f"Lose", True, (0, 0, 0))
        font = pygame.font.Font(font_path, 50)
        t0 = font.render(f"{n} Act", True, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.KEYDOWN or event.type ==
                  pygame.MOUSEBUTTONDOWN):
                if True:
                    if n == 1:
                        act1()
                    elif n == 2:
                        act2()
                    elif n == 3:
                        act3()
                    else:
                        sybtit_screen()
                        results()
                        act1()
                    return

        screen.blit(t0, (300, 100))
        screen.blit(t, (300, 200))
        screen.blit(t2, (300, 300))
        pygame.display.flip()
        clock.tick(FPS)


def act1():
    global all_sprites, player_group, player, background, door, door_group, \
        i, word_group, x, y, loc5, time, runi
    time = datetime.datetime.now()
    fon = pygame.transform.scale(load_image('act1.png'), (800, 500))
    pygame.mixer.music.load("data/start_sound.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)

    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    background = Background('a1_m1.png', (1360, 760))
    door = Door(1180, 440, 1, 1)
    all_sprites.add(background)
    door_group.add(door)
    pygame.mixer.music.load("data/act1_main.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    player = Player(290, 470, 1)
    word_group = pygame.sprite.Group()
    x, y = 0, 0
    loc5 = 0
    i = 0
    runi = -600
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)

    screen.blit(pygame.transform.scale(load_image("run.png"), (40, 40)),
                (5, 5))
    font_path = os.path.join("data/fonts", "comic.ttf")
    txt = pygame.font.Font(font_path, 35).render(f"active", True,
                                                 (255, 0, 0))
    screen.blit(txt, (50, 0))
    all_sprites.draw(screen)


def act2():
    global all_sprites, player_group, player, background, door, \
        door_group, time, x, y, door2, door3, pas, loc11, img, runi
    time = datetime.datetime.now()
    fon = pygame.transform.scale(load_image('act2.png'), (800, 500))
    pygame.mixer.music.load("data/start_sound.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)

    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    background = Background('a2_m1.png', (2060, 1500))
    door = Door(350, 840, 2, 1)
    door2 = Door(1528, 540, 2, 1)
    door3 = Door(350, 540, 2, 1)
    all_sprites.add(background)
    door_group.add(door, door2, door3)
    pas = Pass(850, 700)
    img = load_image('key.jpg')
    img = pygame.transform.scale(img, (50, 50))
    pygame.mixer.music.load("data/a2_m1.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    x, y = 0, 0
    loc11 = 0
    runi = -600
    player = Player(730, 730, 2)
    player.loc = 6
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)

    screen.blit(pygame.transform.scale(load_image("run.png"), (40, 40)),
                (5, 5))
    font_path = os.path.join("data/fonts", "comic.ttf")
    txt = pygame.font.Font(font_path, 35).render(f"active", True,
                                                 (255, 0, 0))
    screen.blit(txt, (50, 0))
    all_sprites.draw(screen)
    door_group.draw(screen)


def act3():
    global all_sprites, player_group, player, background, door, door_group, \
        i, x, y, time, defen, traveler, apples, runi
    fon = pygame.transform.scale(load_image('act3.png'), (800, 500))
    screen.blit(fon, (0, 0))
    pygame.mixer.music.load("data/start_sound.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    pygame.display.flip()
    clock.tick(1)

    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    background = Background('a3_m1.jpg', (10000, 6000))
    all_sprites.add(background)
    pygame.mixer.music.load("data/act3_main.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    door = Door(1950, 2750, 1, 1)
    door_group.add(door)
    player = Player(1650, 1200, 3)
    traveler = Traveler(5000, 3600)
    player.loc = 13
    runi = -600
    defen = Defens(2350, 2450)
    apples = [
        Apple(6000, 3000),
        Apple(6400, 2500),
        Apple(4800, 3000),
        Apple(6100, 1900),
        Apple(8000, 2800)
    ]

    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)

    screen.blit(pygame.transform.scale(load_image("run.png"), (40, 40)),
                (5, 5))
    font_path = os.path.join("data/fonts", "comic.ttf")
    txt = pygame.font.Font(font_path, 35).render(f"active", True,
                                                 (255, 0, 0))
    screen.blit(txt, (50, 0))
    all_sprites.draw(screen)


t1 = None
t2 = None
t3 = None
t4 = None
t5 = None


def other_color(cl1, cl2, cl3, cl4, cl5):
    global t1, t2, t3, t4, t5
    font_path = os.path.join("data/fonts", "comic.ttf")
    font = pygame.font.Font(font_path, 40)
    t1 = font.render(f"1 Act",
                     True, cl1)
    t2 = font.render(f"2 Act",
                     True, cl2)
    t3 = font.render(f"3 Act",
                     True, cl3)
    t4 = font.render(f"Tab result",
                     True, cl4)
    t5 = font.render(f"Cancel",
                     True, cl5)


def menu():
    con = sqlite3.connect("data/bd.sqlite")
    cur = con.cursor()
    result1 = cur.execute("""SELECT id FROM player
            WHERE act == 1""").fetchall()
    result2 = cur.execute("""SELECT id FROM player
            WHERE act == 2""").fetchall()
    con.close()
    COLOR1 = (64, 64, 64)
    COLOR2 = (255, 0, 0)
    COLOR3 = (0, 0, 0)

    other_color(COLOR1, COLOR1, COLOR1, COLOR1, COLOR2)
    colT = 5
    pygame.mixer.music.pause()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    colT -= 1
                    if colT == 0:
                        colT = 5
                        other_color(COLOR1, COLOR1, COLOR1, COLOR1,
                                    COLOR2)
                    if colT == 1:
                        other_color(COLOR2, COLOR1, COLOR1,
                                    COLOR1, COLOR1)
                    if colT == 2:
                        if result1:
                            other_color(COLOR1, COLOR2, COLOR1,
                                        COLOR1, COLOR1)
                        else:
                            other_color(COLOR1, COLOR3, COLOR1,
                                        COLOR1, COLOR1)
                    if colT == 3:
                        if result2:
                            other_color(COLOR1, COLOR1, COLOR2,
                                        COLOR1, COLOR1)
                        else:
                            other_color(COLOR1, COLOR1, COLOR3,
                                        COLOR1, COLOR1)
                    if colT == 4:
                        other_color(COLOR1, COLOR1, COLOR1,
                                    COLOR2, COLOR1)

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    colT += 1
                    if colT == 6:
                        colT = 1
                        other_color(COLOR2, COLOR1, COLOR1,
                                    COLOR1, COLOR1)
                    if colT == 5:
                        other_color(COLOR1, COLOR1, COLOR1, COLOR1,
                                    COLOR2)
                    if colT == 2:
                        if result1:
                            other_color(COLOR1, COLOR2, COLOR1,
                                        COLOR1, COLOR1)
                        else:
                            other_color(COLOR1, COLOR3, COLOR1,
                                        COLOR1, COLOR1)
                    if colT == 3:
                        if result2:
                            other_color(COLOR1, COLOR1, COLOR2,
                                        COLOR1, COLOR1)
                        else:
                            other_color(COLOR1, COLOR1, COLOR3,
                                        COLOR1, COLOR1)
                    if colT == 4:
                        other_color(COLOR1, COLOR1, COLOR1,
                                    COLOR2, COLOR1)

                if (event.key == pygame.K_SPACE or event.key == pygame.K_p or
                        event.key == pygame.K_RETURN):
                    if colT == 1:
                        act1()
                    if colT == 2:
                        if result1:
                            act2()
                    if colT == 3:
                        if result2:
                            act3()
                    if colT == 4:
                        results()
                    pygame.mixer.music.play(loops=-1)
                    return

        screen.blit(t1, (300, 50))
        screen.blit(t2, (300, 130))
        screen.blit(t3, (300, 210))
        screen.blit(t4, (300, 290))
        screen.blit(t5, (300, 370))
        pygame.display.flip()
        clock.tick(FPS)


class Player(pygame.sprite.Sprite):
    image = load_image('m.c.front_stop.png')
    image = pygame.transform.scale(image, (40, 60))

    def __init__(self, pos_x, pos_y, stena, key=False, pas=False):
        super().__init__(player_group, all_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.x = pos_x + 20
        self.y = pos_y + 60
        self.step = 1
        self.back = False
        self.last_skin_change_time = 0
        self.direction = ''
        self.mask = pygame.mask.from_surface(self.image)
        self.loc = 0
        self.key = key
        self.pas = pas
        self.run = 5
        self.vis = True
        self.appls = 0
        if stena == 1:
            self.stena = [(2, 0, 0)]
        elif stena == 2:
            self.stena = [(34, 177, 76), (0, 162, 232), (54, 19, 11),
                          (0, 8, 4), (4, 28, 16), (15, 69, 10), (18, 89, 22)]
        elif stena == 3:
            self.stena = [(153, 217, 234), (185, 122, 87), (0, 162, 232),
                          (187, 122, 87)]

    def stop(self):
        image = self.image
        if self.vis:
            if self.direction == 'left':
                image = load_image(f'm.c.left_stop.png')
            elif self.direction == 'right':
                image = load_image(f'm.c.right_stop.png')
            elif self.direction == 'down':
                image = load_image(f'm.c.front_stop.png')
            elif self.direction == 'up':
                image = load_image(f'm.c.back_stop.png')
        else:
            image = load_image(f'm.v.jpg')
        self.image = pygame.transform.scale(image, (40, 60))

    def update(self, move_up, move_down, move_left, move_right, passaa=None):
        global all_sprites, background, player, player_group, door_group, \
            door, word_group, x, y, task_text, ok_tip, door2, door3, \
            chest, img, pas, rectangle_group, loc5, loc11, text1, text2, \
            text3, text4
        image = self.image
        current_time = pygame.time.get_ticks()

        if move_left:
            self.direction = 'left'
            self.rect.x -= self.run
            self.x -= self.run
            if background.get_rgb(self.x, self.y) in self.stena:
                self.rect.x += self.run
                self.x += self.run
            if self.vis:
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

                image = load_image(f'm.c.left_walk_{self.step}.png')
            else:
                image = load_image(f'm.v.jpg')
        if move_right:
            self.direction = 'right'
            self.rect.x += self.run
            self.x += self.run
            if background.get_rgb(self.x, self.y) in self.stena:
                self.rect.x -= self.run
                self.x -= self.run
            if self.vis:
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

                image = load_image(f'm.c.right_walk_{self.step}.png')
            else:
                image = load_image(f'm.v.jpg')
        if move_up:
            self.direction = 'up'
            self.rect.y -= self.run
            self.y -= self.run
            if background.get_rgb(self.x, self.y) in self.stena:
                self.rect.y += self.run
                self.y += self.run
            if self.vis:
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

                image = load_image(f'm.c.back_walk_{self.step}.png')
            else:
                image = load_image(f'm.v.jpg')
        if move_down:
            self.direction = 'down'
            self.rect.y += self.run
            self.y += self.run
            if background.get_rgb(self.x, self.y) in self.stena:
                self.rect.y -= self.run
                self.y -= self.run
            if self.vis:
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

                image = load_image(f'm.c.front_walk_{self.step}.png')
            else:
                image = load_image(f'm.v.jpg')
        self.image = pygame.transform.scale(image, (40, 60))
        if pygame.sprite.collide_mask(self, door):
            if self.loc == 0:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a1_m2.png', (839, 1300))
                all_sprites.add(background)
                player = Player(419, 950, 1)
                player.loc = 1
                wizardRus.rect.x = 419
                wizardRus.rect.y = 600
                wizardRus.canRun = False
                wizardRus.y = 600
                all_sprites.add(wizardRus)
                door = Door(363, 48, 1, 2)
            elif self.loc == 1:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                word_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a1_m3.png', (2100, 500))
                all_sprites.add(background)
                door = Door(1800, 200, 1, 1)
                player = Player(200, 330, 1)
                player.loc = 2
            elif self.loc == 2:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                background = Background('a1_m4.png', (700, 500))
                all_sprites.add(background)
                player = Player(385, 300, 1)
                player.loc = 3
                mathGame('a1_m4.png')
            elif self.loc == 3:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                rectangle_group = pygame.sprite.Group()
                background = Background('a1_m6.png', (900, 784))
                all_sprites.add(background)
                pygame.mixer.music.load("data/act1_boss.ogg")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(loops=-1)
                player = Player(450, 300, 1)
                player.loc = 4
                x = player.x
                y = player.y

                loc5 = 0
                door = Door(20000, 20000, 1, 1)
            elif self.loc == 5:
                door.rect.x = 20000
                self.loc = 6
                end_screen(2, True)
            elif self.loc == 6 or self.loc == 9:
                a = ['Птица', "Медведь", "Заяц", "Человек"]
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                word_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a2_m2.png', (2380, 1500))
                all_sprites.add(background)
                door = Door(1670, 750, 2, 1)
                for j in range(1, 5):
                    button_group.add(Button(775 + j * 150, 800, j))
                player = Player(1600, 750, 2, key=player.key, pas=player.pas)
                font_path = os.path.join("data/fonts", "comic.ttf")
                font = pygame.font.Font(font_path, 50)
                ok_tip = random.randint(0, 3)
                task_text = font.render(a[ok_tip], True, (255, 255, 255))
                x, y = 700, 640
                player.loc = 7
            elif self.loc == 7:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a2_m1.png', (2060, 1500))
                door = Door(350, 840, 2, 1)
                door2 = Door(1528, 540, 2, 1)
                door3 = Door(350, 540, 2, 1)
                all_sprites.add(background)
                door_group.add(door, door2, door3)
                pas = Pass(850, 700)
                player = Player(480, 840, 2, key=player.key, pas=player.pas)
                player.loc = 6
            elif self.loc == 12:
                door.rect.x = 20000
                self.loc = 13
                end_screen(3, True)
            elif self.loc == 13:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                background = Background('a3_m2.jpg', (750, 400))
                all_sprites.add(background)
                player = Player(385, 300, 1)
                player.loc = 14
                mathGame('a3_m2.jpg')
            elif self.loc == 16:
                door.rect.x = 20000
                self.loc = 17
                end_screen(4, True)
        for j in apples:
            if pygame.sprite.collide_mask(self, j):
                j.rect.x = 20000
                player.appls += 1
                img = load_image('apple.jpg')
                img = pygame.transform.scale(img, (30, 30))

        if pygame.sprite.collide_mask(self, door3):
            if self.loc == 6 or self.loc == 9:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                word_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a2_m3.png', (4000, 4000))
                all_sprites.add(background)
                chest = Chest(777, 742)
                door3 = Door(3450, 810, 2, 1)
                player = Player(3360, 800, 2, key=player.key, pas=player.pas)
                x, y = 700, 640
                player.loc = 8
            elif self.loc == 8:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a2_m1.png', (2060, 1500))
                door = Door(350, 840, 2, 1)
                door2 = Door(1528, 540, 2, 1)
                door3 = Door(350, 540, 2, 1)
                all_sprites.add(background)
                door_group.add(door, door2, door3)
                pas = Pass(850, 700)
                player = Player(480, 540, 2, key=player.key, pas=player.pas)
                player.loc = 6
        if pygame.sprite.collide_mask(self, chest) and self.loc != 9:
            if player.key:
                player.pas = True
                img = load_image('cash.jpg')
                img = pygame.transform.scale(img, (50, 50))
                chest.image = pygame.transform.scale(
                    load_image('chest_open.jpg'), (60, 40))
        if player.appls == 6 and background.get_rgb(self.x + self.run,
                                                    self.y + self.run) == \
                (0, 162, 232):
            player.vis = False
            try:
                del self.stena[self.stena.index((187, 122, 87))]
            except Exception:
                pass

        if pygame.sprite.collide_mask(self, pas) and self.loc != 9:
            if player.pas:
                all_sprites = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                door_group = pygame.sprite.Group()
                background = Background('a2_m4.png', (2060, 1500))
                pas = Pass(850, 600)
                door = Door(350, 840, 2, 1)
                door2 = Door(1528, 540, 2, 1)
                door3 = Door(350, 540, 2, 1)
                all_sprites.add(background)
                door_group.add(door)
                door_group.add(door2)
                door_group.add(door3)
                pas = Pass(840, 650)
                player = Player(player.x, player.y, 2)
                player.loc = 9
        if pygame.sprite.collide_mask(self, door2):
            all_sprites = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            background = Background('a1_m4.png', (750, 400))
            all_sprites.add(background)
            player = Player(335, 325, 1)
            player.loc = 10
            mathGame('a2_m5.png')
        if pygame.sprite.collide_mask(self, sign1):
            font_path = os.path.join("data/fonts", "comic.ttf")
            font = pygame.font.Font(font_path, 20)
            text1 = font.render('Лучше дальше не идти, это ОПАСНО!!!', False,
                                (255, 255, 255))
            text2 = font.render(
                'Это один из лучших магов наук. Он знает ВСЕ науки!', False,
                (255, 255, 255))
            text3 = font.render(
                'Он тоже не знает как сюда попал, но глупых детей он',
                False, (255, 255, 255))
            text4 = font.render('НИКОГДА не щадил!!!', False,
                                (255, 255, 255))
        elif pygame.sprite.collide_mask(self, sign2):
            font_path = os.path.join("data/fonts", "comic.ttf")
            font = pygame.font.Font(font_path, 20)
            text1 = font.render('Эти ворота скрывают ТЕБЯ от НЕГО!', False,
                                (255, 255, 255))
            text2 = font.render(
                'Он никогда не проигрывал в научных битвах до этого.', False,
                (255, 255, 255))
            text3 = font.render(
                'Он мог бы сбежать отсюда, но власть, которую он получил',
                False, (255, 255, 255))
            text4 = font.render('здесь очень манит его.', False,
                                (255, 255, 255))
        elif self.loc == 3:
            font_path = os.path.join("data/fonts", "comic.ttf")
            font = pygame.font.Font(font_path, 20)
            text1 = font.render('', False, (255, 255, 255))
            text2 = font.render('', False, (255, 255, 255))
            text3 = font.render('', False, (255, 255, 255))
            text4 = font.render('', False, (255, 255, 255))

        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)


class Sign(pygame.sprite.Sprite):
    image = load_image('sign.png')
    image = pygame.transform.scale(image, (51, 54))

    def __init__(self, x_pos, y_pos):
        super().__init__(all_sprites, sign_group)
        self.image = Sign.image
        self.rect = self.image.get_rect().move(x_pos, y_pos)


class Letters(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        a = random.choice(['letter_a.png', 'letter_b.png', 'letter_v.png',
                           'letter_g.png', 'letter_d.png'])
        image_path = load_image(a)
        self.image = pygame.transform.scale(image_path, (40, 60))
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def update(self):
        self.rect.x -= 9
        if pygame.sprite.collide_mask(self, player):
            end_screen(1, False)
            return


class Background(pygame.sprite.Sprite):
    def __init__(self, image_path, size):
        super().__init__()
        self.image = load_image(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_threshold(self.image, (237, 28, 36),
                                               (1, 1, 1, 255))

    def get_rgb(self, x, y):
        pixel = pygame.PixelArray(self.image)
        return self.image.unmap_rgb(pixel[x][y])


class Door(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, act, tip):
        super().__init__(all_sprites)
        if act == 1:
            image_path = load_image(f'door_a1_{tip}.png')
        elif act == 2:
            image_path = load_image('exit-enter_a2.png')
        if tip == 1:
            self.image = pygame.transform.scale(image_path, (120, 96))
        elif tip == 2:
            self.image = pygame.transform.scale(image_path, (112, 67))
        self.rect = self.image.get_rect().move(pos_x, pos_y + 20)
        self.mask = pygame.mask.from_surface(self.image)


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, vx, vy, xx, yy, canDamage, image):
        image_path = load_image(image)
        image_path = pygame.transform.scale(image_path, (xx + 50, yy))
        sprite_image = image_path
        super().__init__(rectangle_group, all_sprites)
        self.image = sprite_image
        self.rect = self.image.get_rect().move(pos_x, pos_y + 20)
        self.mask = pygame.mask.from_surface(self.image)
        self.vx = vx
        self.vy = vy
        self.canDamage = canDamage

    def update(self):
        global rectangle_group, plat
        self.rect.x += 2 * self.vx
        self.rect.y += 2 * self.vy
        if self.canDamage and not (pygame.sprite.collide_mask(player, plat)):
            if pygame.sprite.collide_mask(self, player):
                for j in rectangle_group:
                    j.rect.x = 10000

                rectangle_group = pygame.sprite.Group()
                if player.loc == 4:
                    end_screen(1, False)
                elif player.loc == 11:
                    end_screen(2, False)
                elif player.loc == 15:
                    end_screen(3, False)
                return


class Button(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tip):
        super().__init__(all_sprites)
        if player.loc == 15:
            image_path = load_image(f'button{tip}_{tip}.jpg')
        else:
            image_path = load_image(f'button{tip}.jpg')
        self.image = pygame.transform.scale(image_path, (80, 80))
        self.rect = self.image.get_rect().move(pos_x, pos_y + 20)
        self.mask = pygame.mask.from_surface(self.image)
        self.tip = tip
        self.tm = 300

    def update(self):
        if player.loc != 15:
            if pygame.sprite.spritecollideany(self, player_group):
                font_path = os.path.join("data/fonts", "comic.ttf")
                font = pygame.font.Font(font_path, 50)
                screen.blit(
                    font.render(str(self.tm // 100 + 1), True, (0, 0, 0)),
                    (350, 0))
                if self.tm // 100 + 1 == 0:
                    if self.tip == ok_tip + 1:
                        self.tm += 1
                        player.key = True
                    else:
                        for j in button_group:
                            j.rect.x = 20000
                        end_screen(2, False)
                self.tm -= 1
            else:
                self.tm = 300


class Pass(pygame.sprite.Sprite):
    image = load_image('pass.png')
    image = pygame.transform.scale(image, (79, 90))

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = Pass.image
        self.rect = self.image.get_rect().move(pos_x, pos_y)


class Chest(pygame.sprite.Sprite):
    image = load_image('chest.jpg')
    image = pygame.transform.scale(image, (60, 40))

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = Chest.image
        self.rect = self.image.get_rect().move(pos_x, pos_y)


class Defens(pygame.sprite.Sprite):
    image = load_image('defens.jpg')
    image = pygame.transform.scale(image, (200, 200))

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = Defens.image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Apple(pygame.sprite.Sprite):
    image = load_image('apple.jpg')
    image = pygame.transform.scale(image, (20, 20))

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = Apple.image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Traveler(pygame.sprite.Sprite):
    image = load_image('traveler.jpg')
    image = pygame.transform.scale(image, (70, 90))

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = Traveler.image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Platform(pygame.sprite.Sprite):
    image = load_image('platform.jpg')
    image = pygame.transform.scale(image, (100, 90))

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = Platform.image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class WizardRus(pygame.sprite.Sprite):
    image = load_image('wizardRus.png')
    image = pygame.transform.scale(image, (80, 90))

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = WizardRus.image
        self.rect = self.image.get_rect().move(
            pos_x, pos_y)
        self.canRun = False
        self.y = pos_y

    def update(self):
        if self.canRun:
            self.rect.y -= 15
            self.y -= 15
            if self.y <= -100:
                self.rect.y = -1000
        if player.y <= 800:
            self.canRun = True


wizardRus = WizardRus(2000, 2000)


def act3_buttons():
    global task_text, difference, question, buttons, a, b, tm
    a = random.randint(0, 100)
    difference = random.randint(1, 4)
    b = difference - a
    if b < 0:
        question = f"{a}{b}"
    else:
        question = f"{a} + {b}"
    font_path = os.path.join("data/fonts", "comic.ttf")
    font = pygame.font.Font(font_path, 50)
    task_text = font.render(question, True, (0, 0, 0))
    buttons = []
    for j in range(1, 5):
        buttons.append(
            Button(x - player.x + j * 150, y - player.y + 200, j))
    tm = 300
    screen.blit(font.render(str(tm // 100 + 1), True, (0, 0, 0)),
                (350, 0))


def results():
    con = sqlite3.connect("data/bd.sqlite")
    cur = con.cursor()
    result1 = cur.execute("""SELECT time FROM player
            WHERE act == 1 ORDER BY time""").fetchall()[:10]
    result2 = cur.execute("""SELECT time FROM player
            WHERE act == 2 ORDER BY time""").fetchall()[:10]
    result3 = cur.execute("""SELECT time FROM player
            WHERE act == 3 ORDER BY time""").fetchall()[:10]
    con.close()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.KEYDOWN or event.type ==
                  pygame.MOUSEBUTTONDOWN):
                return
        screen.blit(load_image("sybtit.png"), (0, 0))
        font_path = os.path.join("data/fonts", "comic.ttf")
        font = pygame.font.Font(font_path, 20)
        y = 0
        for res in result1:
            screen.blit(font.render(res[0], True, (255, 255, 255)),
                        (150, 100 + y))
            y += 40
        y = 0
        for res in result2:
            screen.blit(font.render(res[0], True, (255, 255, 255)),
                        (350, 100 + y))
            y += 40
        y = 0
        for res in result3:
            screen.blit(font.render(res[0], True, (255, 255, 255)),
                        (550, 100 + y))
            y += 40
        font = pygame.font.Font(font_path, 50)
        text_1 = font.render("1 Act", True, (255, 255, 255))
        text_2 = font.render("2 Act", True, (255, 255, 255))
        text_3 = font.render("3 Act", True, (255, 255, 255))
        screen.blit(text_1, (150, 0))
        screen.blit(text_2, (350, 0))
        screen.blit(text_3, (550, 0))
        pygame.display.flip()
        clock.tick(FPS)


def sybtit_screen():
    j = 0
    sybtit = load_image('sybtit.png')
    pygame.mixer.music.load("data/final_melody.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        screen.blit(sybtit, (0, -j))
        pygame.display.flip()

        j += 2
        if j >= 1750:
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


clock = pygame.time.Clock()
FPS = 60
# группы спрайтов
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
rectangle_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()
word_group = pygame.sprite.Group()
sign_group = pygame.sprite.Group()
text_group = pygame.sprite.Group()

time = datetime.datetime.now()
x, y = 0, 0
rect = Rectangle(20000, 20000, 0, 0, 10, 500, False, "redrect.jpg")
img = load_image('key.jpg')
img = pygame.transform.scale(img, (50, 50))
sign1 = Sign(120, 20000)
sign2 = Sign(658, 20000)
sign3 = Sign(120, 20000)
sign4 = Sign(658, 20000)
sign5 = Sign(120, 20000)
sign6 = Sign(658, 20000)

loc5 = 0
loc11 = 0
loc14 = 0

runi = -600
camera = Camera()
apples = []
tm = 0
difference = 0

door2 = Door(20000, 20000, 2, 1)
door3 = Door(20000, 20000, 2, 1)
chest = Chest(20000, 20000)
plat = Platform(20000, 20000)
pas = Pass(20000, 20000)
traveler = Traveler(20000, 20000)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Entangled Tale')
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    start_screen()

    text1 = pygame.font.Font(os.path.join("data/fonts", "comic.ttf"),
                             20).render('', False, (255, 255, 255))
    text2 = pygame.font.Font(os.path.join("data/fonts", "comic.ttf"),
                             20).render('', False, (255, 255, 255))
    text3 = pygame.font.Font(os.path.join("data/fonts", "comic.ttf"),
                             20).render('', False, (255, 255, 255))
    text4 = pygame.font.Font(os.path.join("data/fonts", "comic.ttf"),
                             20).render('', False, (255, 255, 255))
    i = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    menu()
                if event.key == pygame.K_e and runi == -600:
                    runi = 300
            if event.type == pygame.KEYUP:
                player.stop()

        if runi != -600:
            player.run = 9
        if runi < 0:
            player.run = 5
        if player.loc <= 5:
            screen.fill((2, 0, 0))
        elif 5 < player.loc <= 12:
            screen.fill((34, 177, 76))
        else:
            screen.fill((153, 217, 234))
        keys = pygame.key.get_pressed()

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
        if player.loc == 7:
            screen.blit(task_text, (x - player.x + 780, y - player.y + 160))
        if not player.key and pygame.sprite.collide_mask(player, chest):
            font_path = os.path.join("data/fonts", "comic.ttf")
            font = pygame.font.Font(font_path, 40)
            task_text = font.render("Нужен ключ!", True, (255, 255, 255))
            screen.blit(task_text, (300, 0))
        if pygame.sprite.collide_mask(player, traveler):
            font_path = os.path.join("data/fonts", "comic.ttf")
            font = pygame.font.Font(font_path, 25)
            if player.appls not in [5, 6]:
                task_text = font.render("Принеси мне 5 яблок, "
                                        "в обмен на информацию", True,
                                        (255, 255, 255))
            else:
                task_text = font.render(
                    "Выпей воды из озера и можешь идти спокойно", True,
                    (255, 255, 255))
                player.appls = 6

            screen.blit(task_text, (100, 0))
        if (not player.pas and pygame.sprite.collide_mask(player, pas) and
                player.loc == 6):
            font_path = os.path.join("data/fonts", "comic.ttf")
            font = pygame.font.Font(font_path, 40)
            task_text = font.render("Нужна монета!", True, (255, 255, 255))
            screen.blit(task_text, (300, 0))
        if player.loc == 13 and background.get_rgb(player.x + player.run,
                                                   player.y + player.run) == (
                187, 122, 87) \
                and (187, 122, 87) in player.stena:
            font_path = os.path.join("data/fonts", "comic.ttf")
            font = pygame.font.Font(font_path, 40)
            task_text = font.render("Дальше нельзя", True, (0, 0, 0))
            screen.blit(task_text, (300, 0))
        player_group.draw(screen)
        if runi > -600:
            runi -= 1

        if player.loc == 2:
            i += 1
            if i % 40 == 0:
                letter = Letters(x - player.x + 2500,
                                 random.randint(y - player.y + 450,
                                                y - player.y + 660))
                word_group.add(letter)
            word_group.update()
            word_group.draw(screen)

        screen.blit(pygame.transform.scale(load_image("run.png"), (40, 40)),
                    (5, 5))
        font_path = os.path.join("data/fonts", "comic.ttf")
        if runi == -600:
            txt = pygame.font.Font(font_path, 35).render(f"active", True,
                                                         (255, 0, 0))
            screen.blit(txt, (50, 0))
        else:
            txt = pygame.font.Font(font_path, 30).render(
                f"{(runi + 660) // 60}", True, (255, 0, 0))
            screen.blit(txt, (50, 5))

        if player.key:
            screen.blit(img, (750, 0))

        if player.appls != 6:
            for i in range(player.appls):
                screen.blit(img, (770 - i * 30, 0))

        if player.loc == 4:
            if 200 <= loc5 <= 1000 and loc5 % 200 == 0:
                try:
                    n = random.randint(-1, 3) * 200
                    while n == m:
                        n = random.randint(-1, 3) * 200
                    m = n
                except Exception:
                    m = random.randint(-1, 3) * 200
                rect.rect.x = 20000
                rect = Rectangle(x - player.x + m,
                                 y - player.y - 78, 0, 0, 450,
                                 519, False, "warning rect.png")
            if 340 <= loc5 <= 1000 and loc5 % 200 == 140:
                rect.rect.x = 20000
                rect = Rectangle(x - player.x + m,
                                 y - player.y - 78, 0, 0, 450,
                                 519, True, "grayrect.jpg")
            if 1000 <= loc5 <= 3000 and loc5 % 100 == 0:
                rect.rect.x = 20000
                Rectangle(x - player.x + 800,
                          y - player.y + random.randint(-100, 150), -3, 0, 10,
                          random.randint(50, 300), True, "redrect.jpg")
            if 3200 <= loc5 <= 4000 and loc5 % 200 == 0:
                n = random.randint(-1, 3) * 200
                while n == m:
                    n = random.randint(-1, 3) * 200
                m = n
                rect.rect.x = 20000
                rect = Rectangle(x - player.x + m,
                                 y - player.y - 78, 0, 0, 450,
                                 519, False, "warning rect.png")
            if 3200 <= loc5 <= 4140 and loc5 % 200 == 140:
                rect.rect.x = 20000
                rect = Rectangle(x - player.x + m,
                                 y - player.y - 78, 0, 0, 450,
                                 519, True, "grayrect.jpg")
            if loc5 == 4200:
                rect.rect.x = 20000
            if loc5 == 4400:
                door = Door(x - player.x + 350, y - player.y + 150, 1, 1)
                player.loc = 5
            loc5 += 1
            rectangle_group.update()
        if player.loc == 11:
            if loc11 <= 2000 and loc11 % 100 == 0:
                Rectangle(x - player.x + 800,
                          y - player.y + random.randint(-100, 200), -3, 0,
                          random.randint(100, 300),
                          10, True, "greenrect2.jpg")
                Rectangle(x - player.x + 800,
                          y - player.y + random.randint(200, 450), -3, 0,
                          random.randint(100, 300),
                          10, True, "greenrect2.jpg")
            if 2300 <= loc11 <= 3400 and loc11 % 100 == 0:
                Rectangle(x - player.x + random.randint(-100, 300),
                          y - player.y - 200, 0, 1, 20,
                          random.randint(100, 300),
                          True, "greenrect1.jpg")
                Rectangle(x - player.x + random.randint(300, 800),
                          y - player.y - 200, 0, 1, 20,
                          random.randint(100, 300),
                          True, "greenrect1.jpg")
            if 3400 <= loc11 <= 5000 and loc11 % 100 == 0:
                Rectangle(x - player.x + 800,
                          y - player.y + random.randint(-100, 200), -3, 0,
                          random.randint(100, 300),
                          10, True, "greenrect2.jpg")
                Rectangle(x - player.x - 300,
                          y - player.y + random.randint(200, 450), 3, 0,
                          random.randint(100, 300),
                          10, True, "greenrect2.jpg")
            if loc11 == 5400:
                door = Door(x - player.x + 350, y - player.y + 150, 1, 1)
                player.loc = 12
            loc11 += 1
            rectangle_group.update()

        if player.loc == 15:
            if loc14 == 200:
                p = [random.randint(0, 600),
                     random.randint(0, 300)]
                plat = Platform(x - player.x + p[0], y - player.y + p[1])
            elif loc14 == 400:
                plat.rect.x = 20000
                rect = Rectangle(-200, -200, 0, 0, 2000, 2000, True,
                                 "damage_platform.jpg")
                plat = Platform(x - player.x + p[0], y - player.y + p[1])
            elif loc14 == 500:
                plat.rect.x = 20000
                rect.rect.x = 20000
            elif loc14 == 600:
                act3_buttons()
            if 600 <= loc14 <= 900:
                tm -= 1
                font_path = os.path.join("data/fonts", "comic.ttf")
                font = pygame.font.Font(font_path, 50)
                screen.blit(task_text, (300, 0))
                screen.blit(font.render(str(tm // 100 + 1), True, (0, 0, 0)),
                            (650, 0))
            if loc14 == 900:
                for j in buttons:
                    if pygame.sprite.collide_mask(player,
                                                  j) and j.tip == difference:
                        for k in buttons:
                            k.rect.x = 20000
                            buttons = []
                        break
                else:
                    end_screen(3, False)

            if loc14 == 1000:
                p = [random.randint(0, 600),
                     random.randint(0, 300)]
                plat = Platform(x - player.x + p[0], y - player.y + p[1])
            elif loc14 == 1200:
                plat.rect.x = 20000
                rect = Rectangle(-200, -200, 0, 0, 2000, 2000, True,
                                 "damage_platform.jpg")
                plat = Platform(x - player.x + p[0], y - player.y + p[1])
            elif loc14 == 1300:
                plat.rect.x = 20000
                rect.rect.x = 20000
            if 1400 <= loc14 <= 2000 and loc14 % 100 == 0:
                Rectangle(x - player.x + 800,
                          y - player.y + random.randint(-50, 200), -3, 0,
                          random.randint(100, 300),
                          10, True, "damage_platform.jpg")
                Rectangle(x - player.x - 300,
                          y - player.y + random.randint(200, 450), 3, 0,
                          random.randint(100, 300),
                          10, True, "damage_platform.jpg")

            if loc14 == 2100:
                p = [random.randint(0, 600),
                     random.randint(0, 300)]
                plat = Platform(x - player.x + p[0], y - player.y + p[1])
            elif loc14 == 2300:
                plat.rect.x = 20000
                rect = Rectangle(-200, -200, 0, 0, 2000, 2000, True,
                                 "damage_platform.jpg")
                plat = Platform(x - player.x + p[0], y - player.y + p[1])
            elif loc14 == 2400:
                plat.rect.x = 20000
                rect.rect.x = 20000
            elif loc14 == 2500:
                act3_buttons()
            if 2500 <= loc14 <= 2800:
                tm -= 1
                font_path = os.path.join("data/fonts", "comic.ttf")
                font = pygame.font.Font(font_path, 50)
                screen.blit(task_text, (300, 0))
                screen.blit(font.render(str(tm // 100 + 1), True, (0, 0, 0)),
                            (650, 0))
            if loc14 == 2800:
                for j in buttons:
                    if pygame.sprite.collide_mask(player,
                                                  j) and j.tip == difference:
                        for k in buttons:
                            k.rect.x = 20000
                            buttons = []
                        break
                else:
                    end_screen(3, False)
            if 3000 <= loc14 <= 3500 and loc14 % 100 == 0:
                Rectangle(x - player.x + 800,
                          y - player.y + random.randint(-50, 200), -3, 0,
                          random.randint(100, 300),
                          10, True, "damage_platform.jpg")
                Rectangle(x - player.x - 300,
                          y - player.y + random.randint(200, 450), 3, 0,
                          random.randint(100, 300),
                          10, True, "damage_platform.jpg")

            if 3500 <= loc14 <= 4000 and loc14 % 100 == 0:
                Rectangle(x - player.x - 300,
                          y - player.y + random.randint(-50, 200), 3, 0,
                          random.randint(100, 300),
                          10, True, "damage_platform.jpg")
                Rectangle(x - player.x + 800,
                          y - player.y + random.randint(200, 450), -3, 0,
                          random.randint(100, 300),
                          10, True, "damage_platform.jpg")
            if loc14 == 4100:
                p = [random.randint(0, 600),
                     random.randint(0, 300)]
                plat = Platform(x - player.x + p[0], y - player.y + p[1])
            elif loc14 == 4300:
                plat.rect.x = 20000
                rect = Rectangle(-200, -200, 0, 0, 2000, 2000, True,
                                 "damage_platform.jpg")
                plat = Platform(x - player.x + p[0], y - player.y + p[1])
            elif loc14 == 4400:
                plat.rect.x = 20000
                rect.rect.x = 20000
            elif loc14 == 4500:
                act3_buttons()
            if 4500 <= loc14 <= 4800:
                tm -= 1
                font_path = os.path.join("data/fonts", "comic.ttf")
                font = pygame.font.Font(font_path, 50)
                screen.blit(task_text, (300, 0))
                screen.blit(font.render(str(tm // 100 + 1), True, (0, 0, 0)),
                            (650, 0))
            if loc14 == 4800:
                for j in buttons:
                    if pygame.sprite.collide_mask(player,
                                                  j) and j.tip == difference:
                        for k in buttons:
                            k.rect.x = 20000
                            buttons = []
                        break
                else:
                    end_screen(3, False)
            if 5000 <= loc14 <= 5500 and loc14 % 100 == 0:
                Rectangle(x - player.x + 800,
                          y - player.y + random.randint(-50, 200), -3, 0,
                          random.randint(100, 300),
                          13, True, "damage_platform.jpg")
                Rectangle(x - player.x - 300,
                          y - player.y + random.randint(200, 450), 3, 0,
                          random.randint(100, 300),
                          13, True, "damage_platform.jpg")
            if 5500 <= loc14 <= 6000 and loc14 % 100 == 0:
                Rectangle(x - player.x - 300,
                          y - player.y + random.randint(-50, 200), 3, 0,
                          random.randint(100, 300),
                          13, True, "damage_platform.jpg")
                Rectangle(x - player.x + 800,
                          y - player.y + random.randint(200, 450), -3, 0,
                          random.randint(100, 300),
                          13, True, "damage_platform.jpg")
            if loc14 == 6200:
                door = Door(x - player.x + 100, y - player.y + 150, 1, 1)
                player.loc = 16

            loc14 += 1
            rectangle_group.update()

        if player.loc == 3:
            sign_group.update()
            for i in sign_group:
                if pygame.sprite.collide_mask(player, i):
                    screen.blit(pygame.transform.scale(load_image("text_window.png"), (600, 150)),
                                (100, 0))
            screen.blit(text1, (110, 10))
            screen.blit(text2, (110, 40))
            screen.blit(text3, (110, 70))
            screen.blit(text4, (110, 100))

        button_group.update()
        door_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
