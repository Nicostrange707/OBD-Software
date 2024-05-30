# OBD-Software
| Version | Betriebsystem |
| ------- | ------------ |
| 1       | Windows 10 |
| 2       | Windows 10 |
| 3       | Web Anwendung und Raspberry PI |

## Installation auf Windows für Version 1&2
Als erstes Installeren sie: `pip install obd`

Um die Version 1 zu starten muss der Befehlt `python OBD-GUI.py` ausgeführt werden.
Um die Version 2 zu starten muss der Befehlt `python main.py` ausgeführt werden.

## Installation auf Raspberry Pi und Webserver für Version 3
Ordner PI-API:
script.py ist die Datei die auf dem Raspberry Pi ausgeführt werden muss mit dem Befehl `python3 script.py` um die API für das Webinterface zu starten und die OBD Daten zu übertragen.

Ordner Webinterface-OBD_II:
Das Webinterface ist mit Angular 16 erstellt. Erster Befehlt um das Webinterface zu installieren: `npm install`. Danach `ng serve --o` um es zu starten.


## Alle Befehle in der Übersicht

| Version | Bereich | Befehl |
| ------- | ------- | ------ |
| 1       | Cmd | `python OBD-GUI.py` |
| 2       | Cmd | `python main.py` |
| 3       | Raspberry Pi CLI | `python3 script.py` |
|         | Ordner Webinterface-OBD_II (vor dem Erstellen des dist Verzeichnisses zum deployen)|`npm install`,`ng serve --o` |
