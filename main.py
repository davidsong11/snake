'''
Rules and Features of Snake
Apple:
- makes you grow by 1 
- random but never on top of the snake
- regenerated after eaten

Snake:
- the head cannot run INTO wall or self
- counter for the apples (points for how many apples)
- win by filling up grid
- goes forward no matter what
- press direction key to change direction
- head moves in direction, and everything follows the head

Game world or state:
- 2D array, square 10x10
- how to represent the snake (2 in grid)
    a list of body parts:
    [
        (0,1),
        (0,2),
        (0,3),
        (1,3),
        (2,3),
    ]
- how to represent apple (1 in grid)
    ordered pair for the apple 
    (5,5)
- score
- direction 

Implement the mechanics:
- how to regenerate apple?
    set another 1 to a new ordered pair, both random integers between 0,9 (inclusive)
    while (r,c) in snake:
        choose again?
- how to move the snake?
    two things:
    1. added direction to the head of the snake
    
    e.g.
    get me the head of snake: (2,3)
    add the direction to the head: (1,0)
    get new head (3,3)
    check if head is inside body or the wall or if eating apple 
    add new head to the end

    row goes up by 1, and column doesnt change
    down => (1,0)
    up => (-1,0)
    left => (0,-1)
    right => (0,1) 

    2. deleted the last one (unless eating apple), farthest coord from head, the tail, the first element
'''

'''
    Snake AI:
    The snake knows:
    - where teh food is
    - where the boundaries are
    - where the body is
    - which direction it is going

    The snake can do:
    - change direction
'''

import pygame
from random import randint
pygame.init()
surface = pygame.display.set_mode((500,500))

# Constants
INITIAL_GAME = [
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
]

S = 50

DOWN = (1,0)
UP = (-1,0)
LEFT = (0,-1)
RIGHT = (0,1)

# Initialization
game = INITIAL_GAME
snake = [
  (5,5)
]
apple = (3,5)
dire = UP
score = 0

while True:
  # Clear surface
  surface.fill((0,0,0))
  # Duration of each frame
  pygame.time.wait(300)

#   pygame.event.pump()
#   keys = pygame.key.get_pressed()
#   if keys[pygame.K_d]:
#     if dire != LEFT:
#       dire = RIGHT
#   if keys[pygame.K_a]:
#     if dire != RIGHT:
#       dire = LEFT
#   if keys[pygame.K_w]:
#     if dire != DOWN:
#       dire = UP
#   if keys[pygame.K_s]:
#     if dire != UP:
#       dire = DOWN

  # ordered pairs: (3,7)
  head = snake[-1]
  if head[0] < apple[0]:
    if dire != UP:
      dire = DOWN
  if head[0] > apple[0]:
    if dire != DOWN:
      dire = UP
  if head[1] < apple[1]:
    if dire != LEFT:
      dire = RIGHT
  if head[1] > apple[1]:
    if dire != RIGHT:
      dire = LEFT 


  if head[0] == apple[0]:
    if (head[1] < apple[1] and dire == LEFT) or (head[1] > apple[1] and dire == RIGHT):
      if head[0] == 9:
        dire = UP
      else:
        dire = DOWN
  elif head[1] == apple[1]:
    if (head[0] < apple[0] and dire == UP) or (head[0] > apple[0] and dire == DOWN):
      if head[1] == 9:
        dire = LEFT
      else:
        dire = RIGHT



  # Moving the snake will change the variable snake (which is the list)
  
  # Add new head
  print(dire)
  newhead = (head[0]+dire[0], head[1]+dire[1])

  # is newhead inside body?
  if newhead in snake:
    print('Game over! Tried to eat self!')
    break

  # is newhead out of bounds?
  if newhead[0] == 10 or newhead[0] == -1 or newhead[1] == -1 or newhead[1] == 10:
    print('Game over! You Lost!')
    break

  snake.append(newhead)

  # is newhead over the apple
  if newhead == apple:
    # generate new apple
    apple = (randint(0,9), randint(0,9))
    while apple in snake:
      apple = (randint(0,9), randint(0,9))
  else:  
    #Delete tail
    snake.pop(0)
  
  # After moving snake or apple,
  # update the game grid
  for r in range(10):
    for c in range(10):
      game[r][c] = 0

  applerow, applecol = apple
  game[applerow][applecol] = 1

  for x in snake:
    snakerow, snakecol = x
    game[snakerow][snakecol] = 2

  # After we have updated the game grid,
  # render the game grid
  for r in range(10):
    for c in range(10):
      if game[r][c] == 2:
        pygame.draw.rect(surface, (255,255,255), (S*c+2, S*r+2, S-4, S-4))
      elif game[r][c] == 1:
        pygame.draw.rect(surface, (255,0,0), (S*c+2, S*r+2, S-4, S-4))

        # [[],[],[],[],[]]
        
  pygame.display.update()

