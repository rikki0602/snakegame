import pygame
import random
# import time
pygame.init()

screen_width = 840
screen_height = 440

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game You Bit__")

fps = pygame.time.Clock()


food_pos = [random.randint(0,820)-3,random.randint(0,420)-5]

font1 = pygame.font.SysFont(None, 48)
# font1 = pygame.font.SysFont("didot,ttc", 48)

score = 0 


RUN = True
gameloop = True

def snake_movements(key_enter):
	if key_enter == pygame.K_UP:
		snake_speed[0]  = 0
		snake_speed[1] = -1*speed
		# print("Yes it Works")
	if key_enter == pygame.K_DOWN:
		snake_speed[0]  = 0
		snake_speed[1] = speed
	if key_enter == pygame.K_LEFT:
		snake_speed[0] = -1*speed
		snake_speed[1] = 0
	if key_enter == pygame.K_RIGHT:
		snake_speed[0] = speed
		snake_speed[1] = 0

def food_generation():
	food_pos[0] = random.randint(10,820)
	food_pos[1] = random.randint(10,420)


while gameloop:

	fps.tick(10)
	snake_pos = [screen_width/2 ,screen_height/2]
	snake_body = [[100,50],[90,50],[80,50]]
	snake_speed = [10,0] 
	speed = 15 

	# start_text = font1.render("Press SpaceBar To Start The Game", True, "Black")
	# start_text_rect = start_text.get_rect()
	# start_text_rect.center = screen_width/2 , screen_height/2
	# screen.fill("Green")
	# screen.blit(start_text,start_text_rect)
	# pygame.display.update()

	survive = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameloop = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				survive = True
				score = 0 

	while survive:
		fps.tick(15)
		snake_Rect = pygame.Rect((snake_pos[0],snake_pos[1]),(10,10))
		food_Rect = pygame.Rect((food_pos[0],food_pos[1]),(10,10))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameloop = False
				survive = False

			if event.type == pygame.KEYDOWN:
				snake_movements(event.key)

		snake_body.insert(0,[snake_pos[0],snake_pos[1]])
	
		if snake_Rect.colliderect(food_Rect):
			food_generation()
			score+=10
		else:
			snake_body.pop(-1)

		snake_pos[0] += snake_speed[0]
		snake_pos[1] += snake_speed[1]

		if snake_pos[0] >= screen_width or snake_pos[0] <= 0:
			survive = False
		elif snake_pos[1] >= screen_height or snake_pos[1] <= 0:
			survive = False


		screen.fill("green")

		for len in snake_body:
			pygame.draw.circle(screen, "BLUE", (len[0],len[1]), 7)
		img = font1.render(f'Gravity: {score}', True,"BLUE")
 
		screen.blit(img,img.get_rect())

		pygame.draw.circle(screen, "RED", (food_pos[0],food_pos[1]), 7)
		pygame.display.update()	

	screen.fill("green")
	# text = "Game Over"
	# Your_Score = "Your Score : " + str(score)
	img1  = font1.render(f"Game Over ",True,"BLACK")
	img_rect1 = img1.get_rect()
	img_rect1.center = screen_width/2,screen_height/2-60
	img2 =font1.render(f"Your Score : {score}", True, "BLACK" )
	img_rect2 = img2.get_rect()
	img_rect2.center = screen_width/2, screen_height/2  
	img3 =font1.render(f"Press Space To Start The Game", True, "BLACK" )
	img_rect3 = img3.get_rect()
	img_rect3.center = screen_width/2, screen_height/2 + 50  
	screen.blit(img1, img_rect1)
	screen.blit(img2, img_rect2)
	screen.blit(img3, img_rect3)

	pygame.display.update()

pygame.quit()
