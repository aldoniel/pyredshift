#!/usr/bin/python3

import easygui as eg
import subprocess

def run(command:str):
    try:
        subprocess.run(command, shell=True, check=True)
    except Exception:
        eg.exceptionbox(command)
        exit(1)
        
def removechar(string:str)->int:
    l:list=[]
    for c in string:
        if c.isdigit():
            l.append(c)
    return int("".join(l))

def main():
    liste:tuple=("3000K","day (6500K)","night (4500K)","4000K","2500K","2000K","1000K")
    ret=eg.choicebox("Choose a temperature","Redshift",liste)
    if ret==None:
        exit(0)
    ret=removechar(ret)
    run(f"redshift -P -O{ret}")
    
try:
    main()
except Exception:
    eg.exceptionbox("main")
    exit(1)
