import pygame
import sys

pixel_font30 = pygame.font.Font("fonts/PixeloidSans.ttf", 30)
pixel_font15 = pygame.font.Font("fonts/PixeloidSans.ttf", 15)
maus_pos = pygame.mouse.get_pos()
maus_klick = pygame.mouse.get_pressed()
screen_w = 1920
screen_h = 1080
screen = pygame.display.set_mode([screen_w, screen_h])

#region -> Def
def textObjekt(text, pixel_font):
    textFlaeche = pixel_font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()
def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, font):
    global maus_aktiv
    global option
    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if but_txt == "Start":
                option = "Start"
            elif but_txt == "Einstellungen":
                option = "Einstellungen"
            elif but_txt == "Credits":
                option = "Credits"
            elif but_txt == "Home":
                option = "Home"
            elif but_txt == "Exit":
                sys.exit()
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)
#endregion

def main_menu():
    button("Play", 1700, 1020, 200, 50, "Red", "Green", pixel_font15)