import pygame
import random
pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption('Honey Game')

# FPS
clock = pygame.time.Clock()
# 10fps: 1초동안 10번동작, 1초동안 100이동해야 하면 10씩 10번 이동 
# 20FPS: 1초동안 20번 동작, 1초동안 100 이동해야하면 5씩 20번 이동

# 배경
background = pygame.image.load('C:\\codingpractice\\pygame_basic\\background.png')

# 캐릭터
character = pygame.image.load('C:\\codingpractice\\pygame_basic\\character.png')
character_size = character.get_rect().size  # 이미지 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2  # 화면 가로의 중앙에 위치
character_y_pos = screen_height - character_height  # 가장 아래 위치

# 적
enemy = pygame.image.load('C:\\codingpractice\\pygame_basic\\enemy.png')
enemy_size = enemy.get_rect().size  # 이미지 크기를 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = enemy_height * -1

# 이동할 거리
to_x_LEFT = 0
to_x_RIGHT = 0
to_y = 0.6

# 이동속도
character_speed = 0.6

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시간 계산
start_ticks = pygame.time.get_ticks()   # 현재 tick을 받아옴

# 이벤트 루프
running = True
while running:
    # 프레임
    dt = clock.tick(30)

    # 어떤 이벤트가 발생했는지 체크
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 캐릭터 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x_LEFT -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x_RIGHT += character_speed

        # 방향키 떼면 멈춤
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_x_LEFT = 0
            elif event.key == pygame.K_RIGHT:
                to_x_RIGHT = 0

    # 캐릭터 이동
    # FPS에 따라 속도가 달라지면 안되므로 dt를 곱해준다
    to_x = to_x_LEFT + to_x_RIGHT
    character_x_pos += to_x * dt
    enemy_y_pos += to_y * dt

    # 캐릭터 화면 밖으로 안나가게
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    # 적 재생성
    if enemy_y_pos >= screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = enemy_height * -1

    # 충돌처리
    # 캐릭터의 정보 업데이트: screen.blit(character, (character_x_pos, character_y_pos))에서 좌표는 변하지만
    # character자체의 정보는 변하지 않으므로 업데이트 해줘야함
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌체크
    if character_rect.colliderect(enemy_rect):
        print('충돌했어요')
        running = False
    
    # 이미지 표시
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 경과 시간: 현재 시간 - 처음 시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   # 초로 환산

    # 남은 시간
    rest_time = total_time - elapsed_time

    if rest_time <= 0:
        print('승리')
        running = False

    # 타이머 표시
    timer = game_font.render(str(int(rest_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))    # 출력 글자, True, 색상

    # 업데이트
    pygame.display.update() # 매 수행마다 화면을 새로 그려야함

pygame.time.delay(1000)
pygame.quit()
