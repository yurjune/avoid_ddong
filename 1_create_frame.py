import pygame
pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption('Honey Game')

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생했는지 체크
        if event.type == pygame.QUIT:   # 발생한 여러 이벤트 중에 QUIT가 있으면 종료
            running = False

# 종료
pygame.quit()
