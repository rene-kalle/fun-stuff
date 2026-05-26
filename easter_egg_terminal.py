#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════╗
║   🐣  Dev Easter Egg Terminal  🐣            ║
║   Für das beste ABAP-Team diesseits der SAP  ║
╚══════════════════════════════════════════════╝
Starten mit:  python easter_egg_terminal.py
Beenden mit:  exit  oder  Ctrl+C
"""

import os
import sys
import time
import random
import shutil
import itertools
import threading

# ── ANSI-Farben ──────────────────────────────────────────────────────────────


class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PINK = "\033[95m"
    CYAN = "\033[96m"
    RED = "\033[91m"
    GRAY = "\033[90m"
    WHITE = "\033[97m"


def c(color, text):
    return f"{color}{text}{C.RESET}"


# ── Hilfsfunktionen ───────────────────────────────────────────────────────────


def clear_screen():
    """Bildschirm löschen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def typewrite(text, delay=0.022, newline=True):
    """Text Zeichen für Zeichen ausgeben wie ein echtes Terminal."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()


def slow_print(text, delay=0.04):
    """Zeilenweise mit Verzögerung ausgeben."""
    for line in text.strip().splitlines():
        print(line)
        time.sleep(delay)


def hr(char="─", color=C.GRAY):
    width = min(shutil.get_terminal_size().columns, 72)
    print(c(color, char * width))


def prompt():
    return f"{c(C.GREEN, 'dev@team')}:{c(C.BLUE, '~/projekt')}$ "


def spinner(label, duration=1.2):
    """Kleiner Spinner für 'Ladeeffekte'."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{c(C.CYAN, frames[i % len(frames)])} {label}  ")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r{c(C.GREEN, '✔')} {label}  \n")
    sys.stdout.flush()


# ── Easter-Egg-Inhalte ────────────────────────────────────────────────────────

JOKES = [
    ("Warum debuggen Entwickler im Dunkeln?", "Weil Licht Bugs anzieht. 🪲"),
    ("Wie nennt man einen schlafenden Programmierer?", "Ein Deadlock. 💤"),
    (
        "99 kleine Bugs im Code …",
        "Einen gepatcht, neu kompiliert —\n     127 kleine Bugs im Code. 😅",
    ),
    (
        "Wie viele Entwickler braucht man, um eine Glühbirne zu wechseln?",
        "Keine – das ist ein Hardware-Problem. 💡",
    ),
    (
        "Was sagt ein Java-Entwickler beim Camping?",
        '"Kein Heap, kein Stack – nur noch Stack Trace." ⛺',
    ),
    (
        "Was ist der Unterschied zwischen einem Bug und einem Feature?",
        "Die Dokumentation. 📄",
    ),
    ("Warum mögen Programmierer keine Natur?", "Zu viele Bugs. 🌿"),
    (
        "Ein SQL-Query betritt eine Bar und bestellt:",
        '"SELECT beer FROM taps WHERE price < 5 ORDER BY taste DESC LIMIT 1;" 🍺',
    ),
]

ABAP_SNIPPETS = [
    (
        "DATA: lv_todo TYPE string VALUE 'TODO: Fix later'.",
        "Seit 2019 im Code. Later = never. 😬",
    ),
    (
        '" Author: Unbekannt\n" Datum:  irgendwann mal\n" Status: funktioniert irgendwie',
        "Die ehrlichste Dokumentation aller Zeiten.",
    ),
    (
        'IF sy-subrc <> 0.\n  " Das sollte nicht passieren\nENDIF.',
        "Es ist passiert. Es wird wieder passieren. 🎯",
    ),
    (
        "SELECT * FROM mara\n  WHERE matnr LIKE '%TEST%'.",
        "⚠️  Nie im Produktivsystem. Versprochen. 🤞",
    ),
    (
        'LOOP AT lt_data INTO ls_data.\n  " TODO: Performance optimieren\nENDLOOP.',
        "Nur 2 Mio. Einträge. Wird schon. ⏳",
    ),
    (
        '" Dieser Code ist Magie.\n" Nicht anfassen.\n" Wirklich.',
        "Der Autor hat die Firma verlassen. 👻",
    ),
    (
        'CATCH cx_root INTO lx_error.\n  " Fehler ignorieren\nENDTRY.',
        "Exception-Handling auf höchstem Niveau. 🏆",
    ),
]

BUG_TYPES = [
    (
        "SCHRÖDINGER-BUG 🔬",
        "Tritt nur auf, wenn du deinem Chef zuschaust.\nBeim Einzeltest: nie reproduzierbar.",
    ),
    (
        "NINJA-BUG 🥷",
        "Erscheint lautlos am Freitagabend.\nIst am Montag wieder weg. War er jemals da?",
    ),
    (
        "HEISENBUG 👁️",
        "Verschwindet, wenn man debuggt.\nAls ob der Code weiß, dass er beobachtet wird.",
    ),
    ("BOHRBUG 😤", "Immer da. Immer gleich.\nWartet geduldig bis ins Produktivsystem."),
    (
        "MANDELBUG 🌀",
        "Ursache so komplex, dass niemand sie versteht.\nWird offiziell als 'Feature' eingetragen.",
    ),
    (
        "LURCH-BUG 🐊",
        "Verursacht durch Code, der 'vorübergehend'\nvor 4 Jahren eingefügt wurde.",
    ),
]

GIT_LOG = [
    ("a1b2c3d", "Fix: Das hier war meine Schuld. Tut mir leid."),
    ("e4f5a6b", "Revert: Revert: Revert: fix cors"),
    ("c7d8e9f", "Emergency: Bitte nicht lesen"),
    ("1a2b3c4", "Merge branch 'hotfix' into 'hotfix-2' into 'hotfix-final'"),
    ("5d6e7f8", "Update README (lügt immer noch)"),
    ("9a0b1c2", "Performance: Hat nichts geholfen, klingt aber gut im Sprint Review"),
    ("d3e4f5a", "temp (ACHTUNG: bitte nicht anfassen)"),
    ("6b7c8d9", "WIP WIP WIP WIP WIP"),
    ("e0f1a2b", "Final_FINAL_v2_WIRKLICHFINAL.abap"),
    ("3c4d5e6", "Ich weiß nicht warum das funktioniert, aber es tut es"),
    ("f7a8b9c", "Diesen Commit werde ich eines Tages bereuen"),
    ("0d1e2f3", "Hotfix für den Hotfix des letzten Hotfixes"),
]

TEAM_STATUSES = [
    ("Jenkins", "🔴", "Build: FAILED (wie immer)"),
    ("Prod-System", "🟢", "Läuft. Nicht anfassen."),
    ("Doku", "🦗", "Wird noch aktualisiert (seit 2022)"),
    ("Staging", "🟡", "Irgendwie anders als Prod – keiner weiß warum"),
    ("Test-Daten", "🗑️", "Entsprechen nicht der Realität. Nie."),
    ("Sprint-Ziel", "📅", "Wird in das nächste Sprint übernommen"),
    ("Tech-Debt", "📈", "Wächst schneller als das Team"),
    ("Code-Review", "⏳", "Seit 3 Wochen 'fast fertig'"),
]

EXCUSES = [
    '"Funktioniert bei mir lokal!" 🖥️',
    '"Das war schon immer so." 🏛️',
    '"Haben wir das denn getestet?" 🤔',
    '"Das Ticket war nicht klar genug." 📋',
    '"Ich dachte das wäre optional." 😶',
    '"Der letzte Commit war nicht von mir." 👀',
    '"Das ist eigentlich ein Feature." ✨',
    '"In der Anforderung stand das nicht!" 📄',
    '"Das Deployment war schuld." 🚀',
    '"Wir brauchen erstmal ein Meeting dazu." 📅',
]

COFFEE_LEVELS = [
    (0, "KRITISCH", "🪫", "Sofort Kaffeemaschine aufsuchen!"),
    (25, "NIEDRIG", "🔋", "Zweite Tasse dringend empfohlen."),
    (50, "STABIL", "☕", "Ausreichend für einfache Tickets."),
    (75, "GUT", "⚡", "Bereit für Code-Reviews."),
    (100, "OPTIMAL", "🚀", "Produktivitätspeak. Jetzt deployen!"),
]

# ── Befehle ───────────────────────────────────────────────────────────────────


def cmd_joke(args=None):
    """Zeigt einen zufälligen Entwickler-Witz."""
    q, a = random.choice(JOKES)
    print()
    typewrite(c(C.YELLOW, f"  ❓ {q}"), delay=0.018)
    time.sleep(0.5)
    typewrite(c(C.GREEN, f"  ✅ {a}"), delay=0.018)
    print()


def cmd_abap(args=None):
    """Zeigt einen schmerzhaft echten ABAP-Code-Kommentar."""
    code, note = random.choice(ABAP_SNIPPETS)
    print()
    for line in code.splitlines():
        print(f"  {c(C.PINK, line)}")
    print()
    typewrite(c(C.GRAY, f"  // Code-Review: ") + c(C.YELLOW, note), delay=0.015)
    print()


def cmd_bug(args=None):
    """Klassifiziert einen zufälligen Bug-Typ."""
    name, desc = random.choice(BUG_TYPES)
    print()
    spinner("Analysiere Bug-Muster", 1.0)
    print(f"  {c(C.RED, c(C.BOLD, '🐛 Typ: ' + name))}")
    print()
    for line in desc.splitlines():
        print(f"  {c(C.WHITE, line)}")
    print()


def cmd_git(args=None):
    """Gibt einen ehrlichen Git-Log aus."""
    print()
    entries = random.sample(GIT_LOG, min(6, len(GIT_LOG)))
    for h, msg in entries:
        print(f"  {c(C.YELLOW, h)}  {c(C.WHITE, msg)}")
    print()


def cmd_status(args=None):
    """Zeigt den ehrlichen Team-Status."""
    print()
    hr()
    print(c(C.CYAN, c(C.BOLD, "  TEAM STATUS — LIVE")))
    hr()
    items = random.sample(TEAM_STATUSES, min(5, len(TEAM_STATUSES)))
    for name, icon, status in items:
        pad = 14 - len(name)
        print(f"  {icon}  {c(C.YELLOW, name)}{' ' * pad}{c(C.GRAY, status)}")
    hr()
    print()


def cmd_excuse(args=None):
    """Generiert eine professionelle Entwickler-Ausrede."""
    print()
    spinner("Generiere Ausrede", 0.8)
    excuse = random.choice(EXCUSES)
    typewrite(c(C.CYAN, f"  💬 {excuse}"), delay=0.020)
    print()


def cmd_coffee(args=None):
    """Misst den aktuellen Kaffee-Level."""
    try:
        level = int(args[0])  # type: ignore
        if level < 0:
            level = 0
        elif level > 100:
            level = 100
    except (IndexError, ValueError, TypeError):
        level = random.randint(0, 100)
    # Finde passende Kategorie
    cat_pct, cat_name, cat_icon, cat_msg = COFFEE_LEVELS[0]
    for pct, name, icon, msg in COFFEE_LEVELS:
        if level >= pct:
            cat_pct, cat_name, cat_icon, cat_msg = pct, name, icon, msg
    print()
    spinner("Messe Koffein-Level", 1.1)
    bar_filled = int(level / 5)
    bar = "█" * bar_filled + "░" * (20 - bar_filled)
    color = C.RED if level < 30 else C.YELLOW if level < 60 else C.GREEN
    print(f"  {cat_icon}  {c(color, bar)}  {c(C.BOLD, str(level) + '%')}")
    print(f"  Status: {c(color, cat_name)} — {c(C.GRAY, cat_msg)}")
    print()


def cmd_deploy(args=None):
    """Simuliert ein Produktions-Deployment."""
    print()
    steps = [
        ("Tests werden ausgeführt", True, 0.9),
        ("Code-Qualität wird geprüft", True, 0.7),
        ("Backup wird erstellt", True, 0.6),
        ("Deployment auf Staging", True, 0.8),
        ("Smoke Tests", True, 0.5),
        ("Deployment auf Produktion", True, 1.2),
        ("Cache wird geleert", False, 0.4),  # geht mal schief
        ("Monitoring wird benachrichtigt", True, 0.5),
    ]
    print(c(C.BOLD, "  🚀 Deployment gestartet...\n"))
    for label, ok, dur in steps:
        spinner(label, dur)
        if not ok:
            print(
                f"  {c(C.RED, '⚠️  Warnung: ')}Cache-Clearing schlägt fehl (wie immer). Ignoriert."
            )
    print()
    time.sleep(0.3)
    typewrite(
        c(C.GREEN, c(C.BOLD, "  ✅ Deployment erfolgreich! (Finger gedrückt halten)")),
        delay=0.015,
    )
    print(
        c(
            C.GRAY,
            "  Hotline: +49-XXX-XXXXXXX  |  Notfall-Rollback: hoffentlich nicht nötig",
        )
    )
    print()


def cmd_standup(args=None):
    """Generiert ein auto-generiertes Daily Standup."""
    done = random.choice(
        [
            "Bug untersucht (Ursache noch unklar)",
            "Technischen Debt dokumentiert (nicht behoben)",
            "Code Review kommentiert",
            "Meeting über das nächste Meeting vorbereitet",
            "Komplexes Ticket in kleinere Tickets aufgeteilt",
        ]
    )
    todo = random.choice(
        [
            "Ticket #" + str(random.randint(1000, 9999)) + " angehen (vermutlich)",
            "Den gleichen Bug von gestern weiter untersuchen",
            "Endlich die TODOs anschauen",
            "Doku schreiben (optimistisch)",
            "Performance-Problem analysieren",
        ]
    )
    blocker = random.choice(
        [
            "Keiner (lüge)",
            "Warte auf Antwort aus dem Fachbereich (seit Dienstag)",
            "Build ist wieder kaputt",
            "Brauche Zugang zu Testsystem",
            "Zu viele Meetings heute",
        ]
    )
    print()
    print(c(C.BOLD, c(C.CYAN, "  📅 DAILY STANDUP — AUTO-GENERIERT")))
    print()
    print(f"  {c(C.GRAY, 'Gestern:')}  {c(C.WHITE, done)}")
    print(f"  {c(C.GRAY, 'Heute:  ')}  {c(C.WHITE, todo)}")
    print(f"  {c(C.GRAY, 'Blocker:')}  {c(C.YELLOW, blocker)}")
    print()


def cmd_matrix(args=None):
    """Kurze Matrix-Animation."""
    print()
    cols = min(shutil.get_terminal_size().columns - 2, 70)
    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノ"
    try:
        for _ in range(12):
            line = "".join(random.choice(chars) for _ in range(cols))
            color = random.choice([C.GREEN, C.CYAN, C.GRAY])
            print(c(color, line))
            time.sleep(0.07)
    except KeyboardInterrupt:
        pass
    print()
    typewrite(c(C.GREEN, "  Du nimmst die rote Pille... 💊"), delay=0.025)
    print()


def cmd_konami(args=None):
    """Der Konami-Code Easter Egg."""
    print()
    typewrite(c(C.YELLOW, "  ↑ ↑ ↓ ↓ ← → ← → B A"), delay=0.08)
    time.sleep(0.4)
    print()
    lines = [
        c(C.GREEN, c(C.BOLD, "  🎉 KONAMI CODE AKTIVIERT! 🎉 ")),
        "",
        c(C.YELLOW, "  +30 Leben") + c(C.WHITE, " wurden deinem Projekt hinzugefügt."),
        c(C.WHITE, "  Alle Bugs wurden nach ")
        + c(C.PINK, "/dev/null")
        + c(C.WHITE, " verschoben."),
        c(C.WHITE, "  Deployment läuft auf ") + c(C.GREEN, "GRÜN") + c(C.WHITE, ". 🚀"),
        "",
        c(C.GRAY, "  Ein Klassiker seit 1986. ✨"),
    ]
    for line in lines:
        print(line)
        time.sleep(0.12)
    print()


def cmd_help(args=None):
    """Zeigt alle verfügbaren Befehle."""
    print()
    hr("═", C.CYAN)
    print(c(C.CYAN, c(C.BOLD, "  🐣 DEV EASTER EGG TERMINAL — Verfügbare Befehle")))
    hr("═", C.CYAN)
    commands_help = [
        ("joke", "Zufälliger Entwickler-Witz"),
        ("abap", "Echter ABAP-Code mit Kommentar"),
        ("bug", "Bug-Typ-Klassifizierung"),
        ("git", "Ehrlicher Git-Log"),
        ("status", "Team- & System-Status"),
        ("excuse", "Professionelle Entwickler-Ausrede"),
        ("coffee", "Koffein-Level messen (Level kann optional angegeben werden)"),
        ("deploy", "Produktions-Deployment simulieren"),
        ("standup", "Daily Standup auto-generieren"),
        ("matrix", "Die Wahrheit sehen 🟩"),
        ("konami", "↑↑↓↓←→←→BA"),
        ("all", "Alle Easter Eggs nacheinander"),
        ("help", "Diese Hilfe anzeigen"),
        ("exit", "Terminal beenden"),
    ]
    for cmd, desc in commands_help:
        pad = 10 - len(cmd)
        print(f"  {c(C.GREEN, cmd)}{' ' * pad}{c(C.GRAY, desc)}")
    hr("═", C.CYAN)
    print()


def cmd_all(args=None):
    """Führt alle Easter Eggs nacheinander aus."""
    all_cmds = [
        cmd_joke,
        cmd_abap,
        cmd_bug,
        cmd_git,
        cmd_status,
        cmd_excuse,
        cmd_coffee,
        cmd_deploy,
        cmd_standup,
        cmd_matrix,
        cmd_konami,
    ]
    for fn in all_cmds:
        hr("·", C.GRAY)
        fn()
        time.sleep(1.0)


# ── Befehlsregister ───────────────────────────────────────────────────────────

COMMANDS = {
    "joke": cmd_joke,
    "abap": cmd_abap,
    "bug": cmd_bug,
    "git": cmd_git,
    "status": cmd_status,
    "excuse": cmd_excuse,
    "coffee": cmd_coffee,
    "deploy": cmd_deploy,
    "standup": cmd_standup,
    "matrix": cmd_matrix,
    "konami": cmd_konami,
    "all": cmd_all,
    "help": cmd_help,
    "?": cmd_help,
}

# ── Boot-Sequenz ──────────────────────────────────────────────────────────────


def boot():
    print()
    hr("═", C.CYAN)
    title = "  🐣  DEV EASTER EGG TERMINAL  🐣"
    print(c(C.CYAN, c(C.BOLD, title)))
    print(c(C.GRAY, "  Für das beste ABAP-Team diesseits der SAP"))
    hr("═", C.CYAN)
    print()
    boot_msgs = [
        ("Lade Kaffee-Abhängigkeiten", 0.7),
        ("Ignoriere Tech-Debt", 0.5),
        ("Kopiere Stack Overflow Antwort", 0.8),
        ("Pretende, Tests zu schreiben", 0.6),
        ("System bereit", 0.4),
    ]
    for msg, dur in boot_msgs:
        spinner(msg, dur)
    print()
    typewrite(
        c(C.GREEN, "  Gib 'help' ein für alle Befehle. Viel Spaß! 🎉"), delay=0.018
    )
    print()


# ── Main Loop ────────────────────────────────────────────────────────────────


def main():
    clear_screen()
    boot()
    while True:
        try:
            raw = input(prompt()).strip()
        except (KeyboardInterrupt, EOFError):
            print()
            typewrite(
                c(C.YELLOW, "  Tschüss! Und denk dran: Es ist immer ein PEBKAC. 👋"),
                delay=0.018,
            )
            print()
            break

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd in ("exit", "quit", "q", "x", "bye"):
            typewrite(c(C.YELLOW, "  Bis zum nächsten Bug! 👋"), delay=0.018)
            print()
            break
        elif cmd in COMMANDS:
            COMMANDS[cmd](args)
        else:
            # Kleines Easter Egg für unbekannte Befehle
            responses = [
                f"  {c(C.RED, 'command not found:')} {cmd}  {c(C.GRAY, '(auch im Ticket-System unbekannt)')}",
                f"  {c(C.RED, 'Fehler:')} '{cmd}' wurde in keiner Doku gefunden {c(C.GRAY, '(welche Doku?)')}",
                f"  {c(C.YELLOW, '🤔')} Meintest du 'help'? Oder schreibst du gerade ein neues Feature?",
            ]
            print(random.choice(responses))
            print()


if __name__ == "__main__":
    main()
