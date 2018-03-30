# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

###soundmaschine

import random
from random import choice

Tonfolge = []

def createLsystem(runs, startton):                #Lsystem durchlaufanzahl und startaxiom
    startString = startton                        
    endString = ""
    for R in range(runs):                         #durchlaeufe definieren
        endString = processString(startString)
        startString = endString
    
    return endString

def processString(oldString):                      #prozessstring defenieren, 
    newstr = ""
    for T in oldString:                            #neuer string ist der vorheriger string mit angewandten regeln 
        newstr = newstr + applyRules(T)
    Tonfolge.append(oldString)                               #ausgeben des alten Strings bzw des Tons bevor er wieder ersetzt wird
    return newstr

def applyRules(T):                                 # bestimmen der Regeln, zufaellige Zahl wird gewuerfelt, um die Wahrscheinlichkeiten fuer die darauffolgenden Toene festzulegen
    newstr = ""
    if T == 'C':
        X = random.randint(1, 100)/100              #hoehere wahrscheinlichkeit fuer die anliegenden Toene
        if X < 0.3:
            newstr = 'H'
        elif X < 0.6:
            newstr = 'D'
        elif X < 0.7:
            newstr = 'E'
        elif X < 0.8:
            newstr = 'F'
        elif X < 0.9:
            newstr = 'G'
        elif X < 1.0:
            newstr = 'A'
            
    elif T == 'D':
        X = random.randint(1, 100)/100
        if X < 0.3:
            newstr = 'C'
        elif X < 0.6:
            newstr = 'E'
        elif X < 0.7:
            newstr = 'F'
        elif X < 0.8:
            newstr = 'G'
        elif X < 0.9:
            newstr = 'A'
        elif X < 1.0:
            newstr = 'H'
    
    elif T == 'E':
        X = random.randint(1, 100)/100
        if X < 0.3:
            newstr = 'D'
        elif X < 0.6:
            newstr = 'F'
        elif X < 0.7:
            newstr = 'G'
        elif X < 0.8:
            newstr = 'A'
        elif X < 0.9:
            newstr = 'H'
        elif X < 1.0:
            newstr = 'C'
            
    elif T == 'F':
        X = random.randint(1, 100)/100
        if X < 0.3:
            newstr = 'E'
        elif X < 0.6:
            newstr = 'G'
        elif X < 0.7:
            newstr = 'A'
        elif X < 0.8:
            newstr = 'H'
        elif X < 0.9:
            newstr = 'C'
        elif X < 1.0:
            newstr = 'D'
            
    elif T == 'G':
        X = random.randint(1, 100)/100
        if X < 0.3:
            newstr = 'F'
        elif X < 0.6:
            newstr = 'A'
        elif X < 0.7:
            newstr = 'H'
        elif X < 0.8:
            newstr = 'C'
        elif X < 0.9:
            newstr = 'D'
        elif X < 1.0:
            newstr = 'E'
            
    elif T == 'A':
        X = random.randint(1, 100)/100
        if X < 0.3:
            newstr = 'G'
        elif X < 0.6:
            newstr = 'H'
        elif X < 0.7:
            newstr = 'C'
        elif X < 0.8:
            newstr = 'D'
        elif X < 0.9:
            newstr = 'E'
        elif X < 1.0:
            newstr = 'F'
            
    elif T == 'H':
        X = random.randint(1, 100)/100
        if X < 0.3:
            newstr = 'A'
        elif X < 0.6:
            newstr = 'C'
        elif X < 0.7:
            newstr = 'D'
        elif X < 0.8:
            newstr = 'E'
        elif X < 0.9:
            newstr = 'F'
        elif X < 1.0:
            newstr = 'G'
            
    
    else:
        newstr = T                             #absicherung
        
    return newstr                              #wiederholen des Vorgangs, der schleife

def Lied():                                    # Funktion Lied definieren, damit L System druchgefuehrt werden kann
    Melodie = createLsystem(24, choice ("CDEFGAH") )     #per zufall startaxiom auswaehlen, zahl der durchlauefe bestimmen 
    print(Melodie)                                       

Lied ()    

print(Tonfolge)

import pygame

def abspielen (t, Tonfolge) :
    if Tonfolge [t] == 'C' :
        pygame.mixer.init()
        pygame.mixer.music.load('/Users/morics/Desktop/ModSimProjekt/c-durRobo.wav')        #Dateipfad mit Toenen
        pygame.mixer.music.play() 
        
    elif Tonfolge [t] == 'D' :
        pygame.mixer.init()
        pygame.mixer.music.load('/Users/morics/Desktop/ModSimProjekt/d-durRobo.wav')        #Dateipfad mit Toenen
        pygame.mixer.music.play()
        
    elif Tonfolge [t] == 'E' :       
        pygame.mixer.init()
        pygame.mixer.music.load('/Users/morics/Desktop/ModSimProjekt/e-durRobo.wav')        #Dateipfad mit Toenen
        pygame.mixer.music.play()
        
    elif Tonfolge [t] == 'F' :
        pygame.mixer.init()
        pygame.mixer.music.load('/Users/morics/Desktop/ModSimProjekt/f-durRobo.wav')        #Dateipfad mit Toenen
        pygame.mixer.music.play()
        
    elif Tonfolge [t] == 'G' :
        pygame.mixer.init()
        pygame.mixer.music.load('/Users/morics/Desktop/ModSimProjekt/g-durRobo.wav')        #Dateipfad mit Toenen
        pygame.mixer.music.play()
        
    elif Tonfolge [t] == 'A' :
        pygame.mixer.init()
        pygame.mixer.music.load('/Users/morics/Desktop/ModSimProjekt/a-durRobo.wav')        #Dateipfad mit Toenen
        pygame.mixer.music.play()
        
    elif Tonfolge [t] == 'H' :
        pygame.mixer.init()
        pygame.mixer.music.load('/Users/morics/Desktop/ModSimProjekt/h-durRobo.wav')        #Dateipfad mit Toenen
        pygame.mixer.music.play()
        
    
    else :
        print("EndeGelaende") 
        
