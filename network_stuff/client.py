import pygame
from network import Network
from player import Player

width=500
height=500
win=pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")


def redrawWindow(win, player, others):
    win.fill((255,255,255))
    player.draw(win)
    for other in others:
        other.draw(win)
    pygame.display.update()
    

def main():
    run=True
    n=Network()

    p=n.getP()

    clock=pygame.time.Clock()

    while run:
        clock.tick(60)

        others=n.send(p)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
            
        p.move()
        redrawWindow(win, p, others)

if __name__=="__main__":
    main()