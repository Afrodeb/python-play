import pygame #1
 
#2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

x_coord = 50
y_coord = 45
x_speed = 0
y_speed = 0

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

 
#3
pygame.init()
 
#4
size = (700, 500)

#5
screen = pygame.display.set_mode(size) 

#6 
pygame.display.set_caption("My Game")
 
#6
done = False
 
#7
clock = pygame.time.Clock()
screen.fill(WHITE)
#
pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # Move the object according to the speed vector.
x_coord = x_coord + x_speed
y_coord = y_coord + y_speed
 
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
draw_stick_figure(screen, x_coord, y_coord)



#8
while not done:
    #9
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 #10
    
	
	

#11 
    pygame.display.flip()
 
#12
    clock.tick(60)
 
#13 
pygame.quit()