'''
The gppyield function takes a primary energy and observation angle
and returns the predicted gamma ray yield in bins of x = E_gamma/E_CR. The
primary energy is rounded to nearest value, no interpolation between energies.
The angle designates the angular bin, there is no interpolation between bins.
If the angle is on a bin edge it rounds down to the lower bin.
Function returns a series of pairs. The first value is x which refers to the 
center of the x bin. The second value is the yield: d^2 N/dx dOmega.

Example:
    To obtain the yield for a 6.2 GeV incident proton at an angle of 13.7 deg
    
    gppyield(6.2, 13.7)
    
    This returns the yields in x-bins for a 5.62 GeV proton, since this is the 
    closest primary energy in the database, in the 10 to 15 deg angular bin
'''

import numpy as np
import sqlite3

#Values used for incident cosmic rays (coincide with the gamma ray energy bins)
Ecr = np.array([1.33, 1.78, 2.37, 3.16, 4.22, 5.62, 7.5, 10, 13.3, 17.8, 23.7, 31.6, 
              42.2, 56.2, 75, 100])      
#Left edges of angular bins
theta = np.linspace(0 ,175, 36)
#Middles of angular bins
thetaCtrs = np.linspace(0 ,180, 73)[1::2]
#Angular bins in format convenient for querying database
theta_names = theta.astype(int).astype(str)
for i in range(len(theta)):
    theta_names[i] = 'deg' + theta_names[i]

#Load database
db_file_path = 'gammappdata.db'
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

def gppyield(primEnergy, angle):
    primEnergy = float(primEnergy)
    angle = float(angle)
    if 0 <= angle <= 180:
    	pass
    else:
    	raise ValueError('Angle relative to the primary must be between 0 and 180 degrees')
    if 1.22 <= primEnergy <= 100:
    	pass
    else:
    	raise ValueError('Primary energy must be between 1.22GeV (pion production threshold) and 100GeV')  
    idxEnergy = np.argmin(np.abs(Ecr - primEnergy))
    idxTheta = np.argmin(np.abs(thetaCtrs - angle))
    return cursor.execute("SELECT xval, " + theta_names[idxTheta] + " FROM '" + str(Ecr[idxEnergy]) + "GeV Ep'").fetchall()

