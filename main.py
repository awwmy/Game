from pygame import *

window = display.set_mode((800,600))
picture = transform.scale(image.load("fon.webp"),(800,600))
player1 = transform.scale(image.load("lina.png"),(150,150))
player2 = transform.scale(image.load("crystalmaiden.png"),(150,150))

clock = time.Clock()
x1,y1 = 100,100
x2,y2 = 200,200
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 





    window.blit(picture,(0,0))
    window.blit(player1,(x1,y1))
    window.blit(player2,(x2 ,y2))

    key_presed = key.get_pressed()
    if key_presed[K_LEFT] and x1 > 0:
        x1 -= 5
    if key_presed[K_RIGHT] and x1 < 650:
        x1 += 5
    if key_presed[K_d] and x2 > 0:
        x2 += 5
    if key_presed[K_a] and x2 < 650:
        x2 -= 5
    if key_presed[K_UP] and y1 > 0:
        y1 -= 5
    if key_presed[K_DOWN] and y1 < 450:
        y1 += 5
    if key_presed[K_w] and y2 > 0:
        y2 -= 5
    if key_presed[K_s] and y2 < 450:
        y2 += 5

    display.update()
    clock.tick(60)