import pygame
import sys

pygame.init()
w, h = 1200, 900
screen = pygame.display.set_mode((w, h))
runtime_login = True
clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((w, h))
FONT = pygame.font.Font(None, 32)

runtime_login = True
runtime = False

maus_pos = pygame.mouse.get_pos()
maus_klick = pygame.mouse.get_pressed()


font = pygame.font.Font(None, 32)
input_box = pygame.Rect(470, 200, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False
suche_em = False
suche_string = " "
a5e_erg = ""

login_but = False

pixel_font60 = pygame.font.Font("fonts/PixeloidSans.ttf", 60)
pixel_font30 = pygame.font.Font("fonts/PixeloidSans.ttf", 30)
pixel_font22 = pygame.font.Font("fonts/PixeloidSans.ttf", 22)
pixel_font15 = pygame.font.Font("fonts/PixeloidSans.ttf", 15)
sys_font15 = pygame.font.SysFont(None, 15)
sys_font22 = pygame.font.SysFont(None, 22)
sys_font30 = pygame.font.SysFont(None, 30)
sys_font60 = pygame.font.SysFont(None, 60)

login_kennung = ""






def draw_text(text, sys_font15, color, screen, x , y):
    textobj = sys_font15.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

def textObjekt(text, pixel_font15):
    textFlaeche = pixel_font15.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option
    global sites
    global scan_switch
    global login_but

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
            elif but_txt == "Anmelden":
                login_but = True


        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
        login_but = False
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)


while runtime_login:
    runtime = False
    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    pressed = pygame.key.get_pressed()


    if pressed[pygame.K_SPACE]:
        runtime_login = False


    screen.fill((0, 0, 50))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime_login = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
            # Change the current color of the input box.
            color = color_active if active else color_inactive
        elif event.type == pygame.KEYDOWN:
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

    draw_text("User Kennung", sys_font22, (255, 255, 255), screen, 515, 150)
    draw_text("Login", sys_font60, (255, 255, 255), screen, 510, 50)
    button("Anmelden", 470, 250, 200, 40, "Green", (19, 141, 158), sys_font30)

    if login_but:
        login_kennung = text
        runtime = True
        runtime_login = False


    print(login_kennung)
    pygame.display.flip()
    clock.tick(fps)




while runtime:
    runtime_login = False
    print("Test runtime")

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False

    if pressed[pygame.K_SPACE]:
        runtime = False


    screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(fps)
