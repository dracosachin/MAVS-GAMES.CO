import pygame,time,random
pygame.init()
ob_x=0
ob_y=0
obs_x=[]
obs_y=[]
black = (0,0,0)
white = (255,255,255)
game1=pygame.display.set_mode((800,600))
pygame.display.set_caption("Sample")
game1.fill(white)

for i in range(30):
		print(i)
		ob_x = round(random.randrange(0,600-10)/10.0)*10.0
		ob_y = round(random.randrange(0,600-10)/10.0)*10.0
		obs_x.append(ob_x)
		obs_y.append(ob_y)
		print(obs_x[i])
		print(obs_y[i])
		pygame.draw.rect(game1,black, [obs_x[i],obs_y[i],10,10])
		pygame.display.update()
