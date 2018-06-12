"""
Ganz einfaches Tool zum sichern der installierten pip3 Pakete
in einer vorhandenen python installation
"""
from rundos import runcmd, printdosscreen

befehl = 'pip3 list'
fuehraus = runcmd (befehl)
erzeugteliste = printdosscreen(fuehraus)
datei = open("pip3data.txt","w+")
for werte in range(2,len(erzeugteliste)):
    erzeugteliste[werte] = " ".join(erzeugteliste[werte].split())
    datei.write (erzeugteliste[werte]+'\n')
datei.close()
