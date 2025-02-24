1. Virtuelle Umgebung erstellen (optional)
Falls du eine isolierte Umgebung nutzen möchtest:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

2.  Benötigte Pakete installieren

pip install selenium webdriver-manager

3. WebDriver installieren
Falls du Chrome nutzt, installiere den ChromeDriver automatisch mit:

python -m webdriver_manager.chrome

4. Login Daten im KLARTEXT in die settings.py eintragen
