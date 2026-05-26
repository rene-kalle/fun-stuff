# Fun-Stuff

Kurze Sammlung von kleinen, unterhaltsamen Python-Scripts — nicht ernst nehmen.

## Enthaltene Skripte

- `hacker-games.py` — Konsolen-Sammlung von spielerischen "Hacking"-Simulationen und Tools (nur Simulation / Entertainment):
    - Network Scanning (zufällige IP-Listen)
    - Password Cracking Simulation (Dateiauswahl, zufällige Treffer)
    - John-the-Ripper Simulation (Hash/Wordlist Eingabe)
    - Distributed Denial of Service (Dauer-Simulation)
    - Data Exfiltration Simulation
    - System Bypass Simulation
    - Phone Tracking (zufällige Koordinaten)
    - Security Camera Feed Simulation
    - Oracle Operations (zeigt eine ProgressBar an)
    - ASCII-Willkommensbildschirm, Login-Screen mit Demo-Accounts, Fortschrittsbalken und diverse Hilfsfunktionen

- `easter_egg_terminal.py` — Interaktives "Dev Easter Egg" Terminal mit bunten Ausgaben und kleinen Gags:
    - Befehle: `joke`, `abap`, `bug`, `git`, `status`, `excuse`, `coffee`, `deploy`, `standup`, `matrix`, `konami`, `all`, `help`
    - `help` zeigt alle möglichen Kommandos an
    - `all` demonstriert alle Kommandos
    - Typing-Effekte, Spinner, Zufallstexte (Witze, ABAP-Snippets, Git-Logs, Team-Status, etc.)

- `color-health-bar.py` — Einfaches Terminal-UI zur Darstellung von Lebens- und Manabaren (ANSI-Farben), interaktiv, `q` zum Beenden.

## Voraussetzungen

- Python 3.10+ empfohlen
- Optional: `colorama` für bessere Farbunterstützung auf Windows (installieren mit `pip install colorama`)

## Nutzung

Starte ein Script in der Konsole mit:

```
python hacker-games.py
python easter_egg_terminal.py
python color-health-bar.py
```

Hinweis für Windows: Manche Terminals unterstützen ANSI-Farben nicht vollständig. Entweder ein ANSI-fähiges Terminal verwenden (Windows Terminal, PowerShell 7+, WSL) oder `colorama` installieren.

## Sicherheitshinweis

Alle Skripte sind rein unterhaltend und simulieren Aktionen — sie führen keine echten Angriffe oder Datenübertragungen aus.

Viel Spaß beim Ausprobieren!
