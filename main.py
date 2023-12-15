import os
import pygame
import sys


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


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


tile_images = {
    'blackfon': load_image('blackfon.png'),
    'grayfon': load_image('grayfon.png'),
    'bhod': load_image('bhod.png'),
    'bhod2': load_image('bhod2.png'),
    'portal': load_image('portal.png')
}
tile_images['bhod'] = pygame.transform.scale(tile_images['bhod'], (55, 55))
tile_images['bhod2'] = pygame.transform.scale(tile_images['bhod2'], (55, 35))

tile_width = tile_height = 55

CELL_SIZE = 55


#  описание классов воды, непроходимых стен и разрешенной для ходьбы дороги
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        self.pos_x = pos_x
        self.tile_type = tile_type
        self.pos_y = pos_y
        if self.tile_type == 'blackfon':
            super().__init__(tiles_group, all_sprites, blackfon_group)
        else:
            super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            CELL_SIZE * pos_x, CELL_SIZE * pos_y)

    def get_tile_type(self):
        return self.tile_type


class Player(pygame.sprite.Sprite):
    image = load_image('player.jpg', colorkey=-1)
    image = pygame.transform.scale(image, (60, 80))

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    #  перемещение сундука по экрану
    def update(self, x, y):
        try:
            self.rect.x += x
            self.rect.y += y
            if pygame.sprite.spritecollide(self, blackfon_group, False):
                self.rect.x -= x
                self.rect.y -= y
        except:
            pass


# основной персонаж
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
blackfon_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('blackfon', x, y)
            elif level[y][x] == '*':
                Tile('grayfon', x, y)
            elif level[y][x] == '^':
                Tile('bhod', x, y)
            elif level[y][x] == '&':
                Tile('bhod2', x, y)
            elif level[y][x] == 'k':
                Tile('portal', x, y)
            elif level[y][x] == '@':
                Tile('grayfon', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


player, level_x, level_y = generate_level(load_level('map.txt'))

clock = pygame.time.Clock()

FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = [""]

    fon = pygame.transform.scale(load_image('fon.jpg'), (800, 500))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру

        pygame.display.flip()
        clock.tick(FPS)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
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
    start_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        # moves hero with key presses
        if keys[pygame.K_LEFT]:
            player.update(-10, 0)
        elif keys[pygame.K_RIGHT]:
            player.update(10, 0)
        if keys[pygame.K_UP]:
            player.update(0, -10)
        elif keys[pygame.K_DOWN]:
            player.update(0, 10)

        screen.fill((0, 0, 0))
        # изменяем ракурс камеры
        camera.update(player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
