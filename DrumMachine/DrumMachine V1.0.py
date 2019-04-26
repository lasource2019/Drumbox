#coding:utf-8
import pygame
from pygame.locals import *
import time
import numpy as np
import sounddevice as sd


#Création de la fenêtre graphique

res = (800, 540)
pygame.init()
pygame.display.set_caption("Drumbox")
pygame.mixer.init(14100, -16, 2, 2048)

#Mise en place du fond

fenetre_drumbox = pygame.display.set_mode(res)
drumbox_image = pygame.image.load("DrumMachine.png")
fenetre_drumbox.blit(drumbox_image, [0, 0])
pygame.display.flip()

pygame.key.set_repeat(400, 30)

clavier_image = pygame.image.load("clavier.png")
fenetre_drumbox.blit(clavier_image, [0, 70])
pygame.display.flip()

#Initialisation des sons

clap = pygame.mixer.Sound("Clap.wav")
kick = pygame.mixer.Sound("Kick.wav")
crash = pygame.mixer.Sound("crash.wav")
snare = pygame.mixer.Sound("Snare.wav")

#Intitialisation des images

ImgClap = pygame.image.load("DrumMachine-Hat.png")
ImgKick = pygame.image.load("DrumMachine-Kick.png")
ImgCrash = pygame.image.load("DrumMachine-Crash.png")
ImgSnare = pygame.image.load("DrumMachine-Snare.png")
ImgDrumbox = pygame.image.load("DrumMachine.png")

ImDo = pygame.image.load("ClavierDO.png")
ImRe = pygame.image.load("ClavierRE.png")
ImMi = pygame.image.load("ClavierMI.png")
ImFa = pygame.image.load("ClavierFA.png")
ImSol = pygame.image.load("ClavierSOL.png")
ImLa = pygame.image.load("ClavierLA.png")
ImSi = pygame.image.load("ClavierSI.png")

def Main():
    keydown()
    keyup()
    SonClavierPressé()
    


def SonClavierPressé():    
    
    if event.type == KEYDOWN:

        if event.key == K_f:
            clavier_image = ImDo
            ChangementClavier(clavier_image)
            frequency = 262
            NoteClavier(frequency)

        if event.type == KEYDOWN and event.key == K_g:
            clavier_image = ImRe
            ChangementClavier(clavier_image)
            frequency = 293
            NoteClavier(frequency)
           
        if event.type == KEYDOWN and event.key == K_h:
            clavier_image = ImMi
            ChangementClavier(clavier_image)
            frequency = 329
            NoteClavier(frequency)
            
        if event.type == KEYDOWN and event.key == K_j:
            clavier_image = ImFa
            ChangementClavier(clavier_image)
            frequency = 349
            NoteClavier(frequency)
            
        if event.type == KEYDOWN and event.key == K_k:            
            clavier_image = ImSol
            ChangementClavier(clavier_image)
            frequency = 392
            NoteClavier(frequency)
            
        if event.type == KEYDOWN and event.key == K_l:
            clavier_image = ImLa
            ChangementClavier(clavier_image)
            frequency = 440
            NoteClavier(frequency)
            
def ChangementClavier(clavier_image):
    fenetre_drumbox.blit(clavier_image, [0, 70])
    pygame.display.flip()
    
def ChangementFond(drumbox_image):
    fenetre_drumbox.blit(drumbox_image, [0, 0])
    pygame.display.flip()

def RetourFond():
    drumbox_image = pygame.image.load("DrumMachine.png")
    fenetre_drumbox.blit(drumbox_image, [0, 0])
    pygame.display.flip()


def NoteClavier(frequency):
    sd.default.samplerate = 44100
    # on définit le temps
    time = 1.0
    samples = np.arange(44100 * time) / 44100.0
    # on convertit en onde sinusoïdale de fréquence f de formule w(t) = A*sin(2*pi*f*t)
    onde = 10000 * np.sin(2 * np.pi * frequency * samples)
    # on converit en format onde (16 bits)
    ond_onde = np.array(onde, dtype=np.int16)
    sd.play(ond_onde, blocking=True)


def keydown():        #Fonction qui affecte des touches aux sons et au changement de fond quand la touche est pressée

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

def keyup():          #Fonction qui change le fond et arrête le son quand la touche est relachée
      
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
        if event.type == pygame.QUIT:   #Fermeture de la fenêtre lorsque l'on appuie sur la croix rouge
            launched = False
            
        Main()

pygame.quit()
