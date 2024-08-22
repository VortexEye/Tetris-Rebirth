import pygame, time
from game import Game

pygame.init()

Size = (400, 500)
board_size = (10, 20, 20)
screen = pygame.display.set_mode(Size)
pygame.display.set_caption("Tetris-Rebirth")

game = Game(board_size, screen)
game.run()

print("A Game by VortexEye")
time.sleep(1)
print("Thanks for playing!")
pygame.quit()

# Hallo! Ich schreibe diesen Text hier, weil und während ich nichts zu tun habe. Mir wird so langam wirklich sehr langweilig
# und ich weiß auch nicht mehr, was ich schreiben soll :(. Deshalb erzähle ich jetzt von dem Wetter: