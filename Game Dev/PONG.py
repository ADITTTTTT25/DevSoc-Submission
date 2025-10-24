import pygame, sys, random

#General Setup
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

#setting up main window
screen_width = 640
screen_height= 480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#game rectangles
ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10,20,20)
player = pygame.Rect(0, screen_height/2 - 45,10,90)
player2 = pygame.Rect(screen_width-10, screen_height/2 - 45,10,90)
restart = pygame.Rect(screen_width/2-100,screen_height/2 - 25,200,100)

#text
player1_score=0
player2_score=0
game_font=pygame.font.Font("freesansbold.ttf",32)

#Music
pygame.mixer.music.load("BGM.mp3")  
pygame.mixer.music.play(-1)

#image
# player1_img = pygame.image.load("Player1.png").convert_alpha()
# player1_img = pygame.transform.scale(player1_img, (player.width, player.height))

# player2_img = pygame.image.load("Player2.png").convert_alpha()
# player2_img = pygame.transform.scale(player2_img, (player2.width, player2.height))

# ball_img = pygame.image.load("Ball.png").convert_alpha()
# ball_img = pygame.transform.scale(ball_img, (ball.width, ball.height))

def ball_animation():
    global ball_speed_x,ball_speed_y, player1_score,player2_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y*=-1
    if ball.left <= 0:
        ball.center=(screen_width/2,screen_height/2)
        player.center = (5,screen_height/2)
        player2.center=(screen_width-5,screen_height/2)
        player2_score+=1
        ball_speed_x*=random.choice((-1,1))
        ball_speed_y*=random.choice((-1,1))
    if ball.right >= screen_width:
        ball.center=(screen_width/2,screen_height/2)
        player.center = (5,screen_height/2)
        player2.center=(screen_width-5,screen_height/2)
        player1_score+=1
        ball_speed_x*=random.choice((-1,1))
        ball_speed_y*=random.choice((-1,1))
    if ball.colliderect(player) or ball.colliderect(player2) :
        ball_speed_x*=-1

    

def player_movement():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def player2_movement():
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def gameOver(player1_score,player2_score):
    ball.center=(screen_width/2,screen_height/2)
    pygame.draw.rect(screen,light_grey,restart)
    result = None
    if(player1_score>player2_score):
        result = "Player 1"
    else:   
        result = "Player 2"
    gameOver_text=game_font.render(f"Game Over, {result} Wins!",False,light_grey)
    screen.blit(gameOver_text,(screen_width/2-200,screen_height/2-100))
    
    restart_text=game_font.render(f"Restart 'R'",False,"#000000")
    screen.blit(restart_text,(screen_width/2-80,screen_height/2+10))
            


bg_color = pygame.Color('grey12')
light_grey = (200,200,200)
ball_speed_x=5 * random.choice((-1,1))
ball_speed_y=5 * random.choice((-1,1))
player_speed=0
player2_speed = 0
while True:
    #Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player2_speed = 5
            if event.key == pygame.K_UP:
                player2_speed = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player2_speed = 0
            if event.key == pygame.K_UP:
                player2_speed = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_speed = 5
            if event.key == pygame.K_w:
                player_speed = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed = 0
            if event.key == pygame.K_w:
                player_speed = 0
        if event.type == pygame.KEYDOWN and (player1_score > 4 or player2_score > 4):
           if event.key == pygame.K_r:
                player1_score = 0
                player2_score  = 0
    #Visuals


    screen.fill(bg_color)

    if player1_score > 4 or player2_score > 4 :
        gameOver(player1_score=player1_score,player2_score=player2_score)
    else:   
        pygame.draw.ellipse(screen,light_grey,ball)
        pygame.draw.rect(screen,light_grey,player)
        pygame.draw.rect(screen,light_grey,player2)
        pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))
    

        player1_text=game_font.render(f"{player1_score}",False,light_grey)
        screen.blit(player1_text,(screen_width/2-35,screen_height/2))
        player2_text=game_font.render(f"{player2_score}",False,light_grey)
        screen.blit(player2_text,(screen_width/2 + 12,screen_height/2))

        # screen.blit(player1_img, player)
        # screen.blit(player2_img,player2)
        # screen.blit(ball_img,ball)


    ball_animation()
    player_movement()
    player2_movement()
    player.y+=player_speed
    player2.y += player2_speed
    #updating the window
    pygame.display.flip()
    clock.tick(60)

