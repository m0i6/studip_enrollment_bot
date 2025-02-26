## 1. Benötigte Pakete installieren

```sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## 2. Datei `.env` erstellen, Login Daten im KLARTEXT eintragen

```env
FLENS_USERNAME=user
FLENS_PASSWORD=pass
```

## 3. Links und Namen der gewünschten Kursen in course_data.json eintragen

#### Anleitung zum Ausfüllen der `course_data.json`

Die JSON-Datei enthält eine Liste von Kursen. Jeder Kurs sollte als Objekt hinzugefügt werden. Du kannst beliebig viele Kurse hinzufügen, indem du das Objekt für jeden Kurs duplizierst und die entsprechenden Parameter anpasst.

Die Parameter, die du für jeden Kurs ausfüllen musst, sind:
- **`name`**: Der Name des Kurses (dient nur der Bezeichnung)
- **`url_v`**: Die URL zum Einschreiben in die Vorlesung (Stud.IP-Seite des Kurses)
- **`url_l`**: Die URL zum Labor, wenn das Labor eine eigene Seite hat oder die URL zur Gruppenseite, falls die Einschreibung über Gruppen erfolgt
- **`enrollment_in_groups`**: Ein Boolean-Wert (`true` oder `false`), der angibt, ob das Labor über Gruppen eingeschrieben wird
- **`group_number`**: Die Nummer der Gruppe, in die du dich eintragen möchtest startend bei 1 (nur relevant, wenn `enrollment_in_groups` auf `true` gesetzt ist; andernfalls kann der Wert auf `0` gesetzt werden)

Wenn du ein neues Kursobjekt hinzufügst, sollte es wie folgt aussehen:

```json
{
    "name": "Software Engineering",
    "url_v": "",
    "url_l": "",
    "enrollment_in_groups": false,
    "group_number": 0
}
```

## 4. Skript starten

```sh
python main.py
```

## 5. Ans HPI wechseln

## Anmerkung

Bei der Laborwahl über Gruppen sind Fehler möglich, wenn eine Gruppe schon voll ist bevor das Skript sich einschreiben kann. In diesem Fall findet die Einschreibung automatisch in das nächste freie Labor (wenn vorhanden), deshalb sollte der Erfolg der Laborwahl über Gruppen nach dem Ablaufen des Skriptes überprüft werden.
