import pygame
import time
import sys

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

class Game_Manager(object):
    """ Handles all the game objects,
        and manages the game stuff!!!"""
    def __init__(self, settings):
        self.settings = settings
        self.player = None
        self.actors = []
        self.objects = []
        self.running = True
        self.background = GameObject(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,"images/test_background_DO_NOT_SHIP.jpg")
        self.background.resize(1024, 768)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bounds = self.screen.get_rect()

        pygame.init()
        pygame.display.set_caption("Top Down Game")

    def add_player(self, player):
        self.player = player

    def start_loop(self):
        while self.running == True:
            ## HANDLE EVENTS
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        sys.exit()
                        break
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.player.move_right()
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.player.move_left()
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self.player.move_up()
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.player.move_down()
                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.player.stop_move_right()
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.player.stop_move_left()
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self.player.stop_move_up()
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.player.stop_move_down()

            ## UPDATE PHYSICS AND POSITION
            self.player.update()

            ## DISPLAY ALL OBJECTS

            ## BACKGROUND
            self.background.draw(self.screen)
            ## PLAYER
            self.player.draw(self.screen)

            pygame.display.flip()

            time.sleep(0.01)

class GameObject(object):
    def __init__(self, x, y, image_file):
        self.x = x
        self.y = y
        self.image_file = image_file
        self.image = pygame.image.load(self.image_file)

    def draw(self, surface):
        ## Draws to actual game coordinates
        surface.blit(self.image, (self.x-self.image.get_width()/2, SCREEN_HEIGHT-self.y-self.image.get_height()/2))

    def resize(self, new_width, new_height):
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def get_rect(self):
        self.rect = self.image.get_rect()
        return self.rect

    def is_collided_with(self, target):
        rect1 = self.image.get_rect()
        rect1.topleft = (self.x,self.y)
        rect2 = target.image.get_rect()
        rect2.topleft = (target.x, target.y)
        return rect1.colliderect(rect2)

class Player(GameObject):
    def __init__(self, x, y, image_file):
        super().__init__(x, y, image_file)
        self.vx = 0
        self.vy = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy
        print ("player tick")

    def move_right(self):
        self.vx = 4

    def move_left(self):
        self.vx = -4

    def move_up(self):
        self.vy = 4

    def move_down(self):
        self.vy = -4

    def stop_move_right(self):
        self.vx = 0

    def stop_move_left(self):
        self.vx = 0

    def stop_move_up(self):
        self.vy = 0

    def stop_move_down(self):
        self.vy = 0


def test_game():
    p = Player(512,512,"images/player.png")
    manager = Game_Manager()
    manager.add_player(p)
    manager.start_loop()

if __name__ == "__main__":
    test_game()

