if option == mlfb_digital[i][0]:
    if mlfb_digital[i][7]:
        pygame.draw.rect(screen, (5, 255, 0), (670,465,50, 50))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (670,465,50, 50))
if mlfb_digital[i][0] == option:
    draw_text("Wärme: ", sys_font30, (0, 0, 0), screen, 560 , 480)
    pygame.draw.rect(screen, (192, 192, 192), (560,100,85, 85))
    draw_text(mlfb_digital[i][3], sys_font30, (0, 0, 0), screen, 560+33, 100+35)
    pygame.draw.rect(screen, (192, 192, 192), (660,100,85, 85))
    draw_text(mlfb_digital[i][4], sys_font30, (0, 0, 0), screen, 660+33, 100+35)
    pygame.draw.rect(screen, (192, 192, 192), (760,100,85, 85))
    draw_text(mlfb_digital[i][5], sys_font30, (0, 0, 0), screen, 760+33, 100+35)
    pygame.draw.rect(screen, (192, 192, 192), (860,100,85, 85))
    draw_text(mlfb_digital[i][6], sys_font30, (0, 0, 0), screen, 860+33, 100+35)

    pygame.draw.rect(screen, (192, 192, 192), (560,300,85, 85))
    draw_text(mlfb_digital[i][8], sys_font30, (0, 0, 0), screen, 560+33, 300+35)
    pygame.draw.rect(screen, (192, 192, 192), (660,300,85, 85))
    draw_text(mlfb_digital[i][9], sys_font30, (0, 0, 0), screen, 660+33, 300+35)
    pygame.draw.rect(screen, (192, 192, 192), (760,300,85, 85))
    draw_text(mlfb_digital[i][10], sys_font30, (0, 0, 0), screen, 760+33, 300+35)
    pygame.draw.rect(screen, (192, 192, 192), (860,300,85, 85))
    draw_text(mlfb_digital[i][11], sys_font30, (0, 0, 0), screen, 860+33, 300+35)