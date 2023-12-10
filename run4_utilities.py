# run4 GUED utilities, updated 11/17/2022
# Fuhao Ji @ AD

from epics import caget, caput
from time import sleep
import time
from PVnamelist import pvnamelist
from run4_basics import *
import numpy as np
import sys

def setBi():
    pumpLaserOff()
    sleep(1)

    print("setting Bi...")
    set_sample_settings(file_path = 'settings_Bi.txt')
    return

def setSi():
    pumpLaserOff()
    sleep(1)
    
    print("setting Si...")
    set_sample_settings(file_path = 'settings_Si.txt')
    return

def setFC():
    pumpLaserOff()
    sleep(1)
    
    print("setting Flow Cell...")
    set_sample_settings(file_path = 'settings_FC.txt')
    return

def setSJ():
    pumpLaserOff()
    sleep(1)
    
    print("setting Slit Jet...")
    set_sample_settings(file_path = 'settings_SJ.txt')
    return

def goToFC():
    pumpLaserOff()
    sleep(1)
    # pumpLaserLowest()
    print("move Flow Cell in...")
    FCIn()
    return

def goToSJ():
    pumpLaserOff()
    sleep(1)
    # pumpLaserLowest()
    print("move Slit Jet in...")
    SJIn()
    return

def goToBi():
    pumpLaserOff()
    sleep(1)
    pumpLaserLowest()
    print("move Bi in...")
    # sample stage motor
    BiIn()
    return

def goToYAG():
    pumpLaserOff()
    sleep(1)
    # pumpLaserLowest()
    print("move YAG in...")
    # sample stage motor
    YAGIn()
    return

def goToSi():
    pumpLaserOff()
    sleep(1)
    # pumpLaserLowest()
    print("move Si in...")
    # sample stage motor
    SiIn()
    return

def goToAndor1():
    # sample stage motor
    ## got to Andor1 function
    ## equivalent to (1) move THz structure fully out (2) move 2nd chamber YAG fully out
    StageOut()
    # phosphorIn()
    return
    

def waitForInput_test():
    pumpLaserOff()
    goToYAG()
    chamberLightOff()
    sleep(2)
    chamberLightOn()
    sleep(2)
    
    # wait operator to check status
    print("Please check status")
    print("Press Enter to continue...")
    sys.stdin.readline()
    return
    
def spatialOverlap():
    pumpLaserOff()
    sleep(1)
    
    pumpLaserLowest()
    
    goToYAG()
    sleep(1)
    chamberLightOff()
    sleep(2)
    
    print("setting camera gain and exp")
    caput('ASPS04:cam1:Gain', 30)
    caput('ASPS04:cam1:AcquireTime', 2.0)
    
    gunUVOn()
    print("Please check e-beam location, move marker to ebeam")
    
    print("Press Enter to continue...")
    sys.stdin.readline()
    
    print("setting camera gain and exp")
    caput('ASPS04:cam1:Gain', 10)
    caput('ASPS04:cam1:AcquireTime', 0.1)   
    sleep(3)
    
    pumpLaserOn()
    print("Please check pump laser location, move laser to marker")
    print("Press Enter to continue...")
    sys.stdin.readline()
    
    pumpLaserOff()
    sleep(1)
    
    print("setting camera gain and exp")
    caput('ASPS04:cam1:Gain', 0)
    caput('ASPS04:cam1:AcquireTime', 0.1)   
    sleep(3)
    
    chamberLightOn()
    return
    
def checkEbeam():
    pumpLaserOff()
    sleep(1)
    
    goToYAG()
    sleep(1)
    chamberLightOff()
    sleep(2)
    
    print("setting camera gain and exp")
    caput('ASPS04:cam1:Gain', 30)
    caput('ASPS04:cam1:AcquireTime', 2.0)
    
    gunUVOn()
    print("Please check e-beam location, move marker to ebeam")
    
    print("Press Enter to continue...")
    sys.stdin.readline()
    
    print("setting camera gain and exp")
    caput('ASPS04:cam1:Gain', 0)
    caput('ASPS04:cam1:AcquireTime', 0.1)   
    sleep(3)
    
    chamberLightOn()
    return
    
def checkAndorEbeam():
    pumpLaserOff()
    sleep(1)
    print("move stage out...")
    StageOut()
    sleep(2)
    
    print("far detector phosphor in")
    caput('ASTA:BO:2114-9:BIT2', 1) # insert the fardetector phosphor
    
    print("Please set Andor detector gain = 10, exp = 0.1")
    print("Press Enter to continue...")
    sys.stdin.readline()
    
    gunUVOn()
    
    print("Please check e-beam on Andor detector")
    print("Press Enter to continue...")
    sys.stdin.readline()
    # sleep(5)
    
    print("Please Insert collimator to 93 mm")
    print("Press Enter to continue...")
    sys.stdin.readline()
    sleep(5)
    
    print("Please tune steering zero and collimator to optimize beam")
    print("Press Enter to continue...")
    sys.stdin.readline()
    return
    
    
def checkPumpLaser():
    pumpLaserOff()
    sleep(1)
    
    pumpLaserLowest()
    
    goToYAG()
    sleep(1)
    chamberLightOff()
    sleep(2)
    
    print("setting camera gain and exp")
    caput('ASPS04:cam1:Gain', 10)
    caput('ASPS04:cam1:AcquireTime', 0.1)   
    sleep(3)
    
    pumpLaserOn()
    print("Please check pump laser location, move laser to marker")
    print("Press Enter to continue...")
    sys.stdin.readline()
    
    pumpLaserOff()
    sleep(1)
    
    print("setting camera gain and exp")
    caput('ASPS04:cam1:Gain', 0)
    caput('ASPS04:cam1:AcquireTime', 0.1)   
    sleep(3)
    
    chamberLightOn()
    return
    