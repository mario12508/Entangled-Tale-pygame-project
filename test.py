import pygame
import sys

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Инициализация экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Лесная локация")

# Загрузка изображения леса
forest_image = pygame.image.load("forest_background.png")

# Загрузка изображения объекта, в который можно отдать монету (сундук)
chest_image = pygame.image.load("chest.png")

# Позиция объекта
object_x, object_y = 300, 400

# Позиция монеты
coin_x, coin_y = 50, 50

# Количество монет
coin_count = 0

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Обработка действий при нажатии клавиши
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and coin_count > 0:
                # Если нажата клавиша пробела и у игрока есть монета, отдать монету
                coin_count -= 1
                print("Монета отдана в сундук!")

    # Отрисовка лесной локации
    screen.blit(forest_image, (0, 0))

    # Отрисовка объекта (сундук)
    screen.blit(chest_image, (object_x, object_y))

    # Отрисовка монеты
    if coin_count > 0:
        pygame.draw.circle(screen, (255, 255, 0), (coin_x, coin_y), 15)

    # Отображение количества монет
    font = pygame.font.Font(None, 36)
    text = font.render(f"Монеты: {coin_count}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
