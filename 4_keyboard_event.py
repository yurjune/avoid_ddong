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

# 캐릭터
character = pygame.image.load('C:\\codingpractice\\pygame_basic\\character.png')
character_size = character.get_rect().size  # 이미지 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2  # 화면 가로의 중앙에 위치
character_y_pos = screen_height - character_height  # 가장 아래 위치

# 이동할 거리
to_x = 0
to_y = 0

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생했는지 체크
        if event.type == pygame.QUIT:
            running = False
        # 캐릭터 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        # 방향키 떼면 멈춤
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터 이동
    character_x_pos += to_x
    character_y_pos += to_y

    # 캐릭터 화면 밖으로 안나가게
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 배경, 캐릭터 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 업데이트
    pygame.display.update() # 매 수행마다 화면을 새로 그려야함

pygame.quit()   
