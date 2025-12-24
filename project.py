import pygame
import sys
import random
# =================================
#               CONFIG
# =================================
CELL = 20
WIDTH, HEIGHT = 600, 600
GRID_W, GRID_H = WIDTH // CELL, HEIGHT // CELL

MOVE_INTERVAL = 120
MIN_INTERVAL = 60
SPEED_FACTOR = 2

MOVE_EVENT = pygame.USEREVENT + 1

# =================================
#          REQUIRED FUNCTIONS
# =================================
def draw_block(surface, color, pos):
    """Draw a single block on the grid."""
    x, y = pos
    pygame.draw.rect(surface, color, (x* CELL, y* CELL, CELL, CELL ))

def spawn_food(snake):
    """Spawn food in a position not occupied by the snake."""
    while True:
        pos = (random.randint(0, GRID_W - 1), random.randint(0, GRID_H - 1))
        if pos not in snake:
            return pos

def load_highscore(path="highscore.txt"):
    """Load highscore from file."""
    try:
        with open(path, "r") as file:
            return int(file.read())
    except:
        return 0

def save_highscore(score, path="highscore.txt"):
    """Save highscore to file."""
    try:
        with open(path, "w") as file:
            file.write(str(score))
    except:
        pass

# =================================
#             GAME CLASS
# =================================
class SnakeGame:
    def __init__(self, screen, clock, font):
        self.screen= screen
        self.clock= clock
        self.font= font
        self.highscore= load_highscore()
        self.reset()

    def reset(self):
        self.snake=[(10,10),(9,10),(8,10)]
        self.direction=(1,0)
        self.food= spawn_food(self.snake)
        self.score= 0
        self.interval= MOVE_INTERVAL
        self.game_over= False
        self.paused= False
        pygame.time.set_timer(MOVE_EVENT,self.interval)

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != (0,1):
            self.direction = (0,-1)
        elif key== pygame.K_DOWN and self.direction !=(0,-1):
            self.direction  = (0,1)
        elif key == pygame.K_LEFT and self.direction != (1,0):
            self.direction= (-1,0)
        elif key== pygame.K_RIGHT and self.direction !=(-1,0):
            self.direction= (1,0)
    def update(self):
        if self.paused or self.game_over:
            return
        head_x,head_y = self.snake[0]
        dx,dy= self.direction
        new_head=(head_x + dx, head_y + dy)
        if (
            new_head in self.snake
            or new_head[0]< 0 or new_head[0]>= GRID_W
            or new_head[1]<0 or new_head[1]>= GRID_H

        ):
            self.game_over= True
            return
        if new_head== self.food:
            self.snake.insert(0,new_head)
            self.score+=1
            self.food= spawn_food(self.snake)

            self.interval= max(
                MIN_INTERVAL, MOVE_INTERVAL - self.score *  SPEED_FACTOR
            )
            pygame.time.set_timer(MOVE_EVENT,self.interval)

            if self.score > self.highscore:
                self.highscore= self.score

        else:
            self.snake.insert(0,new_head)
            self.snake.pop()

    def draw(self):
        self.screen.fill((10,10,30))
        draw_block(self.screen,(255,50,50),self.food)

        for segment in self.snake:
            draw_block(self.screen,(0,200,0),segment)

        score_text= self.font.render(f"score:{self.score}",True,(255,255,255))
        high_text= self.font.render(
            f"Highscore:{self.highscore}",True,(255,255,0)
        )
        self.screen.blit(score_text,(10,10))
        self.screen.blit(high_text,(10,40))

        if self.paused:
            pause_text = self.font.render(
                "PAUSED - Press P to resume",True , (255,200,0)
            )
            self.screen.blit(pause_text,(150,HEIGHT // 2))

        if self.game_over:
            over_text= self.font.render(
                "GAME OVER - Press R to restart",True,(255,50,50)
            )
            self.screen.blit(over_text,(120,HEIGHT // 2))

        pygame.display.flip()

    def run(self):
        print("GAME STARTED")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_highscore(self.highscore)
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_p:
                        self.paused = not self.paused
                    elif event.key == pygame.K_r:
                        self.reset()
                    elif event.key == pygame.K_q:
                        save_highscore(self.highscore)
                        pygame.quit()
                        sys.exit()
                    else:
                        self.change_direction(event.key)
                if event.type == MOVE_EVENT:
                    self.update()


            self.draw()
            self.clock.tick(60)
#================================
#           main
#================================
def main():
    pygame.init()
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("SNAKE GAME - CS50P Final project")
    clock= pygame.time.Clock()
    font= pygame.font.SysFont(None, 32)

    game=SnakeGame(screen,clock,font)
    game.run()

if __name__=="__main__":
    main()
