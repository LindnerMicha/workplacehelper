import pygame
import sys

pygame.init()
w, h = 1200, 900
screen = pygame.display.set_mode((w, h))
runtime = True

global option

screen = pygame.display.set_mode([w, h])
pygame.display.set_caption("Workplace Helper")
clock = pygame.time.Clock()
fps = 60

option = " "

mlfb_digital = [["131-6BF00-0CA0", "73643", "A5E45983869"],
                ["131-6BF00-0DA0", "73643", "A5E45983869"],
                ["131-6BF01-0AA0", "69488", "A5E37018268"],
                ["131-6BF01-0BA0", "69486", "A5E36861757"],
                ["131-6BH01-0BA0", "69485", "A5E36775154"],

                ["132-6BD20-0BA0", "73644", "A5E45998818"],
                ["132-6BF00-0CA0", "69388", "A5E35772026"],
                ["132-6BF01-0AA0", "69489", "A5E37061405"],
                ["132-6BF01-0BA0", "82466", "A5E51753289"],
                ["132-6BF61-0AA0", "75900", "A5E37757230"],
                ["132-6BH00-0AA0", "75792", "A5E38882505"],
                ["132-6BH01-0BA0", "82467", "A5E51756149"]]
mlfb_analog =  [["134-6FB00-0BA1", "75967", "A5E35649239", " ", " ", "37", " ", 0],
                ["134-6FF00-0AA1", "77127", "A5E34098222", " ", " ", "37", " ", 1],
                ["134-6GB00-0BA1", "75786", "A5E35649001", "37", " ", "39", " ", 0],
                ["134-6GD01-0BA1", "73654", "A5E46004518", "37", " ", "37", "37", 0],
                ["134-6GF00-0AA1", "69385", "A5E34097886", "37", " ", "37", "37", 0],
                ["134-6HB00-0CA1", "69484", "A5E37970403", "39", "3", "39", "3", 1],
                ["134-6HB00-0DA1", "77532", "A5E50585786", "39", " ", "39", "37", 0],
                ["134-6HD01-0BA1", "73655", "A5E46004505", "37", " ", "37", "37", 0],
                ["134-6JD00-0CA1", "71259", "A5E38837676", "33/39", "1", "41/45", "1", 1],

                ["135-6GB00-0BA1", "77129", "A5E35652111", " ", " ", "37", " ", 1],
                ["135-6HB00-0CA1", "69482", "A5E32562703", "37", "4", "37", "37", 1],
                ["135-6HB00-0DA1", "69481", "A5E35652111", "37", "4", "37", "37", 1],
                ["135-6HD00-0BA1", "69249", "A5E31290169", "37", "4", "37", "37", 0]]

#region      -> Fonts
pixel_font60 = pygame.font.Font("fonts/PixeloidSans.ttf", 60)
pixel_font30 = pygame.font.Font("fonts/PixeloidSans.ttf", 30)
pixel_font22 = pygame.font.Font("fonts/PixeloidSans.ttf", 22)
pixel_font15 = pygame.font.Font("fonts/PixeloidSans.ttf", 15)
sys_font15 = pygame.font.SysFont(None, 15)
sys_font22 = pygame.font.SysFont(None, 22)
sys_font30 = pygame.font.SysFont(None, 30)
sys_font60 = pygame.font.SysFont(None, 60)
#endregion
#region -> Button
def textObjekt(text, pixel_font15):
    textFlaeche = pixel_font15.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option

    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            option = but_txt
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)
#endregion
#region -> Funktionen
def draw_text(text, sys_font15, color, screen, x , y):
    textobj = sys_font15.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

def baugruppen():
    pygame.draw.rect(screen, (168, 165, 165), (0,0,w, 60))
    button(mlfb_digital[0][0], 0, 60, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[1][0], 0, 90, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[2][0], 0, 120, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[3][0], 0, 150, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[4][0], 0, 180, 300, 30, (155,150,100), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,210,300, 30))
    button(mlfb_digital[5][0], 0, 240, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[6][0], 0, 270, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[7][0], 0, 300, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[8][0], 0, 330, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[9][0], 0, 360, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[10][0], 0, 390, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_digital[11][0], 0, 420, 300, 30, (155,150,100), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,450,300, 30))
    button(mlfb_analog[0][0], 0, 480, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[1][0], 0, 510, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[2][0], 0, 540, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[3][0], 0, 570, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[4][0], 0, 600, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[5][0], 0, 630, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[6][0], 0, 660, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[7][0], 0, 690, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[8][0], 0, 720, 300, 30, (155,150,100), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,750,300, 30))
    button(mlfb_analog[9][0], 0, 780, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[10][0], 0, 810, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[11][0], 0, 840, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(mlfb_analog[12][0], 0, 870, 300, 30, (155,150,100), (0,100,255), sys_font22)

    draw_text("PEMO's", sys_font60, (0,0,0), screen, 675 , 80)
    draw_text(option, sys_font30, (0,0,0), screen, 675 , 140)

    draw_text("SP1", sys_font30, (0,0,0), screen, 370 , 235)
    pygame.draw.rect(screen, (168, 165, 165), (460,200,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (660,200,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (860,200,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (1050,200,85, 85))

    draw_text("SP2", sys_font30, (0,0,0), screen, 370 , 335)
    pygame.draw.rect(screen, (168, 165, 165), (460,300,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (660,300,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (860,300,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (1050,300,85, 85))

    draw_text("Vorwärme", sys_font30, (0,0,0), screen, 310 , 435)
    pygame.draw.rect(screen, (168, 165, 165), (460,400,85, 85))

    if option == mlfb_analog[0][0] and mlfb_analog[0][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[0][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[1][0] and mlfb_analog[1][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[1][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[2][0] and mlfb_analog[2][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[2][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[3][0] and mlfb_analog[3][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[3][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[4][0] and mlfb_analog[4][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[4][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[5][0] and mlfb_analog[5][7]:
        pygame.draw.rect(screen, (5, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[5][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[6][0] and mlfb_analog[6][7]:
        pygame.draw.rect(screen, (6, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[6][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[7][0] and mlfb_analog[7][7]:
        pygame.draw.rect(screen, (7, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[7][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[8][0] and mlfb_analog[8][7]:
        pygame.draw.rect(screen, (8, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[8][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[9][0] and mlfb_analog[9][7]:
        pygame.draw.rect(screen, (9, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[9][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[10][0] and mlfb_analog[10][7]:
        pygame.draw.rect(screen, (7, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[10][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[11][0] and mlfb_analog[11][7]:
        pygame.draw.rect(screen, (8, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[11][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_analog[12][0] and mlfb_analog[12][7]:
        pygame.draw.rect(screen, (9, 255, 0), (460,400,85, 85))
    elif option == mlfb_analog[12][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))

    if option == mlfb_analog[0][0]:
        draw_text(mlfb_analog[0][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[0][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[0][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[0][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[0][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[0][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[0][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[0][5], sys_font30, (0,0,0), screen, 1080 , 330)

        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[0][1], sys_font30, (0,0,0), screen, 460 , 550)


    if option == mlfb_analog[1][0]:
        draw_text(mlfb_analog[1][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[1][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[1][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[1][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[1][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[1][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[1][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[1][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[2][0]:
        draw_text(mlfb_analog[2][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[2][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[2][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[2][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[2][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[2][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[2][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[2][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[3][0]:
        draw_text(mlfb_analog[3][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[3][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[3][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[3][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[3][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[3][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[3][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[3][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[4][0]:
        draw_text(mlfb_analog[4][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[4][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[4][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[4][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[4][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[4][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[4][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[4][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[5][0]:
        draw_text(mlfb_analog[5][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[5][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[5][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[5][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[5][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[5][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[5][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[5][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[6][0]:
        draw_text(mlfb_analog[6][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[6][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[6][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[6][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[6][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[6][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[6][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[6][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[7][0]:
        draw_text(mlfb_analog[7][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[7][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[7][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[7][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[7][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[7][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[7][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[7][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[8][0]:
        draw_text(mlfb_analog[8][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[8][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[8][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[8][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[8][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[8][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[8][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[8][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[9][0]:
        draw_text(mlfb_analog[9][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[9][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[9][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[9][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[9][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[9][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[9][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[9][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[10][0]:
        draw_text(mlfb_analog[10][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[10][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[10][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[10][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[10][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[10][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[10][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[10][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[11][0]:
        draw_text(mlfb_analog[11][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[11][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[11][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[11][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[11][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[11][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[11][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[11][5], sys_font30, (0,0,0), screen, 1080 , 330)
    if option == mlfb_analog[12][0]:
        draw_text(mlfb_analog[12][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[12][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[12][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[12][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[12][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[12][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[12][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[12][5], sys_font30, (0,0,0), screen, 1080 , 330)

def marker():
    if option == mlfb_analog[0][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,485,15,15])
    if option == mlfb_analog[1][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,510,15,15])
    if option == mlfb_analog[2][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,545,15,15])
    if option == mlfb_analog[3][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,575,15,15])
    if option == mlfb_analog[4][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,605,15,15])
    if option == mlfb_analog[5][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,635,15,15])
    if option == mlfb_analog[6][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,665,15,15])
    if option == mlfb_analog[7][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,695,15,15])
    if option == mlfb_analog[8][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,725,15,15])
    if option == mlfb_analog[9][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,785,15,15])
    if option == mlfb_analog[10][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,815,15,15])
    if option == mlfb_analog[11][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,845,15,15])
    if option == mlfb_analog[12][0]:
        pygame.draw.ellipse(screen, (255,0,0), [300,875,15,15])


#endregion

while runtime:

    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False
    if pressed[pygame.K_SPACE]:
            runtime = False


    screen.fill((255, 255, 255))
    baugruppen()
    marker()

    pygame.display.flip()
    clock.tick(fps)
