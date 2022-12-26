import pygame
import sys
import time
from urllib import request
import tkinter as tk

pygame.init()
w, h = 1200, 900
screen = pygame.display.set_mode((w, h))
runtime = True

global option
global sites

screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

screen = pygame.display.set_mode([w, h])
pygame.display.set_caption("Workplace Helper")
s_icon = pygame.image.load("icon/slogo.png").convert_alpha()
pygame.display.set_icon(s_icon)
clock = pygame.time.Clock()
fps = 60

option = " "
sites = "Material"
scan_switch = "Leiterplatte"


save_dir = "C:\\Users\\micha\\Desktop\\python_log.txt"




font = pygame.font.Font(None, 32)
input_box = pygame.Rect(400, 100, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False
suche_em = False
suche_string = " "
a5e_erg = ""

html_index_min = 0
html_index_max = 0

set_error = False
erg_gefunden = False


background_r = 255
background_g = 255
background_b = 255
plus_minus = " "

buttoncolor_r = 155
buttoncolor_g = 150
buttoncolor_b = 108
#155, 150, 100

topbar_r = 168
topbar_g = 165
topbar_b = 165

text_r = 0
text_g = 0
text_b = 0






mlfb_digital = [["131-6BF00-0CA0", "73643", "A5E45983869", " ", " ", " ", " ", 0],
                ["131-6BF00-0DA0", "73643", "A5E45983869", " ", " ", " ", " ", 0],
                ["131-6BF01-0AA0", "69488", "A5E37018268", " ", " ", " ", " ", 0],
                ["131-6BF01-0BA0", "69486", "A5E36861757", " ", " ", " ", " ", 0],
                ["131-6BH01-0BA0", "69485", "A5E36775154", " ", " ", " ", " ", 0],

                ["132-6BD20-0BA0", "73644", "A5E45998818", " ", " ", " ", " ", 0],
                ["132-6BF00-0CA0", "69388", "A5E35772026", " ", " ", " ", " ", 0],
                ["132-6BF01-0AA0", "69489", "A5E37061405", " ", " ", " ", " ", 0],
                ["132-6BF01-0BA0", "82466", "A5E51753289", " ", " ", " ", " ", 0],
                ["132-6BF61-0AA0", "75900", "A5E37757230", " ", " ", " ", " ", 0],
                ["132-6BH00-0AA0", "75792", "A5E38882505", " ", " ", " ", " ", 0],
                ["132-6BH01-0BA0", "82467", "A5E51756149", " ", " ", " ", " ", 0]]

mlfb_analog =  [["134-6FB00-0BA1", "75967", "A5E35649239", " ", " ", "37", " ", 0],
                ["134-6FF00-0AA1", "77127", "A5E34098222", " ", " ", "37", " ", 1],
                ["134-6GB00-0BA1", "75786", "A5E35649001", "37", " ", "39", " ", 0],
                ["134-6GD01-0BA1", "73654", "A5E46004518", "37", " ", "37", "37", 0],
                ["134-6GF00-0AA1", "69385", "A5E34097886", "37", " ", "37", "37", 0],
                ["134-6HB00-0CA1", "69484", "A5E37970403", "39", "3", "39", "3", 1],
                ["134-6HB00-0DA1", "77532", "A5E50585786", "39", " ", "39", "37", 0],
                ["134-6HD01-0BA1", "73655", "A5E46004505", "37", " ", "37", "37", 0],
                ["134-6JD00-0CA1", "71259", "A5E38837676", "33", "1", "41", "1", 1, "49", "45"],

                ["135-6GB00-0BA1", "77129", "A5E35652111", " ", " ", "37", " ", 1],
                ["135-6HB00-0CA1", "69482", "A5E32562703", "37", "4", "37", "37", 1],
                ["135-6HB00-0DA1", "69481", "A5E35652111", "37", "4", "37", "37", 1],
                ["135-6HD00-0BA1", "69249", "A5E31290169", "37", "4", "37", "37", 0]]

materials = [["Frontdeckel Dunkelblau", "65325", "A5E36039007", "3196 St.", "2970 St."],
             ["Frontdeckel Hellblau", "65260", "A5E36039005", "3196 St.", "2970 St."],
             ["Frontdeckel Schwarz", "65189", "A5E36039004", "3196 St.", "2970 St."],
             ["Frontdeckel Weiß", "65257", "A5E36039003", "3196 St.", "2970 St."],
             ["Gehäuse 15mm", "63167", "A5E03387374", "925 St.", "3700 St."],
             ["Codierung A (Schwarz)", "75504", "A5E03392060", "1500 St.", "8000 St."],
             ["Codierung B (Weiß)", "75505", "A5E03392061", "1500 St.", "8000 St."],
             ["Schachtel 15mm", "63448", "A5E03749927", "720 St.", "2880 St."],
             ["Schachtel 10-fach", "64176", "A5E34858449", "360 St.", "170 St."],
             ["Etiketten 60x70", "AAB", "EWA-000000429125", "2000 St.", " "],
             ["Thermotransferband", "AAB", "EWA-000000535789", "1 St.", " "],
             ["Papiertücher (Blau)", "AAB", "EWA-000000429203", "200 St.", " "],
             ["Thermotransferband", "AAB", "EWA-000000535789", "1 St.", " "],
             ["1.6mm Fräser", "AAB", "A5E49854071", "1 St.", " "]]

#region -> Barcodes
front_black_img = pygame.image.load("barcodes/front-schwarz.gif").convert_alpha()
front_white_img = pygame.image.load("barcodes/front-weiß.gif").convert_alpha()
front_hblue_img = pygame.image.load("barcodes/front-hblue.gif").convert_alpha()
front_dblue_img = pygame.image.load("barcodes/front-dblue.gif").convert_alpha()
cod_a_img = pygame.image.load("barcodes/cod-a.gif").convert_alpha()
cod_b_img = pygame.image.load("barcodes/cod-b.gif").convert_alpha()
geh_15_img = pygame.image.load("barcodes/geh-15.gif").convert_alpha()
schach_15_img = pygame.image.load("barcodes/schach-15.gif").convert_alpha()
schach_10_f_img = pygame.image.load("barcodes/schach-10f.gif").convert_alpha()
e4_leer_img = pygame.image.load("barcodes/e4-leer.gif").convert_alpha()
#endregion

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
    textFlaeche = pixel_font15.render(text, True, (text_r, text_g,text_b))
    return textFlaeche, textFlaeche.get_rect()

def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option
    global sites
    global scan_switch

    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            option = but_txt

            if but_txt == "Baugruppen":
                sites = "Baugruppen"
            elif but_txt == "Material":
                sites = "Material"
            elif but_txt == "Exit":
                sites = "Exit"
            elif but_txt == "Suchen":
                sites = "Suchen"
            elif but_txt == "Settings":
                sites = "Settings"
            elif but_txt == "Leiterplatte":
                scan_switch = "Leiterplatte"
            elif but_txt == "Baugruppe":
                scan_switch = "Baugruppe"
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)

def button_setting(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option_setting
    global set_0_r
    global set_0_g
    global set_0_b
    global background_r
    global background_g
    global background_b
    global buttoncolor_r
    global buttoncolor_g
    global buttoncolor_b
    global topbar_r
    global topbar_g
    global topbar_b
    global text_r
    global text_g
    global text_b

    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if option == "Backgroundcolor":
                if but_txt == "+" and but_y == 100:
                    option_setting = "+"
                    if background_r < 255:
                        background_r += 1
                    else:
                        background_r = 0
                elif but_txt == "-" and but_y == 100:
                    option_setting = "-"
                    if background_r > 0:
                        background_r -= 1
                    else:
                        background_r = 255
                if but_txt == "+" and but_y == 150:
                    option_setting = "+"
                    if background_g < 255:
                        background_g += 1
                    else:
                        background_g = 0
                elif but_txt == "-" and but_y == 150:
                    option_setting = "-"
                    if background_g > 0:
                        background_g -= 1
                    else:
                        background_g = 255
                if but_txt == "+" and but_y == 200:
                    option_setting = "+"
                    if background_b < 255:
                        background_b += 1
                    else:
                        background_b = 0
                elif but_txt == "-" and but_y == 200:
                    option_setting = "-"
                    if background_b > 0:
                        background_b -= 1
                    else:
                        background_b = 255

                if but_txt == "set 0" and but_y == 100:
                    background_r = 0
                elif but_txt == "set 255" and but_y == 100:
                    background_r = 255
                if but_txt == "set 0" and but_y == 150:
                    background_g = 0
                elif but_txt == "set 255" and but_y == 150:
                    background_g = 255
                if but_txt == "set 0" and but_y == 200:
                    background_b = 0
                elif but_txt == "set 255" and but_y == 200:
                    background_b = 255

                if but_txt == "Save":
                    print("Test Save")
                    file = open(save_dir,'w+')
                    file.write(f"{background_r},{background_g},{background_b},{buttoncolor_r},{buttoncolor_g},{buttoncolor_b},{topbar_r},{topbar_g},{topbar_b},{text_r},{text_g},{text_b}")
                if but_txt == "Set to Default":
                    background_r = 255
                    background_g = 255
                    background_b = 255
                    file = open(save_dir,'w+')
                    file.write(f"{background_r},{background_g},{background_b},{buttoncolor_r},{buttoncolor_g},{buttoncolor_b},{topbar_r},{topbar_g},{topbar_b},{text_r},{text_g},{text_b}")
            elif option == "Buttoncolor":
                if but_txt == "+" and but_y == 100:
                    option_setting = "+"
                    if buttoncolor_r < 255:
                        buttoncolor_r += 1
                    else:
                        buttoncolor_r = 0
                elif but_txt == "-" and but_y == 100:
                    option_setting = "-"
                    if buttoncolor_r > 0:
                        buttoncolor_r -= 1
                    else:
                        buttoncolor_r = 255
                if but_txt == "+" and but_y == 150:
                    option_setting = "+"
                    if buttoncolor_g < 255:
                        buttoncolor_g += 1
                    else:
                        buttoncolor_g = 0
                elif but_txt == "-" and but_y == 150:
                    option_setting = "-"
                    if buttoncolor_g > 0:
                        buttoncolor_g -= 1
                    else:
                        buttoncolor_g = 255
                if but_txt == "+" and but_y == 200:
                    option_setting = "+"
                    if buttoncolor_b < 255:
                        buttoncolor_b += 1
                    else:
                        buttoncolor_b = 0
                elif but_txt == "-" and but_y == 200:
                    option_setting = "-"
                    if buttoncolor_b > 0:
                        buttoncolor_b -= 1
                    else:
                        buttoncolor_b = 255

                if but_txt == "set 0" and but_y == 100:
                    buttoncolor_r = 0
                elif but_txt == "set 255" and but_y == 100:
                    buttoncolor_r = 255
                if but_txt == "set 0" and but_y == 150:
                    buttoncolor_g = 0
                elif but_txt == "set 255" and but_y == 150:
                    buttoncolor_g = 255
                if but_txt == "set 0" and but_y == 200:
                    buttoncolor_b = 0
                elif but_txt == "set 255" and but_y == 200:
                    buttoncolor_b = 255

                if but_txt == "Save":
                    print("Test Save")
                    file = open(save_dir,'w+')
                    file.write(f"{background_r},{background_g},{background_b},{buttoncolor_r},{buttoncolor_g},{buttoncolor_b},{topbar_r},{topbar_g},{topbar_b},{text_r},{text_g},{text_b}")
                if but_txt == "Set to Default":
                    buttoncolor_r = 155
                    buttoncolor_g = 150
                    buttoncolor_b = 108
                    file = open(save_dir,'w+')
                    file.write(f"{background_r},{background_g},{background_b},{buttoncolor_r},{buttoncolor_g},{buttoncolor_b},{topbar_r},{topbar_g},{topbar_b},{text_r},{text_g},{text_b}")
            elif option == "Topbarcolor":
                if but_txt == "+" and but_y == 100:
                    option_setting = "+"
                    if topbar_r < 255:
                        topbar_r += 1
                    else:
                        topbar_r = 0
                elif but_txt == "-" and but_y == 100:
                    option_setting = "-"
                    if topbar_r > 0:
                        topbar_r -= 1
                    else:
                        topbar_r = 255
                if but_txt == "+" and but_y == 150:
                    option_setting = "+"
                    if topbar_g < 255:
                        topbar_g += 1
                    else:
                        topbar_g = 0
                elif but_txt == "-" and but_y == 150:
                    option_setting = "-"
                    if topbar_g > 0:
                        topbar_g -= 1
                    else:
                        topbar_g = 255
                if but_txt == "+" and but_y == 200:
                    option_setting = "+"
                    if topbar_b < 255:
                        topbar_b += 1
                    else:
                        topbar_b = 0
                elif but_txt == "-" and but_y == 200:
                    option_setting = "-"
                    if topbar_b > 0:
                        topbar_b -= 1
                    else:
                        topbar_b = 255

                if but_txt == "set 0" and but_y == 100:
                    topbar_r = 0
                elif but_txt == "set 255" and but_y == 100:
                    topbar_r = 255
                if but_txt == "set 0" and but_y == 150:
                    topbar_g = 0
                elif but_txt == "set 255" and but_y == 150:
                    topbar_g = 255
                if but_txt == "set 0" and but_y == 200:
                    topbar_b = 0
                elif but_txt == "set 255" and but_y == 200:
                    topbar_b = 255
                if but_txt == "Save":
                    print("Test Save")
                    file = open(save_dir,'w+')
                    file.write(f"{background_r},{background_g},{background_b},{buttoncolor_r},{buttoncolor_g},{buttoncolor_b},{topbar_r},{topbar_g},{topbar_b},{text_r},{text_g},{text_b}")
                if but_txt == "Set to Default":
                    topbar_r = 168
                    topbar_g = 165
                    topbar_b = 165
                    file = open(save_dir,'w+')
                    file.write(f"{background_r},{background_g},{background_b},{buttoncolor_r},{buttoncolor_g},{buttoncolor_b},{topbar_r},{topbar_g},{topbar_b},{text_r},{text_g},{text_b}")
            elif option == "Textcolor":
                if but_txt == "+" and but_y == 100:
                    option_setting = "+"
                    if text_r < 255:
                        text_r += 1
                    else:
                        text_r = 0
                elif but_txt == "-" and but_y == 100:
                    option_setting = "-"
                    if text_r > 0:
                        text_r -= 1
                    else:
                        text_r = 255
                if but_txt == "+" and but_y == 150:
                    option_setting = "+"
                    if text_g < 255:
                        text_g += 1
                    else:
                        text_g = 0
                elif but_txt == "-" and but_y == 150:
                    option_setting = "-"
                    if text_g > 0:
                        text_g -= 1
                    else:
                        text_g = 255
                if but_txt == "+" and but_y == 200:
                    option_setting = "+"
                    if text_b < 255:
                        text_b += 1
                    else:
                        text_b = 0
                elif but_txt == "-" and but_y == 200:
                    option_setting = "-"
                    if text_b > 0:
                        text_b -= 1
                    else:
                        text_b = 255

                if but_txt == "set 0" and but_y == 100:
                    text_r = 0
                elif but_txt == "set 255" and but_y == 100:
                    text_r = 255
                if but_txt == "set 0" and but_y == 150:
                    text_g = 0
                elif but_txt == "set 255" and but_y == 150:
                    text_g = 255
                if but_txt == "set 0" and but_y == 200:
                    text_b = 0
                elif but_txt == "set 255" and but_y == 200:
                    text_b = 255
                if but_txt == "Save":
                    file = open(save_dir,'w+')
                    file.write(f"{background_r},{background_g},{background_b},{buttoncolor_r},{buttoncolor_g},{buttoncolor_b},{topbar_r},{topbar_g},{topbar_b},{text_r},{text_g},{text_b}")
                if but_txt == "Set to Default":
                    text_r = 0
                    text_g = 0
                    text_b = 0
                    file = open(save_dir,'w+')
                    file.write(f"{background_r},{background_g},{background_b},{buttoncolor_r},{buttoncolor_g},{buttoncolor_b},{topbar_r},{topbar_g},{topbar_b},{text_r},{text_g},{text_b}")


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

def topbar():
    pygame.draw.rect(screen, (topbar_r, topbar_g, topbar_b), (0,0,w, 60))
    button("Baugruppen", 10, 8, 150, 45, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font30)
    button("Material", 200, 8, 150, 45, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font30)
    button("Suchen", 400, 8, 150, 45, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0, 100, 255), sys_font30)
    button("Settings", 800, 8, 150, 45, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0, 100, 255), sys_font30)
    button("Exit", 1030, 8, 150, 45, (186, 48, 48), (133, 1, 1), sys_font30)

def baugruppen():
    #region -> Buttons
    button(mlfb_digital[0][0], 0, 60, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[1][0], 0, 90, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[2][0], 0, 120, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[3][0], 0, 150, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[4][0], 0, 180, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,210,300, 30))
    button(mlfb_digital[5][0], 0, 240, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[6][0], 0, 270, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[7][0], 0, 300, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[8][0], 0, 330, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[9][0], 0, 360, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[10][0], 0, 390, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_digital[11][0], 0, 420, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,450,300, 30))
    button(mlfb_analog[0][0], 0, 480, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[1][0], 0, 510, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[2][0], 0, 540, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[3][0], 0, 570, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[4][0], 0, 600, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[5][0], 0, 630, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[6][0], 0, 660, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[7][0], 0, 690, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[8][0], 0, 720, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,750,300, 30))
    button(mlfb_analog[9][0], 0, 780, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[10][0], 0, 810, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[11][0], 0, 840, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(mlfb_analog[12][0], 0, 870, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    draw_text("PEMO's", sys_font60, (text_r,text_g,text_b), screen, 675 , 80)
    draw_text(option, sys_font30, (text_r,text_g,text_b), screen, 675 , 140)
    draw_text("SP1", sys_font30, (text_r,text_g,text_b), screen, 370 , 235)
    pygame.draw.rect(screen, (168, 165, 165), (460,200,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (660,200,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (860,200,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (1050,200,85, 85))
    draw_text("SP2", sys_font30, (text_r,text_g,text_b), screen, 370 , 335)
    pygame.draw.rect(screen, (168, 165, 165), (460,300,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (660,300,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (860,300,85, 85))
    pygame.draw.rect(screen, (168, 165, 165), (1050,300,85, 85))
    draw_text("Vorwärme", sys_font30, (text_r,text_g,text_b), screen, 310 , 435)
    pygame.draw.rect(screen, (168, 165, 165), (460,400,85, 85))
    #endregion
    #region -> Wärmeindec
    if option == mlfb_digital[0][0] and mlfb_digital[0][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[0][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[1][0] and mlfb_digital[1][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[1][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[2][0] and mlfb_digital[2][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[2][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[3][0] and mlfb_digital[3][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[3][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[4][0] and mlfb_digital[4][7]:
        pygame.draw.rect(screen, (0, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[4][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[5][0] and mlfb_digital[5][7]:
        pygame.draw.rect(screen, (5, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[5][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[6][0] and mlfb_digital[6][7]:
        pygame.draw.rect(screen, (6, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[6][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[7][0] and mlfb_digital[7][7]:
        pygame.draw.rect(screen, (7, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[7][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[8][0] and mlfb_digital[8][7]:
        pygame.draw.rect(screen, (8, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[8][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[9][0] and mlfb_digital[9][7]:
        pygame.draw.rect(screen, (9, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[9][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[10][0] and mlfb_digital[10][7]:
        pygame.draw.rect(screen, (7, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[10][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))
    if option == mlfb_digital[11][0] and mlfb_digital[11][7]:
        pygame.draw.rect(screen, (8, 255, 0), (460,400,85, 85))
    elif option == mlfb_digital[11][0]:
        pygame.draw.rect(screen, (255, 0, 0), (460,400,85, 85))

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
    #endregion
    #region -> UI Zeichnen
    if option == mlfb_digital[0][0]:
        draw_text(mlfb_digital[0][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[0][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[0][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[0][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[0][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[0][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[0][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[0][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[0][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[0][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[1][0]:
        draw_text(mlfb_digital[1][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[1][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[1][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[1][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[1][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[1][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[1][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[1][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[1][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[1][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[2][0]:
        draw_text(mlfb_digital[2][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[2][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[2][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[2][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[2][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[2][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[2][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[2][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[2][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[2][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[3][0]:
        draw_text(mlfb_digital[3][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[3][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[3][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[3][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[3][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[3][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[3][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[3][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[3][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[3][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[4][0]:
        draw_text(mlfb_digital[4][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[4][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[4][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[4][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[4][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[4][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[4][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[4][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[4][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[4][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[5][0]:
        draw_text(mlfb_digital[5][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[5][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[5][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[5][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[5][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[5][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[5][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[5][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[5][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[5][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[6][0]:
        draw_text(mlfb_digital[6][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[6][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[6][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[6][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[6][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[6][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[6][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[6][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[6][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[6][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[7][0]:
        draw_text(mlfb_digital[7][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[7][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[7][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[7][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[7][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[7][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[7][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[7][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[7][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[7][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[8][0]:
        draw_text(mlfb_digital[8][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[8][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[8][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[8][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[8][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[8][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[8][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[8][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[8][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[8][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[9][0]:
        draw_text(mlfb_digital[9][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[9][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[9][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[9][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[9][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[9][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[9][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[9][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[9][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[9][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[10][0]:
        draw_text(mlfb_digital[10][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[10][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[10][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[10][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[10][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[10][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[10][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[10][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[10][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[10][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_digital[11][0]:
        draw_text(mlfb_digital[11][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_digital[11][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_digital[11][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_digital[11][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_digital[11][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_digital[11][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_digital[11][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_digital[11][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_digital[11][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_digital[11][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)


    if option == mlfb_analog[0][0]:
        draw_text(mlfb_analog[0][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[0][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[0][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[0][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[0][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[0][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[0][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[0][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[0][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[0][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[1][0]:
        draw_text(mlfb_analog[1][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[1][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[1][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[1][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[1][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[1][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[1][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[1][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[1][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[1][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[2][0]:
        draw_text(mlfb_analog[2][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[2][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[2][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[2][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[2][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[2][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[2][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[2][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[2][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[2][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[3][0]:
        draw_text(mlfb_analog[3][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[3][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[3][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[3][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[3][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[3][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[3][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[3][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[3][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[3][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[4][0]:
        draw_text(mlfb_analog[4][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[4][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[4][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[4][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[4][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[4][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[4][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[4][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[4][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[4][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[5][0]:
        draw_text(mlfb_analog[5][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[5][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[5][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[5][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[5][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[5][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[5][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[5][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[5][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[5][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[6][0]:
        draw_text(mlfb_analog[6][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[6][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[6][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[6][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[6][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[6][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[6][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[6][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[6][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[6][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[7][0]:
        draw_text(mlfb_analog[7][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[7][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[7][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[7][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[7][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[7][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[7][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[7][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[7][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[7][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[8][0]:
        draw_text(mlfb_analog[8][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[8][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[8][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[8][8], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[8][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[8][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[8][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[8][9], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[8][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[8][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[9][0]:
        draw_text(mlfb_analog[9][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[9][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[9][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[9][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[9][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[9][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[9][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[9][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[9][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[9][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[10][0]:
        draw_text(mlfb_analog[10][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[10][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[10][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[10][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[10][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[10][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[10][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[10][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[10][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[10][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[11][0]:
        draw_text(mlfb_analog[11][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[11][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[11][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[11][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[11][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[11][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[11][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[11][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[11][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[11][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    if option == mlfb_analog[12][0]:
        draw_text(mlfb_analog[12][3], sys_font30, (text_r,text_g,text_b), screen, 490 , 230)
        draw_text(mlfb_analog[12][4], sys_font30, (text_r,text_g,text_b), screen, 690 , 230)
        draw_text(mlfb_analog[12][4], sys_font30, (text_r,text_g,text_b), screen, 890 , 230)
        draw_text(mlfb_analog[12][3], sys_font30, (text_r,text_g,text_b), screen, 1080 , 230)
        draw_text(mlfb_analog[12][5], sys_font30, (text_r,text_g,text_b), screen, 490 , 330)
        draw_text(mlfb_analog[12][6], sys_font30, (text_r,text_g,text_b), screen, 690 , 330)
        draw_text(mlfb_analog[12][6], sys_font30, (text_r,text_g,text_b), screen, 890 , 330)
        draw_text(mlfb_analog[12][5], sys_font30, (text_r,text_g,text_b), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 550)
        draw_text(mlfb_analog[12][1], sys_font30, (text_r,text_g,text_b), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 600)
        draw_text(mlfb_analog[12][2], sys_font30, (text_r,text_g,text_b), screen, 460 , 600)
    #endregion
def material():
    pygame.draw.rect(screen, (168, 165, 165), (0,0,300, h))
    button(materials[0][0], 0, 60, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[1][0], 0, 90, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[2][0], 0, 120, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[3][0], 0, 150, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,180,300, 30))
    button(materials[4][0], 0, 210, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[5][0], 0, 240, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[6][0], 0, 270, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,300,300, 30))
    button(materials[7][0], 0, 330, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[8][0], 0, 360, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[9][0], 0, 390, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[10][0], 0, 420, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,450,300, 30))
    button(materials[11][0], 0, 480, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[12][0], 0, 510, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
    button(materials[13][0], 0, 540, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)

    if option == materials[0][0]:
        draw_text(materials[0][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[0][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[0][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[0][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[0][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (text_r,text_g,text_b), screen, 600 , 400)
        screen.blit(front_dblue_img, (550, 450))
    if option == materials[1][0]:
        draw_text(materials[1][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[1][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[1][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[1][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[1][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (text_r,text_g,text_b), screen, 600 , 400)
        screen.blit(front_hblue_img, (550, 450))
    if option == materials[2][0]:
        draw_text(materials[2][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[2][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[2][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[2][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[2][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (text_r,text_g,text_b), screen, 600 , 400)
        screen.blit(front_black_img, (550, 450))
    if option == materials[3][0]:
        draw_text(materials[3][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[3][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[3][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[3][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[3][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (text_r,text_g,text_b), screen, 600 , 400)
        screen.blit(front_white_img, (550, 450))
    if option == materials[4][0]:
        draw_text(materials[4][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[4][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[4][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[4][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[4][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (text_r,text_g,text_b), screen, 600 , 400)
        screen.blit(geh_15_img, (550, 450))
    if option == materials[5][0]:
        draw_text(materials[5][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[5][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[5][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[5][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[5][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (text_r,text_g,text_b), screen, 600 , 400)
        screen.blit(cod_a_img, (550, 450))
    if option == materials[6][0]:
        draw_text(materials[6][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[6][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[6][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[6][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[6][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (text_r,text_g,text_b), screen, 600 , 400)
        screen.blit(cod_b_img, (550, 450))
    if option == materials[7][0]:
        draw_text(materials[7][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[7][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[7][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[7][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[7][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (text_r,text_g,text_b), screen, 600 , 400)
        screen.blit(schach_10_f_img, (550, 450))
    if option == materials[8][0]:
        draw_text(materials[8][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[8][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[8][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[8][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[8][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (text_r,text_g,text_b), screen, 600 , 400)
        screen.blit(schach_15_img, (550, 450))
    if option == materials[9][0]:
        draw_text(materials[9][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[9][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[9][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[9][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[9][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
    if option == materials[10][0]:
        draw_text(materials[10][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[10][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[10][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[10][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[10][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
    if option == materials[11][0]:
        draw_text(materials[11][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[11][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[11][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[11][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[11][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
    if option == materials[12][0]:
        draw_text(materials[12][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[12][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[12][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[12][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[12][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
    if option == materials[13][0]:
        draw_text(materials[13][0], sys_font30, (text_r,text_g,text_b), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 150)
        draw_text(materials[13][1], sys_font30, (text_r,text_g,text_b), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 200)
        draw_text(materials[13][2], sys_font30, (text_r,text_g,text_b), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 250)
        draw_text(materials[13][3], sys_font30, (text_r,text_g,text_b), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (text_r,text_g,text_b), screen, 310 , 300)
        draw_text(materials[13][4], sys_font30, (text_r,text_g,text_b), screen, 550 , 300)
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


try:
    file = open(save_dir,'r')
    save = file.read()
    save_list = save.split(",")
    print("Try")
except:
    print("File erstellt")
    file = open(save_dir,'a+')
    file.write(f"{background_r},{background_g},{background_b},{buttoncolor_r},{buttoncolor_g},{buttoncolor_b},{topbar_r},{topbar_g},{topbar_b},{text_r},{text_g},{text_b}")
    print("except")
    file = open(save_dir,'r')
    save = file.read()
    save_list = save.split(",")
    print(file.read())


background_r = int(save_list[0])
background_g = int(save_list[1])
background_b = int(save_list[2])

buttoncolor_r = int(save_list[3])
buttoncolor_g = int(save_list[4])
buttoncolor_b = int(save_list[5])
#155, 150, 100

topbar_r = int(save_list[6])
topbar_g = int(save_list[7])
topbar_b = int(save_list[8])

text_r = int(save_list[9])
text_g = int(save_list[10])
text_b = int(save_list[11])




while runtime:

    screen.fill((int(background_r), int(background_g), int(background_b)))

    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    pressed = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False
        elif event.type == pygame.MOUSEBUTTONDOWN and sites == "Suchen":
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
            # Change the current color of the input box.
            color = color_active if active else color_inactive
        elif event.type == pygame.KEYDOWN and sites == "Suchen":
            if active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, color, input_box, 2)


    if pressed[pygame.K_SPACE]:
        runtime = False
    if sites == "Exit":
        runtime = False

    if sites == "Baugruppen":
        baugruppen()
    elif sites == "Material":
        material()
    elif sites == "Suchen":

        button("Suche", 0, 100, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
        button("Neue Suche", 0, 130, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
        button("Im System suchen", 400, 200, 235, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
        button("Leiterplatte", 900, 100, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
        button("Baugruppe", 900, 130, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
        if scan_switch == "Leiterplatte":
            pygame.draw.ellipse(screen, (255,0,0), [880,110,15,15])
        if scan_switch == "Baugruppe":
            pygame.draw.ellipse(screen, (255,0,0), [880,140,15,15])
        draw_text("Die A5E Nummer lautet: ", sys_font30, (text_r,text_g,text_b), screen, 400 , 165)
        draw_text(a5e_erg, sys_font30, (text_r,text_g,text_b), screen, 700 , 165)


        if set_error == True:
            a5e_erg = "Error Webscraper / Ungültiger Barcode"
            #draw_text("Error Webscraper / Ungültiger Barcode", sys_font30, (text_r,text_g,text_b), screen, 700 , 165)


        #region -> Webscraper

        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        if option == "Neue Suche":
            text = ""
            option = " "
            set_error = False
            material_index = 0
            a5e_erg = ""
            suche_string = ""

        if option == "Suche" and suche_em:

            try:
                suche_string = text
                print("Werteübergabe erfolgreich")

                url_requested = request.urlopen(f'https://simaticit.amb2.siemens.de/snr/Default.aspx?SN={suche_string}')
                if 200 == url_requested.code:
                    html_content = str(url_requested.read())


                if scan_switch == "Leiterplatte":
                    material_index = html_content.index("Materialnummer der gescannten Seriennummer")

                    html_index_min = material_index
                    html_index_max = material_index + 250

                    html_index = html_content.index('A5E', html_index_min, html_index_max)

                    a5e_erg = html_content[html_index]+html_content[html_index+1]+html_content[html_index+2]+html_content[html_index+3]+html_content[html_index+4]+html_content[html_index+5]+html_content[html_index+6]+html_content[html_index+7]+html_content[html_index+8]+html_content[html_index+9]+html_content[html_index+10]
                    print(f"Leiterplatten setting -> {a5e_erg}")

                elif scan_switch == "Baugruppe":
                    material_index = html_content.index("HeaderTableBlueWhiteHyperlink")

                    html_index_min = material_index
                    html_index_max = material_index + 250

                    html_index = html_content.index('A5E', html_index_min, html_index_max)

                    a5e_erg = html_content[html_index]+html_content[html_index+1]+html_content[html_index+2]+html_content[html_index+3]+html_content[html_index+4]+html_content[html_index+5]+html_content[html_index+6]+html_content[html_index+7]+html_content[html_index+8]+html_content[html_index+9]+html_content[html_index+10]
                    print(f"Baugruppen setting -> {a5e_erg}")


                set_error = False


            except:
                set_error = True


        #endregion


        if suche_string == text:
            suche_em = False
        else:
            suche_em = True

        if option == "Im System suchen":

            if a5e_erg == mlfb_digital[0][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[0][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[1][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[1][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[2][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[2][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[3][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[3][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[4][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[4][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[5][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[5][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[6][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[6][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[7][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[7][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[8][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[8][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[9][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[9][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[10][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[10][0]
            else:
                set_error = True
            if a5e_erg == mlfb_digital[11][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_digital[11][0]
            else:
                set_error = True




            if a5e_erg == mlfb_analog[0][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[0][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[1][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[1][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[2][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[2][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[3][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[3][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[4][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[4][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[5][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[5][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[6][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[6][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[7][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[7][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[8][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[8][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[9][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[9][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[10][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[10][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[11][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[11][0]
            else:
                set_error = True
            if a5e_erg == mlfb_analog[12][2]:
                erg_gefunden = True
                sites = "Baugruppen"
                option = mlfb_analog[12][0]
            else:
                set_error = True
    elif sites == "Settings":
        screen.fill((background_r, background_g, background_b))
        button("Backgroundcolor", 0, 100, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
        button("Buttoncolor", 0, 130, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
        button("Topbarcolor", 0, 160, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)
        button("Textcolor", 0, 190, 300, 30, (buttoncolor_r,buttoncolor_g,buttoncolor_b), (0,100,255), sys_font22)

        if option == "Backgroundcolor":
            button_setting("+", 400, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Red[r]", sys_font30, (text_r,text_g,text_b), screen, 480 , 100)
            draw_text(f"{background_r}", sys_font30, (text_r,text_g,text_b), screen, 650 , 100)
            button_setting("set 0", 770, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("Save", 400, 250, 100, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("Set to Default", 550, 250, 130, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Green[g]", sys_font30, (text_r,text_g,text_b), screen, 480 , 150)
            draw_text(f"{background_g}", sys_font30, (text_r,text_g,text_b), screen, 650 , 150)
            button_setting("set 0", 770, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 200, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Blue[b]", sys_font30, (text_r,text_g,text_b), screen, 480 , 200)
            draw_text(f"{background_b}", sys_font30, (text_r,text_g,text_b), screen, 650 , 200)
            button_setting("set 0", 770, 200, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 200, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 200, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            if pressed[pygame.K_r]:
                if background_r >= 255:
                    background_r = 0
                else:
                    background_r +=1
            if pressed[pygame.K_g]:
                if background_g >= 255:
                    background_g = 0
                else:
                    background_g +=1
            if pressed[pygame.K_b]:
                if background_b >= 255:
                    background_b = 0
                else:
                    background_b +=1
        elif option == "Buttoncolor":
            button_setting("+", 400, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Red[r]", sys_font30, (text_r,text_g,text_b), screen, 480 , 100)
            draw_text(f"{buttoncolor_r}", sys_font30, (text_r,text_g,text_b), screen, 650 , 100)
            button_setting("set 0", 770, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("Save", 400, 250, 100, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("Set to Default", 550, 250, 130, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Green[g]", sys_font30, (text_r,text_g,text_b), screen, 480 , 150)
            draw_text(f"{buttoncolor_g}", sys_font30, (text_r,text_g,text_b), screen, 650 , 150)
            button_setting("set 0", 770, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 200, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Blue[b]", sys_font30, (text_r,text_g,text_b), screen, 480 , 200)
            draw_text(f"{buttoncolor_b}", sys_font30, (text_r,text_g,text_b), screen, 650 , 200)
            button_setting("set 0", 770, 200, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 200, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 200, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            if pressed[pygame.K_r]:
                if buttoncolor_r >= 255:
                    buttoncolor_r = 0
                else:
                    buttoncolor_r +=1
            if pressed[pygame.K_g]:
                if buttoncolor_g >= 255:
                    buttoncolor_g = 0
                else:
                    buttoncolor_g +=1
            if pressed[pygame.K_b]:
                if buttoncolor_b >= 255:
                    buttoncolor_b = 0
                else:
                    buttoncolor_b +=1
        elif option == "Topbarcolor":
            button_setting("+", 400, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Red[r]", sys_font30, (text_r,text_g,text_b), screen, 480 , 100)
            draw_text(f"{topbar_r}", sys_font30, (text_r,text_g,text_b), screen, 650 , 100)
            button_setting("set 0", 770, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("Save", 400, 250, 100, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("Set to Default", 550, 250, 130, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Green[g]", sys_font30, (text_r,text_g,text_b), screen, 480 , 150)
            draw_text(f"{topbar_g}", sys_font30, (text_r,text_g,text_b), screen, 650 , 150)
            button_setting("set 0", 770, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 200, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Blue[b]", sys_font30, (text_r,text_g,text_b), screen, 480 , 200)
            draw_text(f"{topbar_b}", sys_font30, (text_r,text_g,text_b), screen, 650 , 200)
            button_setting("set 0", 770, 200, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 200, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 200, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            if pressed[pygame.K_r]:
                if topbar_r >= 255:
                    topbar_r = 0
                else:
                    topbar_r +=1
            if pressed[pygame.K_g]:
                if topbar_g >= 255:
                    topbar_g = 0
                else:
                    topbar_g +=1
            if pressed[pygame.K_b]:
                if topbar_b >= 255:
                    topbar_b = 0
                else:
                    topbar_b +=1
        elif option == "Textcolor":
            button_setting("+", 400, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Red[r]", sys_font30, (0,0,0), screen, 480 , 100)
            draw_text(f"{text_r}", sys_font30, (0,0,0), screen, 650 , 100)
            button_setting("set 0", 770, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("Save", 400, 250, 100, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("Set to Default", 550, 250, 130, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Green[g]", sys_font30, (0,0,0), screen, 480 , 150)
            draw_text(f"{text_g}", sys_font30, (0,0,0), screen, 650 , 150)
            button_setting("set 0", 770, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 200, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Blue[b]", sys_font30, (0,0,0), screen, 480 , 200)
            draw_text(f"{text_b}", sys_font30, (0,0,0), screen, 650 , 200)
            button_setting("set 0", 770, 200, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 200, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 200, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            if pressed[pygame.K_r]:
                if text_r >= 255:
                    text_r = 0
                else:
                    text_r +=1
            if pressed[pygame.K_g]:
                if text_g >= 255:
                    text_g = 0
                else:
                    text_g +=1
            if pressed[pygame.K_b]:
                if text_b >= 255:
                    text_b = 0
                else:
                    text_b +=1





    topbar()
    file.close()









    pygame.display.flip()
    clock.tick(fps)

