# Template fuer befehle mit cmd-Befehlsinterpreter
# er hier gesetzte Befehl wird von cmd ausgeführt,
# erzeugteliste ist ein Array mit allen Bildschirmzeilen
# und kann zum Debuggen oder der weiterverarbeitung der Werte
# benutzt werden
from rundos import runcmd, printdosscreen

befehl = 'pip3 list'
fuehraus = runcmd (befehl)
erzeugteliste = printdosscreen(fuehraus)

# Debugging / Weiterverwertung
# des Bildschirminhalts in weiteren Programmteilen
# auskommentieren für eine lesbare Liste
for werte in range(0,len(erzeugteliste)):
    print (erzeugteliste[werte])
