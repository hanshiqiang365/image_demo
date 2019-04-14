#author: hanshiqiang365 （微信公众号：韩思工作室）
 
import pygame
import random

pygame.init()
  
SIZE = (1280, 720)

demoIcon = pygame.image.load("demo_icon.jpg")
pygame.display.set_icon(demoIcon)

pygame.mixer.init()
pygame.mixer.music.load("demo_bgm.wav")
pygame.mixer.music.play(-1)
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snowing Demo - Developed by hanshiqiang365 (wechat public account)")
bg = pygame.image.load('snow.jpg')

snow_list = []

for i in range(200):
    x = random.randrange(0, SIZE[0])
    y = random.randrange(0, SIZE[1])
    sx = random.randint(-1, 1)
    sy = random.randint(3, 6)
    snow_list.append([x, y, sx, sy])
 
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.blit(bg, (0, 0))

    for i in range(len(snow_list)):
        pygame.draw.circle(screen, (255, 255, 255), snow_list[i][:2], snow_list[i][3]-3)
 
        snow_list[i][0] += snow_list[i][2]
        snow_list[i][1] += snow_list[i][3]
 
        if snow_list[i][1] > SIZE[1]:
            snow_list[i][1] = random.randrange(-50, -10)
            snow_list[i][0] = random.randrange(0, SIZE[0])
 
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
