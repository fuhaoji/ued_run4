## Python automation scripts for MeV-UED run4 operations
## Fuhao Ji @ AD, Nov 20, 2023

## if run on UED-DAQ, do
    source load_env.sh
    python "script.py"

## saveBi.py, saveFC.py, saveSi.py, saveSJ.py, saveYAG.py, saveSettings.py
    save the sample stage positions (x, rel x, y, z) and ND wheel/half wave plate set point to txt files
    file names stand for specific gas sources/samples used in GUED user run
    "FC": Flow Cell
    "SJ": Slit Jet
    "Bi": Bismuth for t-zero 
    "Si": single crystal Silicon for t-zero/q calibration
    "YAG": YAG screen for spatial overlap
    "saveSettings": save settings for arbitrary sample/gas source
    
## setBi.py, setFC.py, setSi.py, setSJ.py, setYAG.py, loadSettings.py
    set sample stage positions and ND wheel/half wave plate set point using numbers saved in txt file
    
## goToBi.py, goToFC.py, goToSi.py, goToSJ.py, goToYAG.py, loadStage.py
    set sample stage positions using numbers saved in txt file
    
## checkEbeam.py
    script for checking E-beam at sample plane
    - close pump shutter
    - go to YAG
    - chamber light off
    - set cam exposure and gain
    - operator identify e-beam locaton and perform necessary tuning
    
## checkPumpLaser.py
    script for checking pump laser at sample plane
    - close pump shutter
    - go to YAG
    - chamber light off
    - set NDwheel to lowest energy
    - set cam exposure and gain
    - operator identify laser locaton and perform necessary tuning
    
## spatialOverlap.py
    script for checking E-beam/pump laser overlap at sample plane
    - close pump shutter
    - go to YAG
    - set cam exposure and gain
    - operator identify e-beam locaton, set marker
    - set cam exposure and gain
    - operator identify laser locaton and perform necessary tuning

## checkAndorEbeam.py
    script for checking E-beam on far detector Andor1
    - under development

## PVnamelist.py
    list of PVs of interest
    
## lowCharge.py
    nominal 10 fC initial pulse charge
    - verify using Farady cup
    
## highCharge.py
    nominal 50 fC initial pulse charge
    - verify using Farady cup

    

    
    