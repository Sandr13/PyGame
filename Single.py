import pygame

pygame.init() #инициализируем pygame

### Задаём параметры экрана ###
display_width = 800
display_height = 600

################### Создадим дисплей ###################
display = pygame.display.set_mode((display_width, display_height))

################### Создадим заголовок окна ###################
pygame.display.set_caption('Title')

################### Класс объекта-игрока ###################
class Player():
    def __init__(self):
        self.width = 100
        self.height = 100
        self.x = 0
        self.y = 0
        self.speed = 1

################### Создаём игрока ###################
user1 = Player()

def run_game():
    ################### Бесконечный цикл ###################
    while True:
        for event in pygame.event.get():  # Считываем все события
            if event.type == pygame.QUIT:  # Считываем нажатие на крестик
                pygame.quit()  # Завершаем pygame
                quit() # Завершаем программу

        ################### Заполняем дисплей RGB-цветом ###################
        display.fill((0, 192, 192))

        ################### Рисуем игрока ###################
        pygame.draw.rect(display, (255, 255, 0), (user1.x, user1.y, user1.width, user1.height))

        pygame.display.update() # обновляем наш дисплей

run_game()
