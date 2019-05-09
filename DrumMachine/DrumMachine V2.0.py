import pygame
from pygame.locals import *
import time

res = (800, 250)
pygame.init()
pygame.display.set_caption("FlStudio 1.5")

screen = pygame.display.set_mode(res)

#Initialisation des images

kick_sequenceur = pygame.image.load("Images/Seq-Kick.png").convert_alpha()
snare_sequenceur = pygame.image.load("Images/Seq-Snare.png").convert_alpha()
clap_sequenceur = pygame.image.load("Images/Seq-Clap.png").convert_alpha()
hats_sequenceur = pygame.image.load("Images/Seq-Hats.png").convert_alpha()
silence_sequenceur = pygame.image.load("Images/Seq-Silence.png").convert_alpha()
img_fond = pygame.image.load("Images/img_fondPapier.png").convert_alpha()
boite = pygame.image.load("Images/img_fond.png").convert_alpha()


#Correspond à l'évènement de sélection d'image. Quand selected = 0, l'image n'est pas sélectionnée, quand selected = 1, l'image est sélectionnée
selected_kick = 0      
selected_snare = 0
selected_clap = 0
selected_hats = 0
selected_silence = 0

#Positions des boutons des instruments
posx = [150, 250, 350, 450, 550] 
posy = [35, 35, 35, 35, 35]


kick_position = screen.blit(kick_sequenceur,(posx[0],posy[0]))
snare_position = screen.blit(snare_sequenceur, (posx[1], posy[1]))
clap_position = screen.blit(clap_sequenceur, (posx[2], posy[2]))
hats_position = screen.blit(hats_sequenceur, (posx[3], posy[3]))
silence_position = screen.blit(silence_sequenceur, (posx[4], posy[4]))

#Position des boutons des instruments lorsque la souris est relâchée
poscasex_kick = posx[0] - 35
poscasey_kick = posy[0] - 25
poscasex_snare = posx[1] - 35
poscasey_snare = posy[1] - 25
poscasex_clap = posx[2] - 35
poscasey_clap = posy[2] - 25
poscasex_hats = posx[3] - 35
poscasey_hats = posy[3] - 25
poscasex_silence = posx[4] - 35
poscasey_silence = posy[4] - 25

#Initialisation des sons du séquenceur
son = 0
kickson = 1
snareson = 2
clapson = 3
hatsson = 4
silenceson = 5
sequenceur = [0] * 14
kicksound = pygame.mixer.Sound("Sons/Kick.wav")
snaresound = pygame.mixer.Sound("Sons/Snare.wav")
clapsound = pygame.mixer.Sound("Sons/Clap.wav")
hatssound =pygame.mixer.Sound("Sons/crash.wav")

#Listes des coordonnées des cases du séquenceur
sequenceur_x = [125, 205, 285, 365, 445, 525, 605] 
sequenceur_y = [80, 140]

Boucle = True #Boucle infinie


def BoutonRelacher(position_x,position_y, instrument):
    screen.blit(img_fond, (0,0))
    screen.blit(boite,(100, 70))
    screen.blit(instrument,(position_x-35,position_y-25))
    pygame.display.flip()
    return

#Fonction qui définit "l'aimentation" sur les cases du séquenceur
def Detection_Sequenceur(instrument_son, instrument, posx, posy):
    
    if posx >= sequenceur_x[0] and posx <= sequenceur_x[0] + 70 and posy >= sequenceur_y[0] and posy < sequenceur_y[0] + 50:
        Magnet(instrument, sequenceur_x[0], sequenceur_y[0])
        sequenceur[0] = instrument_son
    if posx >= sequenceur_x[1] and posx <= sequenceur_x[1] + 70 and posy >= sequenceur_y[0] and posy < sequenceur_y[0] + 50:
        Magnet(instrument, sequenceur_x[1], sequenceur_y[0])
        sequenceur[1] = instrument_son              
    if posx >= sequenceur_x[2] and posx <= sequenceur_x[2] + 70 and posy >= sequenceur_y[0] and posy < sequenceur_y[0] + 50:
        Magnet(instrument, sequenceur_x[2], sequenceur_y[0])
        sequenceur[2] = instrument_son              
    if posx >= sequenceur_x[3] and posx <= sequenceur_x[3] + 70 and posy >= sequenceur_y[0] and posy < sequenceur_y[0] + 50:
        Magnet(instrument, sequenceur_x[3], sequenceur_y[0])
        sequenceur[3] = instrument_son
    if posx >= sequenceur_x[4] and posx <= sequenceur_x[4] + 70 and posy >= sequenceur_y[0] and posy < sequenceur_y[0] + 50:
        Magnet(instrument, sequenceur_x[4], sequenceur_y[0])
        sequenceur[4] = instrument_son           
    if posx >= sequenceur_x[5] and posx <= sequenceur_x[5] + 70 and posy >= sequenceur_y[0] and posy < sequenceur_y[0] + 50:
        Magnet(instrument, sequenceur_x[5], sequenceur_y[0])
        sequenceur[5] = instrument_son
    if posx >= sequenceur_x[6] and posx <= sequenceur_x[6] + 70 and posy >= sequenceur_y[0] and posy < sequenceur_y[0] + 50:
        Magnet(instrument, sequenceur_x[6], sequenceur_y[0])
        sequenceur[6] = instrument_son

    if posx >= sequenceur_x[0] and posx <= sequenceur_x[0] + 70 and posy >= sequenceur_y[1] and posy < sequenceur_y[1] + 50:
        Magnet(instrument, sequenceur_x[0], sequenceur_y[1])
        sequenceur[7] = instrument_son
    if posx >= sequenceur_x[1] and posx <= sequenceur_x[1] + 70 and posy >= sequenceur_y[1] and posy < sequenceur_y[1] + 50:
        Magnet(instrument, sequenceur_x[1], sequenceur_y[1])
        sequenceur[8] = instrument_son                
    if posx >= sequenceur_x[2] and posx <= sequenceur_x[2] + 70 and posy >= sequenceur_y[1] and posy < sequenceur_y[1] + 50:
        Magnet(instrument, sequenceur_x[2], sequenceur_y[1])
        sequenceur[9] = instrument_son               
    if posx >= sequenceur_x[3] and posx <= sequenceur_x[3] + 70 and posy >= sequenceur_y[1] and posy < sequenceur_y[1] + 50:
        Magnet(instrument, sequenceur_x[3], sequenceur_y[1])
        sequenceur[10] = instrument_son
    if posx >= sequenceur_x[4] and posx <= sequenceur_x[4] + 70 and posy >= sequenceur_y[1] and posy < sequenceur_y[1] + 50:
        Magnet(instrument, sequenceur_x[4], sequenceur_y[1])
        sequenceur[11] = instrument_son           
    if posx >= sequenceur_x[5] and posx <= sequenceur_x[5] + 70 and posy >= sequenceur_y[1] and posy < sequenceur_y[1] + 50:
        Magnet(instrument, sequenceur_x[5], sequenceur_y[1])
        sequenceur[12] = instrument_son
    if posx >= sequenceur_x[6] and posx <= sequenceur_x[6] + 70 and posy >= sequenceur_y[1] and posy < sequenceur_y[1] + 50:
        Magnet(instrument, sequenceur_x[6], sequenceur_y[1])
        sequenceur[13] = instrument_son

def Son(instrument):
    son = instrument

def Magnet(instrument, case_x, case_y):
    screen.blit(img_fond, (0,0))
    screen.blit(boite,(100, 70))
    screen.blit(instrument,(case_x, case_y))
    pygame.display.flip()

def SourisMouvement(instrument, instrument_position):
    r = screen.blit(screen, instrument_position, instrument_position)
    instrument_position.move_ip(event.rel) #a chaque fois il y a mouvement de souris, le personnage prend la nouvelle position du curseur
    pygame.display.update((r,screen.blit(instrument, instrument_position)))

while Boucle:
    for event in pygame.event.get():
        if event.type == QUIT:
            Boucle = False
        screen.blit(img_fond, (0,0))  
        screen.blit(boite,(100, 70))
        screen.blit(kick_sequenceur, (poscasex_kick, poscasey_kick))
        screen.blit(snare_sequenceur, (poscasex_snare, poscasey_snare))
        screen.blit(clap_sequenceur, (poscasex_clap, poscasey_clap))
        screen.blit(hats_sequenceur, (poscasex_hats, poscasey_hats))
        screen.blit(silence_sequenceur, (poscasex_silence, poscasey_silence))
        pygame.display.flip()

# boucle déplacement d'image pour le KICK
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and kick_position.collidepoint(event.pos):
            selected_kick = 1
            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and selected_kick == 1:
            posx[0],posy[0] = pygame.mouse.get_pos()
            BoutonRelacher(posx[0],posy[0], kick_sequenceur)
            selected_kick = 0
            Detection_Sequenceur(kickson, kick_sequenceur, posx[0], posy[0])

        elif event.type == MOUSEMOTION and selected_kick == 1:
            SourisMouvement(kick_sequenceur, kick_position)

            
# boucle déplacement d'image pour le SNARE
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and snare_position.collidepoint(event.pos):
            selected_snare = 1
            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and selected_snare == 1:
            posx[1],posy[1] = pygame.mouse.get_pos()
            BoutonRelacher(posx[1],posy[1], snare_sequenceur)
            selected_snare = 0
            Detection_Sequenceur(snareson, snare_sequenceur, posx[1], posy[1])
                
        elif event.type == MOUSEMOTION and selected_snare == 1:
            SourisMouvement(snare_sequenceur, snare_position)
            
# boucle déplacement d'image pour le CLAP
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and clap_position.collidepoint(event.pos):
            selected_clap = 1
            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and selected_clap == 1:
            posx[2],posy[2] = pygame.mouse.get_pos()
            BoutonRelacher(posx[2],posy[2], clap_sequenceur)
            selected_clap = 0
            Detection_Sequenceur(clapson, clap_sequenceur, posx[2], posy[2])
                
        elif event.type == MOUSEMOTION and selected_clap == 1:
            SourisMouvement(clap_sequenceur, clap_position)
            
# boucle déplacement d'image pour les HATS
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and hats_position.collidepoint(event.pos):
            selected_hats = 1
            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and selected_hats == 1:
            posx[3],posy[3] = pygame.mouse.get_pos()
            BoutonRelacher(posx[3],posy[3], hats_sequenceur)
            selected_hats = 0
            Detection_Sequenceur(hatsson, hats_sequenceur, posx[3], posy[3])
                
        elif event.type == MOUSEMOTION and selected_hats == 1:
            SourisMouvement(hats_sequenceur, hats_position)
            
# boucle déplacement d'image pour le SILENCE
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and silence_position.collidepoint(event.pos):
            selected_silence = 1
            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and selected_silence == 1:
            posx[4],posy[4] = pygame.mouse.get_pos()
            BoutonRelacher(posx[4],posy[4], silence_sequenceur)
            selected_silence = 0
            Detection_Sequenceur(silenceson, silence_sequenceur, posx[4], posy[4])
                
        elif event.type == MOUSEMOTION and selected_silence == 1:
            SourisMouvement(silence_sequenceur, silence_position)

        poscasex_kick = posx[0] - 35
        poscasey_kick = posy[0] - 25
        poscasex_snare = posx[1] - 35
        poscasey_snare = posy[1] - 25
        poscasex_clap = posx[2] - 35
        poscasey_clap = posy[2] - 25
        poscasex_hats = posx[3] - 35
        poscasey_hats = posy[3] - 25
        poscasex_silence = posx[4] - 35
        poscasey_silence = posy[4] - 25
        
#joue le son quand on appuie sur P
        if event.type == KEYDOWN and event.key == K_p:
            for loop in range(14):
                if sequenceur[loop] == 1:
                    kicksound.play()
                    time.sleep(0.3)
                if sequenceur[loop] == 2:
                    snaresound.play()
                    time.sleep(0.3)
                if sequenceur[loop] == 3:
                    clapsound.play()
                    time.sleep(0.3)
                if sequenceur[loop] == 4:
                    hatssound.play()
                    time.sleep(0.3)
                if sequenceur[loop] == 5:
                    time.sleep(0.5)

#Test du programme
for loop in range(14):
    print(sequenceur[loop], end = "")
print()

pygame.quit()
