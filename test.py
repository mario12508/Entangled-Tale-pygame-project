import pygame
import sys

pygame.init()

# Размеры окна
width, height = 400, 200

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Установка окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Volume Control')

# Загрузка звукового файла
pygame.mixer.init()
pygame.mixer.music.load('data/mus_town.ogg')  # Замените 'your_music_file.mp3' на свой файл

# Создание ползунка
font = pygame.font.Font(None, 36)
text = font.render('Volume:', True, white)
text_rect = text.get_rect(center=(width // 2, height // 2 - 30))

volume = 0.5  # Начальная громкость
volume_text = font.render(str(int(volume * 100)), True, white)
volume_text_rect = volume_text.get_rect(center=(width // 2, height // 2 + 30))

pygame.mixer.music.set_volume(volume)  # Установка начальной громкости
pygame.mixer.music.play(-1)  # Запуск воспроизведения с бесконечным циклом

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка ползунка
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and volume < 1.0:
        volume += 0.01
    elif keys[pygame.K_DOWN] and volume > 0.0:
        volume -= 0.01

    pygame.mixer.music.set_volume(volume)  # Обновление громкости

    # Обновление текста
    volume_text = font.render(str(int(volume * 100)), True, white)

    # Отрисовка
    screen.fill(black)
    screen.blit(text, text_rect)
    screen.blit(volume_text, volume_text_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
