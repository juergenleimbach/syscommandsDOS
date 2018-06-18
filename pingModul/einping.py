"""
Beispielaufruf fuer ping_once -
kann weiter ausgearbeitet, indem die Rückgabewerte
verarbeitet werden
"""
from ping_once import auswertung, einping

befehl = 'ping -n 1 misthaufen'
fertig = einping(befehl)
print (fertig)

