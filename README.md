# MediStore-Monitoring
Überwachungssystem für medizinischen Lagerraum, ein Raspberry Pi Projekt.

# Projektbeschreibung
Die kontinuierliche Überwachung von Lagerbedingungen ist im medizinischen Bereich von entscheidend, um die Qualität und Wirksamkeit von Medikamenten, Impfstoffen oder anderen Produkten sicherzustellen. Bereits minimale Abweichungen bei Temperatur und Luftfeuchtigkeit oder Lagerung können erhebliche Auswirkungen auf die Sicherheit und Wirksamkeit dieser Produkte haben.
Dieses System erfasst kontinuierlich die Lagerbedingungen, gibt die Messwerte visuell aus und signalisiert den Türstatus zusätzlich durch eine LED-Anzeige. Ziel dieses Projekts ist die Entwicklung eines kostengünstigen und zuverlässigen Überwachungssystems, das mithilfe verschiedener Sensoren wichtige Parameter wie Temperatur, Luftfeuchtigkeit, Druck, Türstatus und Bewegung erfasst und übersichtlich auf einem Display darstellt. So können Abweichungen frühzeitig erkannt und bei Bedarf entsprechende Maßnahmen ergriffen werden. 
Mit diesem System wird die sichere Lagerung medizinischer Produkte gewährleistet und das Risiko von Qualitätsverlusten deutlich reduziert.

# Umsetzung und Funktion 
Die Umsetzung dieses Projekts beginnt mit dem Aufbau der Hardware und der anschließenden Softwareentwicklung. Zur Verbindung der Sensoren mit dem Raspberry Pi 4 wird ein T-Cobbler zusammen mit einem Verlängerungskabel verwendet, um die GPIO-Pins auf ein Breadboard zu übertragen und den Aufbau übersichtlicher zu gestalten.
Die einzelnen Sensoren und Bauteile werden am Breadboard angeschlossen. Der BME280-Sensor misst kontinuierlich die Temperatur, die Luftfeuchtigkeit und den Luftdruck im Raum. Zusätzlich erfasst der Bewegungssensor (PIR HC-SR501) Bewegungen innerhalb des Raumes und erkennt, ob sich Personen darin aufhalten. Der Reed-Switch dient der Überwachung des Türstatus. Er erkennt anhand des Magnetkontakts, ob die Tür geöffnet oder geschlossen ist. Die LED zeigt den Türstatus optisch an: bei geöffneter Tür leuchtet die LED, bei geschlossener Tür bleibt sie aus.
Die erfassten Messwerte wie Temperatur, Luftfeuchtigkeit, Luftdruck und Türstatur werden fortlaufend auf einem 16x2 LCD-Display mit I²C-Schnittstelle angezeigt. Bei erkannten Bewegungen erscheint die Meldung „Bewegung erkannt“ und bei nicht erkannten Bewegungen erscheint die Meldung „Keine Bewegung erkannt“. So erhält der Benutzer jederzeit einen Überblick über die aktuellen Lagerbedingungen und den Status des medizinischen Lagerraums.

# Funktionen
- Temperatur-, Luftfeuchtigkeits- und Luftdruckmessung (BME280 Sensor)
- Bewegungserkennung (PIR HC-SR501)
- Türüberwachung per Reed-Switch (Magnetschalter)
- Statusanzeige auf einem LCD Display (16x2 via I2C)
- LED-Warnleuchte bei offener Tür

# Verwendete Hardware
- Raspberry Pi 4
- T-Cobbler GPIO Breakout
- BME280 Sensor (I2C)
- PIR Bewegungssensor HC-SR501
- Reed-Switch + Magnet
- LCD Display 16x2 mit I2C Interface
- LED
- Breadboard und Jumper-Kabel

# Verwendete Bibliotheken
- lcddriver (für LCD-Steuerung)
- RPi.GPIO
- board
- adafruit-circuitpython-bme280
- time

# Installation
1. Python (falls noch nicht installiert):  
   [https://www.python.org](https://www.python.org)
2. Anleitung zur Installation des LCD-Treibers (hd44780_i2c):  
   [Tutorial Raspberry Pi LCD](http://tutorials-raspberrypi.de/wp-content/uploads/scripts/hd44780_i2c)
3. BME280 Sensor Python-Treiber:  
   [Raspberry Pi BME280 Github](https://github.com/andreiva/raspberry-pi-bme280)

# Bauteile
Bauteile des Projekts: https://github.com/stelina1/MediStore-Monitoring/blob/main/Bauteile.jpg

# Projektbild
Bilder des Projekts: https://github.com/stelina1/MediStore-Monitoring/blob/main/Projektbild.jpg

# Schaltplan
Schaltplan des Projekts:

# Fehlerbehebung
- Sensor wird nicht erkannt: Prüfe, ob I2C auf deinem Raspberry Pi aktiviert ist.
- LCD zeigt nichts an: Überprüfe die Verkabelung und die I2C-Adresse des Displays.
- LED leuchtet dauerhaft: Kontrolliere den Reed-Switch und die Türposition.

# Kontakt
Bei Fragen oder Feedback:
- Auf GitHub: stelina1 (https://github.com/stelina1)
- E-Mail: stelinauni@icloud.com

