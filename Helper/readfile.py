# einfaches Snippet zum Auslesen der ersten Spalte aus einer Datei 

import csv
# datei oeffnen und am delimeter trennen
# durch bestimmen des delimeters (Trennzeichens)
# ist auch einfaches Auslesen anderer Spalten moeglich
# Weiterverarbeiten von Ausgaben der systemprogramme
with open('data.txt') as inf:
    reader = csv.reader(inf, delimiter=" ")
    
# Liest eine bestimmte Spalte aus
    col = list(zip(*reader))[0]
# bestimmen der anzahl der zeilen    
num_lines = sum(1 for line in open('data.txt'))

# 
for i in range(2,num_lines):
    print(col[i])
