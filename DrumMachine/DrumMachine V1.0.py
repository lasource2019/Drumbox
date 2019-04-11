#coding:utf-8
import pygame
from pygame.locals import *
import time
import numpy as np
import sounddevice as sd

#Création de la fenêtre graphique

res = (800, 450)
pygame.init()
pygame.display.set_caption("Drumbox")
pygame.mixer.init(44100, -16, 2, 2048)

#Mise en place du fond

fenetre_drumbox = pygame.display.set_mode(res)
drumbox_image = pygame.image.load("Images/LaDrumbox.png")
fenetre_drumbox.blit(drumbox_image, [0, 0])
pygame.display.flip()                

pygame.key.set_repeat(400, 30)



#Initialisation des sons


clap = pygame.mixer.Sound("Sons/Clap.wav")
kick = pygame.mixer.Sound("Sons/Kick.wav")
crash = pygame.mixer.Sound("Sons/crash.wav")
snare = pygame.mixer.Sound("Sons/Snare.wav")


#Intitialisation des images

ImgClap = pygame.image.load("Images/Drumbox-Clap.gif")
ImgKick = pygame.image.load("Images/Drumbox-Kick.png")
ImgCrash = pygame.image.load("Images/Drumbox-Crash.png")
ImgSnare = pygame.image.load("Images/Drumbox-Snare.png")
ImgDrumbox = pygame.image.load("Images/LaDrumbox.png")



def Main():
    keydown()
    keyup()
    
    
    
    if event.type == KEYDOWN and event.key == K_f:
            sd.default.samplerate = 44100
# définir le temps            
            time = 1.0
            frequency = 262
            samples = np.arange(44100 * time) / 44100.0
# convertir en onde sinusoïdale de fréquence f de formule w(t) = A*sin(2*pi*f*t)
            onde = 10000 * np.sin(2 * np.pi * frequency * samples)
# Converir en format onde (16 bits)
            ond_onde = np.array(onde, dtype=np.int16)

            sd.play(ond_onde, blocking=True)
            
    if event.type == KEYDOWN and event.key == K_g:
            sd.default.samplerate = 44100
            time = 1.0
            frequency = 293
            samples = np.arange(44100 * time) / 44100.0
            onde = 10000 * np.sin(2 * np.pi * frequency * samples)
            ond_onde = np.array(onde, dtype=np.int16)
            sd.play(ond_onde, blocking=True)
            
    if event.type == KEYDOWN and event.key == K_h:
            sd.default.samplerate = 44100
         
            time = 1.0
            frequency = 329
            samples = np.arange(44100 * time) / 44100.0
            onde = 10000 * np.sin(2 * np.pi * frequency * samples)
            ond_onde = np.array(onde, dtype=np.int16)
            sd.play(ond_onde, blocking=True)

    if event.type == KEYDOWN and event.key == K_j:
            sd.default.samplerate = 44100
            time = 1.0
            frequency = 349
            samples = np.arange(44100 * time) / 44100.0
            onde = 10000 * np.sin(2 * np.pi * frequency * samples)
            ond_onde = np.array(onde, dtype=np.int16)
            sd.play(ond_onde, blocking=True)
            
    if event.type == KEYDOWN and event.key == K_k:            
            sd.default.samplerate = 44100
            time = 1.0
            frequency = 392
            samples = np.arange(44100 * time) / 44100.0
            onde = 10000 * np.sin(2 * np.pi * frequency * samples)
            ond_onde = np.array(onde, dtype=np.int16)
            sd.play(ond_onde, blocking=True)
            
    if event.type == KEYDOWN and event.key == K_l:                
            sd.default.samplerate = 44100
            time = 1.0
            frequency = 440
            samples = np.arange(44100 * time) / 44100.0
            onde = 10000 * np.sin(2 * np.pi * frequency * samples)
            ond_onde = np.array(onde, dtype=np.int16)
            sd.play(ond_onde, blocking=True)
            
            
            
            


def ChangementFond(drumbox_image):
    fenetre_drumbox.blit(drumbox_image, [0, 0])
    pygame.display.flip()


def RetourFond():
    drumbox_image = pygame.image.load("Images/LaDrumbox.png")
    fenetre_drumbox.blit(drumbox_image, [0, 0])
    pygame.display.flip()


#Fonction qui affecte des touches aux sons et au changement de fond quand la touche est pressée
def keydown():
    
    
    if event.type == KEYDOWN:
        
        
        if event.key == K_q:
            kick.play()
            drumbox_image = ImgKick
            ChangementFond(drumbox_image)
        if event.key == K_w:
            snare.play()
            drumbox_image = ImgSnare
            ChangementFond(drumbox_image)
        if event.key == K_a:
            crash.play
            drumbox_image = ImgCrash
            ChangementFond(drumbox_image)
        if event.key == K_s:
            clap.play()
            drumbox_image = ImgClap
            ChangementFond(drumbox_image)


#Fonction qui change le fond et arrête le son quand la touche est relachée
def keyup():
    
    
    if event.type == KEYUP:
        
        
        if event.key == K_q:
            kick.stop()
            RetourFond()
        if event.key == K_w:
            snare.stop()
            RetourFond()
        if event.key == K_a:
            crash.stop()
            RetourFond()
            pygame.display.flip()
        if event.key == K_s:
            clap.stop()
            RetourFond()

















launched = True
while launched:
    for event in pygame.event.get():
        
        
#Fermeture de la fenêtre lorsque l'on appuie sur la croix rouge
        
        if event.type == pygame.QUIT:
            launched = False
            
        Main()

pygame.quit()
