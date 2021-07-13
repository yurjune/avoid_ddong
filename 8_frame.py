import pygame
############################################################
# 기본 초기화 (반드시)
pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption('Honey Game')

# FPS
clock = pygame.time.Clock()

############################################################
# 1. 사용자 게임 초기화(배경, 캐릭터 정보(크기, 위치, 속도..), 폰트, 시간..)

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()

pygame.quit()
