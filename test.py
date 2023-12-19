import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Pixelized Text")

# Загрузка шрифта
font_size = 36
font = pygame.font.Font('C:\Windows\Fonts\comic.ttf', font_size)

# Создание текстовой строки
text = "Pixelize Me!"
text_surface = font.render(text, True, WHITE)

# Получение прямоугольника текстовой строки и позиционирование в центре экрана
text_rect = text_surface.get_rect(center=(width // 2, height // 2))

# Уменьшение размера текста для пикселизации
pixel_size = 1
pixelated_text_surface = pygame.transform.scale(text_surface, (text_rect.width // pixel_size, text_rect.height // pixel_size))

# Главный цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(BLACK)

    # Отображение пикселизированного текста на экране
    screen.blit(pixelated_text_surface, text_rect.topleft)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для управления частотой обновления
    pygame.time.Clock().tick(60)
