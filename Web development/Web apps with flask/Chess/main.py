import pygame as gm
## here i am importing pygame

gm.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

board_width = 600
board_height = 600

logo_width = 75
logo_height = 75

step_size = 75

logo_x = 225
logo_y = 225

logo_direction = ""

chessboard = gm.display.set_mode([board_width,board_height])
gm.display.set_caption("Chessboooooooooaaaaaaarrrrrrrrrrd")
chessboard.fill(BLACK)
chessboard.fill(WHITE) 
running = True
button_pressed = False
while running:
    for event in gm.event.get():
        if event.type == gm.QUIT:
            running = False
        elif event.type == gm.KEYDOWN:
            if event.key == gm.K_RIGHT and not button_pressed:
                logo_x += step_size
                if logo_x > board_width - logo_width:
                    logo_x = board_width - logo_width 
                button_pressed = True
            elif event.key == gm.K_LEFT and not button_pressed:
                logo_x -= step_size
                if logo_x < 0:
                    logo_x = 0
                button_pressed = True
            elif event.key == gm.K_UP and not button_pressed:
                logo_y -= step_size
                if logo_y < 0:
                    logo_y = 0
                button_pressed = True
    chessboard.fill(BLACK)
    for row in  (0,board_height,step_size):
        for col in (0,board_width,step_size):
            if (row,col) // step_size % 2 == 0:
                gm.draw.rect(chessboard,WHITE,(col,row,step_size,step_size))
            else:
                gm.draw.rect(chessboard,BLACK,(col,row,step_size,step_size))

    gm.draw.rect(chessboard,WHITE,(logo_x,logo_y,logo_width,logo_height))

                    



    print("logo direction: ",logo_direction)


    gm.display.update()

    gm.display.flip()
gm.quit()