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
                ["134-6HB00-0CA1", "69484", "A5E37970403", "39", "3C-PNV29754", "39", "3", 1],
                ["134-6HB00-0DA1", "77532", "A5E50585786", "39", " ", "39", "37", 0],
                ["134-6HD01-0BA1", "73655", "A5E46004505", "37", " ", "37", "37", 0],
                ["134-6JD00-0CA1", "71259", "A5E38837676", "33", "1", "41", "1", 1, "49", "45"],

                ["135-6GB00-0BA1", "77129", "A5E35652111", " ", " ", "37", " ", 1],
                ["135-6HB00-0CA1", "69482", "A5E32562703", "37", "4", "37", "37", 1],
                ["135-6HB00-0DA1", "69481", "A5E35652111", "37", "4", "37", "37", 1],
                ["135-6HD00-0BA1", "69249", "A5E31290169", "37", "4", "37", "37", 0]]

material = [["Frontdeckel Dunkelblau", "65325", "A5E36039007", "3196 St.", "2970 St."],
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

print(f"MLFB = {mlfb_analog[0][0]} AUB = {mlfb_analog[0][1]}  A5E = {mlfb_analog[0][2]}  Pemos SP1{mlfb_analog[0][3]}, {mlfb_analog[0][4]} Pemo SP2 {mlfb_analog[0][5]}, {mlfb_analog[0][6]}  Vorwärme ? = {mlfb_analog[0][7]}")


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


if option == "Backgroundcolor":
    button("+", 400, 100, 30, 30, (155,150,100), (0,100,255), sys_font22)
    draw_text("Red[r]", sys_font30, (0,0,0), screen, 480 , 100)
    draw_text(f"{text_r}", sys_font30, (0,0,0), screen, 650 , 100)
    button("set 0", 770, 100, 60, 30, (155,150,100), (0,100,255), sys_font22)
    draw_text("Green[g]", sys_font30, (0,0,0), screen, 480 , 150)
    draw_text(f"{text_g}", sys_font30, (0,0,0), screen, 650 , 150)
    button("set 0", 770, 150, 60, 30, (155,150,100), (0,100,255), sys_font22)
    draw_text("Blue[b]", sys_font30, (0,0,0), screen, 480 , 200)
    draw_text(f"{text_g}", sys_font30, (0,0,0), screen, 650 , 200)
    button("set 0", 770, 200, 60, 30, (155,150,100), (0,100,255), sys_font22)
    button("-", 900, 100, 30, 30, (155,150,100), (0,100,255), sys_font22)




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
    if text_g < 255:
        text_g += 1
    else:
        text_g = 0
elif but_txt == "-" and but_y == 200:
    option_setting = "-"
    if text_g > 0:
        text_g -= 1
    else:
        text_g = 255

if but_txt == "set 0" and but_y == 100:
    text_r = 0
elif but_txt == "set 255" and but_y == 100:
    text_r = 255
if but_txt == "set 0" and but_y == 150:
    text_g = 0
elif but_txt == "set 255" and but_y == 150:
    text_g = 255
if but_txt == "set 0" and but_y == 200:
    text_g = 0
elif but_txt == "set 255" and but_y == 200:
    text_g = 255



    if option == "Buttoncolor":
        button_setting("+", 400, 100, 30, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)
        draw_text("Red[r]", sys_font30, (0,0,0), screen, 480 , 100)
        draw_text(f"{text_r}", sys_font30, (0,0,0), screen, 650 , 100)
        button_setting("set 0", 770, 100, 60, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)
        button_setting("set 255", 870, 100, 60, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)
        button_setting("-", 1000, 100, 30, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)

        button_setting("+", 400, 150, 30, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)
        draw_text("Green[g]", sys_font30, (0,0,0), screen, 480 , 150)
        draw_text(f"{text_g}", sys_font30, (0,0,0), screen, 650 , 150)
        button_setting("set 0", 770, 150, 60, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)
        button_setting("set 255", 870, 150, 60, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)
        button_setting("-", 1000, 150, 30, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)

        button_setting("+", 400, 200, 30, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)
        draw_text("Blue[b]", sys_font30, (0,0,0), screen, 480 , 200)
        draw_text(f"{text_g}", sys_font30, (0,0,0), screen, 650 , 200)
        button_setting("set 0", 770, 200, 60, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)
        button_setting("set 255", 870, 200, 60, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)
        button_setting("-", 1000, 200, 30, 30, (text_r,text_g,text_g), (0,100,255), sys_font22)

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
            if text_g >= 255:
                text_g = 0
            else:
                text_g +=1









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
                    if text_g < 255:
                        text_g += 1
                    else:
                        text_g = 0
                elif but_txt == "-" and but_y == 200:
                    option_setting = "-"
                    if text_g > 0:
                        text_g -= 1
                    else:
                        text_g = 255

                if but_txt == "set 0" and but_y == 100:
                    text_r = 0
                elif but_txt == "set 255" and but_y == 100:
                    text_r = 255
                if but_txt == "set 0" and but_y == 150:
                    text_g = 0
                elif but_txt == "set 255" and but_y == 150:
                    text_g = 255
                if but_txt == "set 0" and but_y == 200:
                    text_g = 0
                elif but_txt == "set 255" and but_y == 200:
                    text_g = 255






            button_setting("+", 400, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Red[r]", sys_font30, (0,0,0), screen, 480 , 100)
            draw_text(f"{text_r}", sys_font30, (0,0,0), screen, 650 , 100)
            button_setting("set 0", 770, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 100, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 100, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Green[g]", sys_font30, (0,0,0), screen, 480 , 150)
            draw_text(f"{text_g}", sys_font30, (0,0,0), screen, 650 , 150)
            button_setting("set 0", 770, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("set 255", 870, 150, 60, 30, (155, 150, 100), (0,100,255), sys_font22)
            button_setting("-", 1000, 150, 30, 30, (155, 150, 100), (0,100,255), sys_font22)

            button_setting("+", 400, 200, 30, 30, (155, 150, 100), (0,100,255), sys_font22)
            draw_text("Blue[b]", sys_font30, (0,0,0), screen, 480 , 200)
            draw_text(f"{text_g}", sys_font30, (0,0,0), screen, 650 , 200)
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
                if text_g >= 255:
                    text_g = 0
                else:
                    text_g +=1








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