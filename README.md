# 🛰️ Ground Station

DIY automatic satellite tracking ground station — Sommer-Projekt 2026.

Eine drehbare Antenne, die Satelliten am Himmel verfolgt, ihre Funksignale einfängt und in nutzbare Daten (z.B. NOAA-Wetterbilder) verwandelt.

## 🎯 Ziel

**MVP (Minimum Viable Ground Station):**
Erstes NOAA-Wetterbild empfangen — fixe Position, manuell ausgerichtete Antenne, SDR + Pi.

**Danach:**
Automatisches Tracking (Stepper-Mount + Closed Loop), dann optional mobil, Kamera-Feedback, HAM-TX.

## 👥 Team


| Name    | Rolle                          | Owns                                                           |
| ------- | ------------------------------ | -------------------------------------------------------------- |
| Yesunkh | RF & Software Lead             | SDR, Empfang, Signal-Decoding, Tracking-SW auf Pi              |
| David   | Mechanics & Motion Lead        | NEMA17-Steuerung (A4988), Mount-Bau, Pointing-Logik            |
| Joel    | Space & Data Lead, Fabrication | TLE-Daten, Pass-Vorhersage, Pointing-Math, 3D-Druck (Ender V3) |


Alle TU Berlin, Bachelor 8. Semester.

## 📍 Standorte

- **Bauen & Empfang:** Joels Garage (flaches Dach, Strom, Werkzeug)
- Alternativ **Meetings / Coding:** bei Yesunkh (näher an Uni)

## 🏗️ Architektur

```
Satellit → Antenne → SDR → Pi (Decoding + Tracking-Math)
                              ↓
                          D1 mini pro (WiFi) oder Arduino Mega, je nachdem mal schauen
                              ↓
                          A4988 Driver
                              ↓
                          NEMA17 (Az + El)
                              ↓
                       Antenne dreht mit
```

## 📁 Repo-Struktur

- `/firmware` — Code für D1 mini pro / Arduino
- `/pi` — Code fürs Raspberry Pi (SDR, Tracking)
- `/hardware` — Schaltpläne, Mount-Skizzen, STL-Files für 3D-Druck
- `/docs` — Architektur, Diagramme, Anleitungen
- `/log` — Bau-Logbuch (eine `.md`-Datei pro Session)
- `/media` — Fotos, Videos, Empfangsergebnisse (nur Highlights; große Files via Discord/Drive)
- `[INVENTORY.md](./INVENTORY.md)` — Hardware-Inventar

## 🔧 Workflow

- `main` ist immer "funktioniert"
- Feature-Branches pro Person, selbst mergen wenn's läuft
- Bei Unsicherheit → Pull Request öffnen
- Commit-Nachrichten als Mini-Logbuch (`"add stepper test"`, `"first NOAA reception"`)

## 📅 Status

Abgeschlossen: Kickoff: **Sonntag 17.05.2026!**

**next: ..tbd ;P**

## 📜 Lizenz

*tbd*