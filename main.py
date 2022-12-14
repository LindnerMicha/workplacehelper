import pygame
import sys
from urllib import request

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

class Checkbox:
    def __init__(self, surface, x, y, idnum, color=(230, 230, 230),
                 caption="", outline_color=(0, 0, 0), check_color=(0, 0, 0),
                 font_size=22, font_color=(0, 0, 0),
                 text_offset=(28, 1), font='Ariel Black'):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.caption = caption
        self.oc = outline_color
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        self.ft = font

        #identification for removal and reorginazation
        self.idnum = idnum

        # checkbox object
        self.checkbox_obj = pygame.Rect(self.x, self.y, 12, 12)
        self.checkbox_outline = self.checkbox_obj.copy()

        # variables to test the different states of the checkbox
        self.checked = False

    def _draw_button_text(self):
        self.font = pygame.font.SysFont(self.ft, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x + self.to[0], self.y + 12 / 2 - h / 2 +
                         self.to[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_checkbox(self):
        if self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
            pygame.draw.circle(self.surface, self.cc, (self.x + 6, self.y + 6), 4)

        elif not self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = pygame.mouse.get_pos()
        px, py, w, h = self.checkbox_obj
        if px < x < px + w and py < y < py + w:
            if self.checked:
                self.checked = False
            else:
                self.checked = True

    def update_checkbox(self, event_object):
        if event_object.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            self._update(event_object)
#region -> Button
def textObjekt(text, pixel_font15):
    textFlaeche = pixel_font15.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option
    global sites

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
    pygame.draw.rect(screen, (168, 165, 165), (0,0,w, 60))
    button("Baugruppen", 10, 8, 150, 45, (155,150,100), (0,100,255), sys_font30)
    button("Material", 200, 8, 150, 45, (155,150,100), (0,100,255), sys_font30)
    button("Suchen", 400, 8, 150, 45, (155, 150,100), (0, 100, 255), sys_font30)
    button("Exit", 1030, 8, 150, 45, (186, 48, 48), (133, 1, 1), sys_font30)

def baugruppen():
    #region -> Buttons
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
        draw_text(mlfb_digital[0][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[0][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[0][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[0][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[0][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[0][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[0][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[0][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[0][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[0][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[1][0]:
        draw_text(mlfb_digital[1][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[1][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[1][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[1][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[1][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[1][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[1][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[1][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[1][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[1][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[2][0]:
        draw_text(mlfb_digital[2][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[2][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[2][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[2][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[2][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[2][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[2][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[2][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[2][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[2][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[3][0]:
        draw_text(mlfb_digital[3][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[3][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[3][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[3][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[3][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[3][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[3][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[3][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[3][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[3][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[4][0]:
        draw_text(mlfb_digital[4][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[4][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[4][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[4][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[4][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[4][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[4][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[4][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[4][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[4][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[5][0]:
        draw_text(mlfb_digital[5][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[5][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[5][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[5][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[5][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[5][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[5][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[5][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[5][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[5][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[6][0]:
        draw_text(mlfb_digital[6][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[6][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[6][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[6][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[6][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[6][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[6][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[6][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[6][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[6][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[7][0]:
        draw_text(mlfb_digital[7][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[7][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[7][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[7][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[7][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[7][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[7][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[7][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[7][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[7][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[8][0]:
        draw_text(mlfb_digital[8][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[8][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[8][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[8][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[8][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[8][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[8][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[8][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[8][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[8][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[9][0]:
        draw_text(mlfb_digital[9][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[9][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[9][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[9][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[9][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[9][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[9][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[9][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[9][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[9][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[10][0]:
        draw_text(mlfb_digital[10][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[10][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[10][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[10][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[10][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[10][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[10][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[10][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[10][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[10][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_digital[11][0]:
        draw_text(mlfb_digital[11][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_digital[11][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_digital[11][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_digital[11][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_digital[11][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_digital[11][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_digital[11][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_digital[11][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_digital[11][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_digital[11][2], sys_font30, (0,0,0), screen, 460 , 600)


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
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[0][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[1][0]:
        draw_text(mlfb_analog[1][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[1][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[1][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[1][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[1][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[1][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[1][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[1][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[1][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[1][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[2][0]:
        draw_text(mlfb_analog[2][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[2][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[2][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[2][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[2][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[2][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[2][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[2][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[2][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[2][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[3][0]:
        draw_text(mlfb_analog[3][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[3][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[3][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[3][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[3][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[3][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[3][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[3][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[3][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[3][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[4][0]:
        draw_text(mlfb_analog[4][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[4][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[4][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[4][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[4][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[4][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[4][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[4][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[4][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[4][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[5][0]:
        draw_text(mlfb_analog[5][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[5][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[5][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[5][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[5][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[5][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[5][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[5][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[5][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[5][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[6][0]:
        draw_text(mlfb_analog[6][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[6][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[6][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[6][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[6][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[6][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[6][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[6][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[6][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[6][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[7][0]:
        draw_text(mlfb_analog[7][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[7][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[7][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[7][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[7][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[7][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[7][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[7][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[7][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[7][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[8][0]:
        draw_text(mlfb_analog[8][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[8][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[8][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[8][8], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[8][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[8][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[8][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[8][9], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[8][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[8][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[9][0]:
        draw_text(mlfb_analog[9][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[9][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[9][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[9][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[9][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[9][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[9][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[9][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[9][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[9][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[10][0]:
        draw_text(mlfb_analog[10][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[10][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[10][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[10][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[10][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[10][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[10][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[10][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[10][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[10][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[11][0]:
        draw_text(mlfb_analog[11][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[11][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[11][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[11][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[11][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[11][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[11][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[11][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[11][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[11][2], sys_font30, (0,0,0), screen, 460 , 600)
    if option == mlfb_analog[12][0]:
        draw_text(mlfb_analog[12][3], sys_font30, (0,0,0), screen, 490 , 230)
        draw_text(mlfb_analog[12][4], sys_font30, (0,0,0), screen, 690 , 230)
        draw_text(mlfb_analog[12][4], sys_font30, (0,0,0), screen, 890 , 230)
        draw_text(mlfb_analog[12][3], sys_font30, (0,0,0), screen, 1080 , 230)
        draw_text(mlfb_analog[12][5], sys_font30, (0,0,0), screen, 490 , 330)
        draw_text(mlfb_analog[12][6], sys_font30, (0,0,0), screen, 690 , 330)
        draw_text(mlfb_analog[12][6], sys_font30, (0,0,0), screen, 890 , 330)
        draw_text(mlfb_analog[12][5], sys_font30, (0,0,0), screen, 1080 , 330)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 550)
        draw_text(mlfb_analog[12][1], sys_font30, (0,0,0), screen, 460 , 550)
        draw_text("FBG-Nummer: ", sys_font30, (0,0,0), screen, 310 , 600)
        draw_text(mlfb_analog[12][2], sys_font30, (0,0,0), screen, 460 , 600)
    #endregion
def material():
    pygame.draw.rect(screen, (168, 165, 165), (0,0,300, h))
    button(materials[0][0], 0, 60, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[1][0], 0, 90, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[2][0], 0, 120, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[3][0], 0, 150, 300, 30, (155,150,100), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,180,300, 30))
    button(materials[4][0], 0, 210, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[5][0], 0, 240, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[6][0], 0, 270, 300, 30, (155,150,100), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,300,300, 30))
    button(materials[7][0], 0, 330, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[8][0], 0, 360, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[9][0], 0, 390, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[10][0], 0, 420, 300, 30, (155,150,100), (0,100,255), sys_font22)
    pygame.draw.rect(screen, (168, 165, 165), (0,450,300, 30))
    button(materials[11][0], 0, 480, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[12][0], 0, 510, 300, 30, (155,150,100), (0,100,255), sys_font22)
    button(materials[13][0], 0, 540, 300, 30, (155,150,100), (0,100,255), sys_font22)

    if option == materials[0][0]:
        draw_text(materials[0][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[0][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[0][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[0][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[0][4], sys_font30, (0,0,0), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (0,0,0), screen, 600 , 400)
        screen.blit(front_dblue_img, (550, 450))
    if option == materials[1][0]:
        draw_text(materials[1][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[1][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[1][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[1][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[1][4], sys_font30, (0,0,0), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (0,0,0), screen, 600 , 400)
        screen.blit(front_hblue_img, (550, 450))
    if option == materials[2][0]:
        draw_text(materials[2][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[2][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[2][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[2][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[2][4], sys_font30, (0,0,0), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (0,0,0), screen, 600 , 400)
        screen.blit(front_black_img, (550, 450))
    if option == materials[3][0]:
        draw_text(materials[3][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[3][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[3][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[3][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[3][4], sys_font30, (0,0,0), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (0,0,0), screen, 600 , 400)
        screen.blit(front_white_img, (550, 450))
    if option == materials[4][0]:
        draw_text(materials[4][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[4][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[4][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[4][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[4][4], sys_font30, (0,0,0), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (0,0,0), screen, 600 , 400)
        screen.blit(geh_15_img, (550, 450))
    if option == materials[5][0]:
        draw_text(materials[5][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[5][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[5][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[5][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[5][4], sys_font30, (0,0,0), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (0,0,0), screen, 600 , 400)
        screen.blit(cod_a_img, (550, 450))
    if option == materials[6][0]:
        draw_text(materials[6][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[6][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[6][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[6][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[6][4], sys_font30, (0,0,0), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (0,0,0), screen, 600 , 400)
        screen.blit(cod_b_img, (550, 450))
    if option == materials[7][0]:
        draw_text(materials[7][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[7][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[7][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[7][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[7][4], sys_font30, (0,0,0), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (0,0,0), screen, 600 , 400)
        screen.blit(schach_10_f_img, (550, 450))
    if option == materials[8][0]:
        draw_text(materials[8][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[8][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[8][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[8][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[8][4], sys_font30, (0,0,0), screen, 550 , 300)
        draw_text("Bestellcode für Scanner", sys_font30, (0,0,0), screen, 600 , 400)
        screen.blit(schach_15_img, (550, 450))
    if option == materials[9][0]:
        draw_text(materials[9][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[9][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[9][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[9][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[9][4], sys_font30, (0,0,0), screen, 550 , 300)
    if option == materials[10][0]:
        draw_text(materials[10][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[10][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[10][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[10][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[10][4], sys_font30, (0,0,0), screen, 550 , 300)
    if option == materials[11][0]:
        draw_text(materials[11][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[11][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[11][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[11][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[11][4], sys_font30, (0,0,0), screen, 550 , 300)
    if option == materials[12][0]:
        draw_text(materials[12][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[12][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[12][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[12][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[12][4], sys_font30, (0,0,0), screen, 550 , 300)
    if option == materials[13][0]:
        draw_text(materials[13][0], sys_font30, (100,0,0), screen, 310 , 100)
        draw_text("AUB-Nummer: ", sys_font30, (0,0,0), screen, 310 , 150)
        draw_text(materials[13][1], sys_font30, (0,0,0), screen, 550 , 150)
        draw_text("Teilenummer: ", sys_font30, (0,0,0), screen, 310 , 200)
        draw_text(materials[13][2], sys_font30, (0,0,0), screen, 550 , 200)
        draw_text("Verpackungseinheit: ", sys_font30, (0,0,0), screen, 310 , 250)
        draw_text(materials[13][3], sys_font30, (0,0,0), screen, 550 , 250)
        draw_text("Tiefbestand: ", sys_font30, (0,0,0), screen, 310 , 300)
        draw_text(materials[13][4], sys_font30, (0,0,0), screen, 550 , 300)


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


while runtime:

    screen.fill((255, 255, 255))

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
                #if event.key == pygame.K_RETURN:
                #text = ''
                #elif event.key == pygame.K_BACKSPACE:
                #text = text[:-1]
                #else:
                text += event.unicode

            screen.fill((30, 30, 30))
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
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

        screen.fill((255, 255, 255))

        button("Suche", 0, 100, 300, 30, (155,150,100), (0,100,255), sys_font22)
        button("Neue Suche", 0, 130, 300, 30, (155,150,100), (0,100,255), sys_font22)
        button("Im System Suchen", 0, 160, 300, 30, (155,150,100), (0,100,255), sys_font22)
        draw_text("Die A5E Nummer lautet: ", sys_font30, (0,0,0), screen, 400 , 165)
        draw_text(a5e_erg, sys_font30, (0,0,0), screen, 700 , 165)

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

        if option == "Suche" and suche_em:

            try:
                suche_string = text
                print("Werteübergabe erfolgreich")

                url_requested = request.urlopen(f'https://simaticit.amb2.siemens.de/snr/Default.aspx?SN={suche_string}')
                if 200 == url_requested.code:
                    html_content = str(url_requested.read())

                material_index = html_content.index("Materialnummer der gescannten Seriennummer")

                html_index_min = material_index
                html_index_max = material_index + 250

                html_index = html_content.index('A5E', html_index_min, html_index_max)

                a5e_erg = html_content[html_index]+html_content[html_index+1]+html_content[html_index+2]+html_content[html_index+3]+html_content[html_index+4]+html_content[html_index+5]+html_content[html_index+6]+html_content[html_index+7]+html_content[html_index+8]+html_content[html_index+9]+html_content[html_index+10]

                print(a5e_erg)
            except:
                print("Error Webscraper")
        #endregion

        if suche_string == text:
            suche_em = False
        else:
            suche_em = True






    topbar()



    pygame.display.flip()
    clock.tick(fps)
