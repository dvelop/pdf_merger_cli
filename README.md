# 📄 Interactive PDF Merger CLI
Ein interaktives Command-Line Interface (CLI) Tool in Python zum schnellen Suchen, Sortieren und Zusammenführen von PDF-Dateien direkt im Terminal.
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
---
## 📸 Features
🔎 Automatische Suche: Durchsucht das gewählte Verzeichnis rekursiv nach allen `.pdf`-Dateien.
☑️ Komfortable Mehrfachauswahl: Interaktive Auswahl von Dateien mit Pfeiltasten und Leertaste.
🔀 Flexible Reihenfolge: Einfaches Festlegen der Reihenfolge der zusammenzuführenden Dokumente.
🔒 100% Lokal & Sicher: Keine Daten werden ins Internet hochgeladen – ideal für vertrauliche Dokumente.
📦 Portable Executable: Kann mit PyInstaller als eigenständige `.exe`-Datei für Windows gebuildet werden.
---
## 🚀 Schnelleinstieg (Python)
Voraussetzungen
Stelle sicher, dass Python (Version 3.8 oder neuer) installiert ist.
1. Repository klonen
```bash
git clone https://github.com/DEIN-BENUTZERNAME/pdf-merger-cli.git
cd pdf-merger-cli
```
2. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```
(Oder manuell: `pip install pypdf questionary`)
3. Skript ausführen
```bash
python pdf_merger.py
```
---
## 🛠️ Verwendung
Suchordner angeben: Gib den Pfad ein, in dem nach PDFs gesucht werden soll (Standard: aktuelles Verzeichnis `.`).
Dateien auswählen: Navigiere mit `↑` / `↓` durch die Liste, wähle gewünschte Dateien mit `Leertaste` aus und bestätige mit `Enter`.
Reihenfolge festlegen: Bestimme nacheinander die Positionen der ausgewählten Dateien.
Dateiname eingeben: Gib den Namen der fertigen PDF-Datei an (z. B. `zusammengefuehrt.pdf`).
---
## 🖥️ Eigenständige Executable (.exe) erstellen
Du kannst das Skript mit PyInstaller in eine eigenständige Windows-Anwendung umwandeln, die ohne Python-Installation läuft:
```bash
# PyInstaller installieren
pip install pyinstaller

# .exe-Datei generieren
pyinstaller --onefile --console pdf_merger.py
```
Die fertige `.exe`-Datei findest du anschliessend im Ordner `dist/pdf_merger.exe`.
---
## 🧰 Verwendete Bibliotheken
pypdf – Zusammenführen und Verarbeiten der PDF-Dateien.
questionary – Interaktive Terminal-Menüs und Prompts.
---
📜 Lizenz
Siehe die LICENSE Datei für Details.
