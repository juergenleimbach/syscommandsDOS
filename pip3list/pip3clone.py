# Template fuer befehle mit cmd-Befehlsinterpreter
# er hier gesetzte Befehl wird von cmd ausgeführt,
# erzeugteliste ist ein Array mit allen Bildschirmzeilen
# und kann zum Debuggen oder der weiterverarbeitung der Werte
# benutzt werden
from rundos import runcmd, printdosscreen
import csv

befehl = 'python.exe -m pip install --upgrade pip'
fuehraus = runcmd (befehl)
erzeugteliste = printdosscreen(fuehraus)
for werte in range(0,len(erzeugteliste)):
    print (erzeugteliste[werte])
with open('pip3data.txt') as inf:
    reader = csv.reader(inf, delimiter=" ")
    
    col = list(zip(*reader))[0]
num_lines = sum(1 for line in open('pip3data.txt'))
for i in range(0,num_lines):
    befehl = 'pip3 install '+col[i]
    fuehraus = runcmd (befehl)
    erzeugteliste = printdosscreen(fuehraus)
    for werte in range(0,len(erzeugteliste)):
        print (erzeugteliste[werte])

