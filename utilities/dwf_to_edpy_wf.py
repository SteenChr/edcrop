# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:44:19 2021

@author: au156185
"""
import pandas as pd
import numpy as np

def vapor_pressure_gradient(T):
    ### Use Tetens equation c.f.
    ### https://en.wikipedia.org/wiki/Vapour_pressure_of_water
    print(type(T))
    a = np.reciprocal(T+237.3)
    b = np.multiply(T, a)
    c = np.multiply(b, a)
    P = 610.78*np.exp(17.27*b)
    dPdT = np.multiply(17.27*(a - c),P)
    return(dPdT)

def makkink(T, Rad, radunit="MJ/d"):
    """ 
    Computes potential evapotranspiration (Ep) by Makkink's 
    approximation as given by eq. (3.1), p. 23 in
    
    "Olesen, J.E., and Heidmann, T. (2002). EVACROP – Et program 
    til beregning af aktuel fordampning og afstrømning fra 
    rodzonen, Version 1.01. Afdeling for Plantevækst og Jord og 
    Afdeling for Jordbrugssystemer, Forskningscenter Foulum, 
    Tjele, Danmark."
    
    Input:
        Temperature in deg. C.
        Global radiation in MJ/m^2/day (default) or W/m^2.
        unit (optional): either "MJ/d" (default) or "W/m2".
        
    Returns:
        Ep in mm/d
    """
    
    c = {"MJ/d": 1.0, "W/m2": 0.0864}
    
    s = vapor_pressure_gradient(T)
    lamb = 2.465 # MJ/mm, heat of evaporation for water
    gam = 66.7 # Pa/deg C, psycrometric constant
    
    Ep = c[radunit]*np.multiply(np.divide(s, s+gam),Rad)*0.7/lamb
    
    return(Ep)    
    
"""
Code to convert Daisy-Weather-File (dwf) to ed.py climate file. 

Potential evapotranspiration is computed by Makkink's approximation.

Coded by: Steen Christensen, Feb. 2021.
"""

# Input and output file names
fname = "100648019.dwf"      # Name of dwf input file
fnam2 = "100648019.edpy_wf"  # Name ed.py weather file (output)

# Read Daisy Weather File
colnames = ["year", "month", "day", "Rad", "T", "P"]
df = pd.read_csv(fname,skiprows=36,header=None, names=colnames, 
                 delim_whitespace=True, parse_dates={"date":[0,1,2]})

# Compute Er from global radiation and temperature by Makkink
Er = makkink(df["T"].iloc[:].as_matrix(), 
             df["Rad"].iloc[:].as_matrix(), radunit = "W/m2")

df1 = df.copy()
df1.drop("Rad", axis=1, inplace=True)
df1.insert(loc=len(df1.columns), column="Eref", value=Er)
df1
prlist = ["date","T","P","Eref"]
colalias=[prlist[0].ljust(10)]
for i in range(1,len(prlist)):
    colalias.append(prlist[i].rjust(8))

df1.to_csv(fnam2, index=False, columns=prlist,\
  float_format="%8.3f", header=colalias)#, sep=' ')#sep='\s+')