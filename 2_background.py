import pygame
pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption('Honey Game')

# 배경
background = pygame.image.load('C:\\codingpractice\\pygame_basic\\background.png')

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생했는지 체크
        # 종료조건
        if event.type == pygame.QUIT:
            running = False
    
    # 배경그리기
    screen.blit(background, (0, 0))
    # screen.fill((0, 0, 250))    # RGB 값으로 배경화면 대체 가능
    pygame.display.update() # 매 수행마다 화면을 새로 그려야함


# 종료
pygame.quit()   
