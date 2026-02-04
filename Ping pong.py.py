import pygame
import sys

pygame.init()

width, Height = 800, 600
screen = pygame.display.set_mode((width, Height))
pygame.display.set_caption("Ping Pong Game")

White = (255, 255, 255)
Black = (0, 0, 0)

paddle_width = 10
paddle_height = 100
paddle_speed = 7

left_paddle = pygame.Rect(20, Height//2 - 50, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 30, Height//2 - 50, paddle_width, paddle_height)

ball = pygame.Rect(width//2, Height//2, 20, 20)
ball_speed_x = 6
ball_speed_y = 6

left_score = 0
right_score = 0
font = pygame.font.Font(None, 50)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < Height:
        left_paddle.y += paddle_speed

    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < Height:
        right_paddle.y += paddle_speed 

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= Height:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    if ball.left <= 0:
        right_score += 1
        ball.center = (width//2, Height//2)
        ball_speed_x *= -1

    if ball.right >= width:
        left_score += 1
        ball.center = (width//2, Height//2)
        ball_speed_x *= -1

    screen.fill(Black)
    pygame.draw.rect(screen, White, left_paddle)
    pygame.draw.rect(screen, White, right_paddle)
    pygame.draw.ellipse(screen, White, ball)
    pygame.draw.aaline(screen, White, (width//2, 0), (width//2, Height))

    left_text = font.render(str(left_score), True, White)
    right_text = font.render(str(right_score), True, White)
    screen.blit(left_text, (width//4, 20))
    screen.blit(right_text, (width*3//4, 20))

    pygame.display.flip()
    clock.tick(60)










