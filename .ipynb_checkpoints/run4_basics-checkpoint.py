# run4 GUED utilities, updated 11/17/2022
# Fuhao Ji @ AD

from epics import caget, caput
from time import sleep
import time
from PVnamelist import pvnamelist
import numpy as np

## pv names for basic operations, need update
pv_motor_x_rel = 'ASTA:SMAR02:M1:MOTOR' # sampel stage motor rel X
pv_motor_x = 'ASTA:PI02:M3:MOTOR' # sampel stage motor X
pv_motor_y = 'ASTA:PI02:M2:MOTOR' # sampel stage motor Y
pv_motor_z = 'ASTA:PI02:M1:MOTOR' # sampel stage motor Z

pv_gun_uv_throttle = 'MOTR:AS01:MC03:CH1:MOTOR'  # gun UV throttle
pv_NDwheel = 'MOTR:AS01:MC04:CH2:MOTOR' # pump laser ND wheel

pv_phosphor = 'ASTA:BO:2114-9:BIT2' # phosphor screen In/Out


def phosphorIn():
    caput(pv_phosphor, 1)
    return

def YAGIn():
    set_stage_pos(file_path = 'pos_YAG.txt')
    return

def BiIn():
    set_stage_pos(file_path = 'pos_Bi.txt')
    return

def FCIn():   
    set_stage_pos(file_path = 'pos_FC.txt')
    return

def SJIn():   
    set_stage_pos(file_path = 'pos_SJ.txt')
    return

def SiIn():    
    set_stage_pos(file_path = 'pos_Si.txt')
    return

def StageOut():
    caput(pv_motor_x_rel, 5)   ## sample stage motor rel X
    caput(pv_motor_x, 9)    ## sample stage motor X
    return

def pumpLaserOff():
    print("pump laser shutter close")
    caput("ASTA:LSC03:OC:CLOSE", 1) # Pump laser shutter close
    sleep(1)
    return
    
def pumpLaserOn():
    print("pump laser shutter open")
    caput("ASTA:LSC03:OC:OPEN", 1) # Pump laser shutter open
    sleep(1)
    return

def pumpLaserLowest():
    print("pump energy go to lowest")
    caput(pv_NDwheel, -150) # pump laser ND wheel, lowest power at -150
    return

def gunUVOff():
    print("gun UV shutter close")
    caput("ASTA:LSC01:OC:CLOSE", 1) # gun UV shutter close
    sleep(1)
    return
    
def gunUVOn():
    print("gun UV shutter open")
    caput("ASTA:LSC01:OC:OPEN", 1) # gun UV shutter open
    sleep(1)
    return
    
def chamberLightOff():
    print("turning chamber light off")
    caput("ACSW:AS01:NW03:2POWEROFF", 1)
    sleep(1)
    return
    
def chamberLightOn():
    print("turning chamber light on")
    caput("ACSW:AS01:NW03:2POWERON", 1)
    return
    
def highCharge():
    print("setting high charge mode ...")
    caput(pv_gun_uv_throttle, 28.4)
    return
    
def lowCharge():
    print("setting low charge mode ...")
    caput(pv_gun_uv_throttle, 48.4)
    return


def save_stage_pos(file_path = 'pos.txt'):
    # obtain stage positions
    motor_x_rel = caget(pv_motor_x_rel)
    motor_x = caget(pv_motor_x)
    motor_y = caget(pv_motor_y)
    motor_z = caget(pv_motor_z)

    pos = np.array([motor_x_rel, motor_x, motor_y, motor_z])
    
    try:
        np.savetxt(file_path, pos, delimiter=',', fmt='%f')
        print(f"Array saved to {file_path} successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
        
def load_stage_pos(file_path = 'pos.txt'):
    try:
        array = np.loadtxt(file_path, delimiter=',')
        print(array)
        return array
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
def set_stage_pos(file_path = 'pos.txt'):
    # load stage positions from txt file
    array = load_stage_pos(file_path)
    caput(pv_motor_x_rel, array[0])   ## sample stage motor rel X
    caput(pv_motor_x, array[1])    ## sample stage motor X
    caput(pv_motor_y, array[2])   ## sample stage motor Y
    caput(pv_motor_z, array[3])    ## sample stage motor Z
    return
    
def save_sample_settings(file_path = 'settings.txt'):
    # obtain stage positions
    motor_x_rel = caget(pv_motor_x_rel)
    motor_x = caget(pv_motor_x)
    motor_y = caget(pv_motor_y)
    motor_z = caget(pv_motor_z)
    
    # obtain pump laser NDwheel 
    NDwheel = caget(pv_NDwheel)
    
    settings = np.array([motor_x_rel, motor_x, motor_y, motor_z, NDwheel])
    
    try:
        np.savetxt(file_path, settings, delimiter=',', fmt='%f')
        print(f"Array saved to {file_path} successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
def load_settings(file_path = 'settings.txt'):
    try:
        array = np.loadtxt(file_path, delimiter=',')
        print(array)
        return array
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
    
def set_sample_settings(file_path = 'settings.txt'):
    # load sample settings from txt file
    array = load_settings(file_path)
    caput(pv_motor_x_rel, array[0])   ## sample stage motor rel X
    caput(pv_motor_x, array[1])    ## sample stage motor X
    caput(pv_motor_y, array[2])   ## sample stage motor Y
    caput(pv_motor_z, array[3])    ## sample stage motor Z
    caput(pv_NDwheel, array[4])   ## pump laser ND wheel position
    return
    
    