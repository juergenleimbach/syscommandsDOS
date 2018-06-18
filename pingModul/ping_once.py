"""
Mini-Modul, das einzelnes Ping an einen Host sendet, um zu erfahren, ob dieser
existiert oder erreichbar ist. Kann verwendet werden, um z.B. sicherzustellen,
dass eine bestimmte Umgebung oder ein bestimmter Standort existiert.
Kann verwendet werden, um Router bzw. Internetzugriff zu erkennen.
Aufrufbeispiel => einping.py
"""
from rundos import runcmd, printdosscreen

def auswertung(ausgabe):
# nur deutsches MS-Ping:
# wenn Seite nicht bekannt / keine IP
        if (ausgabe[0] != ''):
            return 'NoHost'
# wenn Seite erreichbar
        else:
                if (ausgabe[5][-1] == '0'):
                        return 'isHost'
# wenn Seite nicht erreichbar
                else:
                        return 'NoHost'

def einping(befehl):
        fuehraus = runcmd (befehl)
        erzeugteliste = printdosscreen(fuehraus)
        fertig = auswertung(erzeugteliste)
        return fertig
