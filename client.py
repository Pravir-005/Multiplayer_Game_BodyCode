import pygame
from network import Network

width = 500
height = 500

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Player:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 8

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect) 

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect.topleft = (self.x, self.y)


def readPose(pos):
    if not pos:
        return 0, 0
    try:
        x, y = pos.split(",")
        return int(x), int(y)
    except:
        return 0, 0


def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win, player, player2):
    win.fill((225, 225, 225))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()

    startPos = readPose(n.getPos())

    p = Player(startPos[0], startPos[1], 50, 50, (0, 0, 255))
    p2 = Player(0, 0, 50, 50, (0, 255, 0))

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not run:
            break

        p.move()

        response = n.send(makePos((p.x, p.y)))
        p2Pos = readPose(response)

        p2.x, p2.y = p2Pos
        p2.update()

        redrawWindow(win, p, p2)

    pygame.quit()


main()
