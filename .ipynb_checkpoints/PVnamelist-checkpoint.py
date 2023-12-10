pvnamelist = []
# Gun PV names
pvnamelist.append('SIOC:AS01:KY01:0:AREQ') # gun amplitude
pvnamelist.append('SIOC:AS01:KY01:0:PREQ') # gun phase
pvnamelist.append('GUN:AS01:1:2:S_AACTUAL') # Gun amplitude calibration
pvnamelist.append('APC:AS01:TM01:M2_CH2_SPARE') # Gun body temperature:
pvnamelist.append('SIOC:AS01:KY01:0:ASET01') # Gun feedback correction coefficient

# Magnets setpoint
pvnamelist.append('SOLN:AS01:121:BCTRL') # gun solenoid
pvnamelist.append('SOLN:AS01:311:BCTRL') # 2nd solenoid
pvnamelist.append('QUAD:AS01:361:BCTRL') # Quad doublet 1st quad
pvnamelist.append('QUAD:AS01:371:BCTRL') # Quad doublet 2nd quad

# Magnet readback
pvnamelist.append('SOLN:AS01:121:BACT') # gun solenoid
pvnamelist.append('SOLN:AS01:311:BACT') # 2nd solenoid
pvnamelist.append('QUAD:AS01:361:BACT') # Quad doublet 1st quad
pvnamelist.append('QUAD:AS01:371:BACT') # Quad doublet 2nd quad

# correctors
pvnamelist.append('XCOR:AS01:121:BCTRL') #X00
pvnamelist.append('YCOR:AS01:122:BCTRL') #Y00
pvnamelist.append('XCOR:AS01:221:BCTRL') #X01
pvnamelist.append('YCOR:AS01:222:BCTRL') #Y01
pvnamelist.append('XCOR:AS01:321:BCTRL') #X02
pvnamelist.append('YCOR:AS01:322:BCTRL') #Y02
pvnamelist.append('XCOR:AS01:341:BCTRL') #X03
pvnamelist.append('YCOR:AS01:342:BCTRL') #Y03
pvnamelist.append('XCOR:AS01:381:BCTRL') #X04
pvnamelist.append('YCOR:AS01:382:BCTRL') #Y04

# 45 degree mirror motor
#pvnamelist.append('MOTR:AS01:MC08:CH2:MOTOR')  # for moving the mirror in and out

# sample stage motor
pvnamelist.append('ASTA:SMAR02:M1:MOTOR') # GUED chamber sample stage motor rel X
pvnamelist.append('ASTA:PI02:M3:MOTOR') # GUED chamber sample stage motor X
pvnamelist.append('ASTA:PI02:M2:MOTOR') # GUED chamber sample stage motor Y
pvnamelist.append('ASTA:PI02:M1:MOTOR') # GUED chamber sample stage motor Z

# collimator
pvnamelist.append('MOTR:AS01:MC03:CH7:MOTOR') # collimator position

# pump laser info
pvnamelist.append('MOTR:AS01:MC04:CH2:MOTOR')  # pump laser ND_wheel
pvnamelist.append('MOTR:AS01:MC04:CH3:MOTOR')  # pump laser half wave plate
pvnamelist.append('ASTA:LSC03:OC:OPEN') # pump laser shutter open
pvnamelist.append('ASTA:LSC03:OC:CLOSE') # pump laser shutter close

# gun UV info
pvnamelist.append('MOTR:AS01:MC03:CH1:MOTOR')  # gun UV throttle
pvnamelist.append('ASTA:LSC01:OC:OPEN') # gun UV shutter open
pvnamelist.append('ASTA:LSC01:OC:CLOSE') # gun UV shutter close

# far detector phosphor screen
pvnamelist.append('ASTA:BO:2114-9:BIT2')


### camera size info########
#VCC size info
pvnamelist.append('ASPS05:image1:ArraySize0_RBV') # VCC sizeX
pvnamelist.append('ASPS05:image1:ArraySize1_RBV') # VCC sizeY
pvnamelist.append('ASPS05:ROI1:MinX')
pvnamelist.append('ASPS05:ROI1:MinY')
pvnamelist.append('ASPS05:ROI1:SizeX')
pvnamelist.append('ASPS05:ROI1:SizeY')

#gas chamber cam size info
pvnamelist.append('ASPS04:image1:ArraySize0_RBV') # VCC sizeX
pvnamelist.append('ASPS04:image1:ArraySize1_RBV') # VCC sizeY
pvnamelist.append('ASPS04:ROI1:MinX')
pvnamelist.append('ASPS04:ROI1:MinY')
pvnamelist.append('ASPS04:ROI1:SizeX')
pvnamelist.append('ASPS04:ROI1:SizeY')

#ANDOR size info
pvnamelist.append('ANDOR1:image1:ArraySize0_RBV') # VCC sizeX
pvnamelist.append('ANDOR1:image1:ArraySize1_RBV') # VCC sizeY
pvnamelist.append('ANDOR1:ROI1:MinX')
pvnamelist.append('ANDOR1:ROI1:MinY')
pvnamelist.append('ANDOR1:ROI1:SizeX')
pvnamelist.append('ANDOR1:ROI1:SizeY')


### camera readouts########
# VCC
# pvnamelist.append('ASPS05:image1:ArrayData') # VCC image
pvnamelist.append('ASPS05:Stats1:SigmaX_RBV') # VCC beam size X
pvnamelist.append('ASPS05:Stats1:SigmaY_RBV') # VCC beam size Y
pvnamelist.append('ASPS05:Stats1:CentroidX_RBV') # VCC beam centroid X
pvnamelist.append('ASPS05:Stats1:CentroidY_RBV') # VCC beam centroid Y
pvnamelist.append('ASPS05:Stats1:Total_RBV') # VCC beam total count

# gas chamber cam
# pvnamelist.append('ASPS04:image1:ArrayData') # cam image
pvnamelist.append('ASPS04:Stats1:SigmaX_RBV') # beam size X
pvnamelist.append('ASPS04:Stats1:SigmaY_RBV') #  beam size Y
pvnamelist.append('ASPS04:Stats1:CentroidX_RBV') #  beam centroid X
pvnamelist.append('ASPS04:Stats1:CentroidY_RBV') #  beam centroid Y
pvnamelist.append('ASPS04:Stats1:Total_RBV') #  beam total count

# Andor1
#pvnamelist.append('ANDOR1:image1:ArrayData') # Andor1 image
pvnamelist.append('ANDOR1:Stats1:SigmaX_RBV') # Andor1 beam size X
pvnamelist.append('ANDOR1:Stats1:SigmaY_RBV') # Andor1 beam size Y
pvnamelist.append('ANDOR1:Stats1:CentroidX_RBV') # Andor1 beam centroid X
pvnamelist.append('ANDOR1:Stats1:CentroidY_RBV') # Andor1 beam centroid Y
pvnamelist.append('ANDOR1:Stats1:Total_RBV') # Andor1 beam total count

### camera settings##########
# gas chamber cam
pvnamelist.append('ASPS04:cam1:Gain') # gas chamber camera gain
pvnamelist.append('ASPS04:cam1:AcquireTime') # gas chamber camera gain



# Chamber light
pvnamelist.append('ACSW:AS01:NW03:2POWERON') # gas chamber light on
pvnamelist.append('ACSW:AS01:NW03:2POWEROFF') # gas chamber light off
