# fuer python 3 auf windows
# ausfuehren von befehlen des Betriebssystems mit subprocess
# und speichern der Bildschirmausgabe in einem Bereich
# Dies ist ein Modul für cmd oder powershellbefehle unter
# Windows, das einen byte-Array zurueckliefert, der den
# gesamten Bildschirmtext der Befehlsausgabe an das aufrufende Programm
# uebergibt

def runcmd (befehl):
    import subprocess
    bereich = []
    process = subprocess.Popen(befehl,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE )
    for line in process.stdout:
        bereich.append(line)
    return bereich


# fuer python 3 auf windows
# formatieren der PIPE aus runcmd als eine Liste
# jede Ausgabezeile wird zu einem Listenelement im stringformat
# Sonderzeichen, Steuerungszeichen am Anfang und Ende der Strings werden
# ausgeblendet

def printdosscreen(bereich):
    anzahl = len(bereich)
    liste = []
    for zeile in range(0,anzahl):
        spaltenzahl = len(bereich[zeile])
        werte = []
        ausgebbar = ''
        for spalte in range(0,spaltenzahl-2):
            werte.append(chr(bereich[zeile][spalte]))
            ausgebbar = ausgebbar+werte[spalte]
        liste.append(ausgebbar)
    return liste
