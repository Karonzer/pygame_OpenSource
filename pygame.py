import pygame
import random

pygame.init()

# 화면 사이즈 설정
screen_size = [1200, 400]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Game")

# 색상 및 FPS 설정
screen_color = (255, 255, 255)
fps = pygame.time.Clock()

# 게임 변수
running = True
startGame = False
gameOver = False

# player 캐릭터 이미지 및 크기
player_images = [
    pygame.transform.scale(pygame.image.load('EndRun/Player1.png'), (50, 50)),
    pygame.transform.scale(pygame.image.load('EndRun/Player2.png'), (50, 50)),
    pygame.transform.scale(pygame.image.load('EndRun/Player3.png'), (50, 50))
]

# 장애물 이미지 및 위치
Obstacle = 1
ObstacleMoveSpeed = 5
Obstacletick = 0
ObstacleSponX = [1200,1200,1200]
ObstacleSponY = [0,0,0]
Obstacle_images = [
    pygame.transform.scale(pygame.image.load('EndRun/mob1.png'), (50, 50)),
    pygame.transform.scale(pygame.image.load('EndRun/mob1.png'), (50, 50)),
    pygame.transform.scale(pygame.image.load('EndRun/mob1.png'), (50, 50))
]

# player 캐릭터 위치
x = 10
y = 150

# 애니메이션 변수 설정
current_frame = 0  # 현재 애니메이션 프레임
frame_duration = 100  # 각 프레임 지속 시간 (밀리초 단위)
last_update_time = pygame.time.get_ticks()  # 마지막으로 프레임이 전환된 시간

# 점수 텍스트
score = 0
scoretick = 0
scoreFont = pygame.font.SysFont("arial",25)

# 게임 시작 텍스트
gameStartText = 0
gameStartFont = pygame.font.SysFont("arial",50)

# 게임 설명 텍스트 
gameGuideFont= pygame.font.SysFont("arial",50)
gameGuideText01 = 0
gameGuideText02 = 0
gameGuideText03 = 0
gameGuideText04 = 0

# 게임 오버 텍스
gameOverFont = pygame.font.SysFont("arial",50)
gameOverText = 0
gameReStartText = 0

def Initialize_Score():
    global score
    global scoretick
    score = 0
    scoretick = 0


#처음 시작할때 장애물 위치 Y 랜덤 배치
def Initialize_ObstacleSponY() :
    global Obstacle
    global ObstacleSponX
    global ObstacleSponY
    global ObstacleMoveSpeed
    global Obstacletick

    Obstacle = 1
    Obstacletick = 0
    ObstacleMoveSpeed = 5
    for i in range(len(ObstacleSponY)) :
        ObstacleSponX[i] = 1200
        ObstacleSponY[i] = random.randrange(0,351)

#처음 시작할때 캐릭터 위치 X Y 배치
def Initialize_PlayerSponXY() :
    global x
    global y
    x = 10
    y = 150

# 처음 게임 시작할때 표현하는 함수
def Show_GameStartText() :
    gameStartText = scoreFont.render("Game Start Click : Left Mouse Click", True, (0,0,0))
    screen.blit(gameStartText, (450, 100))

    gameGuideText01 = scoreFont.render("Keyboard ← : Left Move", True, (0,0,0))
    screen.blit(gameGuideText01, (450, 210))

    gameGuideText02 = scoreFont.render("Keyboard → : Right Move", True, (0,0,0))
    screen.blit(gameGuideText02, (450, 240))

    gameGuideText03 = scoreFont.render("Keyboard ↑ : Up Move", True, (0,0,0))
    screen.blit(gameGuideText03, (450, 270))

    gameGuideText04 = scoreFont.render("Keyboard ↓ : Donw Move", True, (0,0,0))
    screen.blit(gameGuideText04, (450, 300))

# 마우스 클릭하여 게임 시작 함수
def GameStartClick() :
    global startGame
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN :
        startGame = True

# 닫기 버튼에 게임종료 함수
def Stop_GameQuit():
    global running
    event = pygame.event.poll()
    if event.type == pygame.QUIT:  # 창 닫기 이벤트 처리
        running = False

# 키 입력 이벤트 함수
def Input_KeyUpDown() :
    global x
    global y
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] :
        if y <= 0 :
            y = 0
        else :
            y -= 5
        
    if pressed[pygame.K_DOWN] :
        if y >= 350 :
            y = 350
        else :
            y +=5

    if pressed[pygame.K_LEFT] :
        if x <= 0 :
            x = 0
        else :
            x -= 5
        
    if pressed[pygame.K_RIGHT] :
        if x >= 1100 :
            x = 1100
        else :
            x +=5

# player 캐릭터 이동 애니메이션 함수
def PlayerAni() :
    global last_update_time
    global current_frame
    now = pygame.time.get_ticks()  # 현재 시간 (밀리초)
    if now - last_update_time > frame_duration:
        current_frame = (current_frame + 1) % len(player_images)  # 다음 프레임으로 전환
        last_update_time = now

# 현재 점수 표현 함수
def ScoreTextShow(_score) :
    global score
    global scoretick

    if (_score / 60) == 1 :
        scoretick = 0
        score +=1
    scoreText = scoreFont.render("Score : " + str(score), True, (0,0,0))
    screen.blit(scoreText, (1050, 25))

# 장애물 이동 및 생성 캐릭터 충돌 체크
def Show_Obstacle() :
    global Obstacletick
    global Obstacle
    global ObstacleMoveSpeed
    global ObstacleSponX
    global ObstacleSponY
    global gameOver

    if(Obstacletick / 600) == 1 :
        Obstacletick = 0
        Obstacle += 1

        if ObstacleMoveSpeed <= 10 :
            ObstacleMoveSpeed +=1

        # 장애물 추가
        if Obstacle > len(Obstacle_images) :
            ObstacleSponX.append(1200)
            ObstacleSponY.append(random.randrange(0,351))
            Obstacle_images.append(pygame.transform.scale(pygame.image.load('EndRun/mob1.png'), (50, 50)))
    # 장애물 이동
    for i in range(Obstacle) :
       screen.blit(Obstacle_images[i], (ObstacleSponX[i],ObstacleSponY[i]))
       ObstacleSponX[i] -= ObstacleMoveSpeed

        # 장애물과 캐릭터 충돌 확인
       if (x - 10) <= ObstacleSponX[i] and  (x + 10) >= ObstacleSponX[i] and (y - 20)  <= ObstacleSponY[i] and (y + 20) >= ObstacleSponY[i] :
            gameOver = True

        # 장애물 다시 원위치 설정
       if(ObstacleSponX[i] <= -10) : 
           ObstacleSponX[i] = 1200
           ObstacleSponY[i] = random.randrange(0,351)
        
# 게임 오버 텍스트 표현
def Show_GameOverText() :
    gameOverText = gameOverFont.render("Game Over", True, (0,0,0))
    screen.blit(gameOverText, (440, 100))

    gameReStartText = gameOverFont.render("Game Re Start : Left Mouse Click", True, (0,0,0))
    screen.blit(gameReStartText, (250, 200))

# 다시 시작
def GameReStartClick() :
    global gameOver
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN :
        gameOver = False
        Initialize_Score()
        Initialize_PlayerSponXY()
        Initialize_ObstacleSponY()

# 게임 실행
def PlayGame() :
    Initialize_Score()
    Initialize_PlayerSponXY()
    Initialize_ObstacleSponY()
    global scoretick
    global Obstacletick

    #반복
    while running:
        fps.tick(60)
        # 화면 그리기
        screen.fill(screen_color)

        #  게임 이벤트 처리
        if startGame == False :
            Show_GameStartText()
            GameStartClick()

            Stop_GameQuit()
        else:
            # 게임중
            if gameOver == False:
                scoretick += 1
                Obstacletick += 1
                PlayerAni()
                Input_KeyUpDown()
                ScoreTextShow(scoretick)
            
                Show_Obstacle()
            else :
                # 게임 오버
                Show_GameOverText()
                GameReStartClick()
            
            Stop_GameQuit()


        screen.blit(player_images[current_frame], (x, y))
        pygame.display.update()


PlayGame()
# Pygame 종료
pygame.quit()
