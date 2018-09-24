# einping, ping_once
## Module zur Ermittlung des Standorts

## ping_once (Modul)

Einmaliges anpingen einer IP-Adresse oder eines Hostnamens (nur Deutsches Windows)
und setzen einer Variablen, ob der Host erreichbar ist bzw. existiert
Mässiger Zeitaufwand, wenn der Host nicht erreichbar ist.
IP-Adresse entweder im ipv4 Modus oder als auflösbarer Hostname. Es muss sichergestellt werden, dass die Namensauflösung funktioniert und icmp Pakete verarbeitet

## einping (Programm)

Enthält als einzige Option die IP-Adresse oder den Hostnamen und ruft die Funktionen in ping_once auf. Ping_once übergibt einen einfachen Wahrheitswert, der hier nur angezeigt wird und mit dem dann weiter gearbeitet werden kann.
Z.B. ist es möglich, über dieses Programm bestimmte Laufwerke einzubinden, wenn der Rechner an einem bestimmten Ort steht, an einem anderen Ort dann wiederum andere Laufwerke oder zu prüfen, ob im lokalen Netz bestimmte Rechner laufen und so Backups in Abhängigkeit zu starten.

## Hilfstool

Insgesamt steht hier ein simpler Ersatz für ping -n 1 <HOSTNAME> zur Verfügung, der fast nur zur Weiterverarbeitung dient, aber im Gegensatz zum ping-Befehl in Windows ohne die Systemvariable ERRORLEVEL auskommt, die hier fehlerhaft implementiert ist.
