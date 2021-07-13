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

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생했는지 체크
        # 종료조건
        if event.type == pygame.QUIT:
            running = False
    
    # 배경그리기
    screen.blit(background, (0, 0))

    # 캐릭터
    screen.blit(character, (character_x_pos, character_y_pos))

    # 업데이트
    pygame.display.update() # 매 수행마다 화면을 새로 그려야함

# 종료
pygame.quit()   
