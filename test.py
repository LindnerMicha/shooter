import pygame
import sys


pygame.display.set_caption("Top Down CSGO")
pygame.init()
screen_w = 1920
screen_h = 1080
screen = pygame.display.set_mode([screen_w, screen_h])
clock = pygame.time.Clock()
fps = 60

maus_pos = pygame.mouse.get_pos()
maus_klick = pygame.mouse.get_pressed()
pixel_font45 = pygame.font.Font("fonts/PixeloidSans.ttf", 45)
pixel_font30 = pygame.font.Font("fonts/PixeloidSans.ttf", 30)
pixel_font15 = pygame.font.Font("fonts/PixeloidSans.ttf", 15)




background_r = 0
background_g = 0
background_b = 0
buttoncolor_r = 109
buttoncolor_g = 36
buttoncolor_b = 146

option = "Main Menu"

main_menu_buttons = [
    ["Play", 860, 200, 220, 75, buttoncolor_r, buttoncolor_g, buttoncolor_b, 0, 255, 0, pixel_font45],
    ["Level", 860, 350, 220, 75, buttoncolor_r, buttoncolor_g, buttoncolor_b, 0, 255, 0, pixel_font45],
    ["Settings", 860, 500, 220, 75, buttoncolor_r, buttoncolor_g, buttoncolor_b, 0, 255, 0, pixel_font45],
    ["Exit", 860, 650, 220, 75, buttoncolor_r, buttoncolor_g, buttoncolor_b, 0, 255, 0, pixel_font45],
]
level_buttons = [
    ["Menü", 40, 1000, 140, 50, buttoncolor_r, buttoncolor_g, buttoncolor_b, 0, 255, 0, pixel_font30],
]
settings_buttons = [
    ["Menü", 40, 1000, 140, 50, buttoncolor_r, buttoncolor_g, buttoncolor_b, 0, 255, 0, pixel_font30],
]

#region -> Def
def main_menu():
    draw_text("Top Down CSGO", pixel_font45, (255, 255, 255), screen, 775, 50)
    for index in range(len(main_menu_buttons)):
        button(main_menu_buttons[index][0], main_menu_buttons[index][1], main_menu_buttons[index][2], main_menu_buttons[index][3], main_menu_buttons[index][4], (main_menu_buttons[index][5], main_menu_buttons[index][6], main_menu_buttons[index][7]), (main_menu_buttons[index][8], main_menu_buttons[index][9], main_menu_buttons[index][10]), main_menu_buttons[index][11])
def levels():
    draw_text("Levels", pixel_font45, (255, 255, 255), screen, 900, 50)
    for index in range(len(level_buttons)):
        button(level_buttons[index][0], level_buttons[index][1], level_buttons[index][2], level_buttons[index][3], level_buttons[index][4], (level_buttons[index][5], level_buttons[index][6], level_buttons[index][7]), (level_buttons[index][8], level_buttons[index][9], level_buttons[index][10]), level_buttons[index][11])
def settings():
    draw_text("Settings", pixel_font45, (255, 255, 255), screen, 900, 50)
    for index in range(len(level_buttons)):
        button(settings_buttons[index][0], settings_buttons[index][1], settings_buttons[index][2], settings_buttons[index][3], settings_buttons[index][4], (settings_buttons[index][5], settings_buttons[index][6], settings_buttons[index][7]), (settings_buttons[index][8], settings_buttons[index][9], settings_buttons[index][10]), settings_buttons[index][11])
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
    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            option = but_txt
            if but_txt == "Exit":
                sys.exit()
            elif but_txt == "Play":
                option = "Play"
            elif but_txt == "Menü":
                option = "Main Menu"
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)
def setting_button(set_state, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global setting_state
    global maus_aktiv
    global set_decider
    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            if set_state == "+":
                set_decider = "+"
            if set_state == "-":
                set_decider = "-"
        if maus_klick[0] == 0:
            maus_aktiv = False
            set_decider = ""
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))

    textGrund, textkasten = textObjekt(set_state, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)
#endregion





runtime = True

while runtime:

    screen.fill((background_r, background_g, background_b))
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pressed[pygame.K_SPACE]:
            runtime = False

    if option == "Main Menu":
        main_menu()
    elif option == "Level":
        levels()
    elif option == "Settings":
        settings()

    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    clock.tick(fps)
    pygame.display.update()