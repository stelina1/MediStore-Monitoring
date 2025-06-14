#Bibliotheken für LCD, GPIO, Zeit und Sensoren
import lcddriver
import RPi.GPIO as GPIO
import board
import time
from adafruit_bme280 import basic as adafruit_bme280 

#Vorherige GPIO-Einstellungen aufräumen
GPIO.cleanup()

#BME280 initialisieren
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x77)

#Display initialisieren und löschen
lcd = lcddriver.lcd()
lcd.lcd_clear()

#GPIO Pins konfigurieren (BCM-Nummerierung)
GPIO.setmode(GPIO.BCM)

#Bewegungssensor (PIR) Setup an GPIO 4 (Board: 7)
Pin = 4 
GPIO.setup(Pin, GPIO.IN)

#Reed-Schalter (Türsensor) Setup an GPIO 12
reed_switch_pin = 12
GPIO.setup(reed_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#LED Setup (3.3V Pin 17 und GND Pin 39)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

#Zwischenvariablen für Bewegungssensor
movement = 0
active = 0

try: 
    while True:
        
        #Reed-Schalter (Magnet) prüfen und LED steuern 
        reed_state = GPIO.input(reed_switch_pin)
        reed_state = not (reed_state)
        
        print(reed_state)
        
        if reed_state == True:  # Magnet erkannt, tür zu
            print("Magnet erkannt-Tür ist zu, LED aus")
            GPIO.output(led_pin, GPIO.LOW)  #LED ausschalten
            lcd.lcd_clear()
            lcd.lcd_display_string("Die Tür ist zu.", 1)
            time.sleep(1)
        else:
            print("kein Magnet erkannt-Tür ist offen, LED an")
            GPIO.output(led_pin, GPIO.HIGH)  #LED einschalten
            lcd.lcd_clear()
            lcd.lcd_display_string("Die Tür ist auf.",1)
            time.sleep(1)
        
        
        #Bewegungssensor auslesen
        movement = GPIO.input(Pin)
        
        #wenn Bewegung erkannt wird
        if movement == 1 and active == 0:
            print("Bewegung im Raum erkannt")
            lcd.lcd_clear()
            lcd.lcd_display_string("Bwegung erkannt!",1)
            active = 1
            time.sleep(1)
        
        #wenn keine Bewegung mehr erkannt wird
        elif movement == 0:
            print("Keine Bewegung erkannt")
            lcd.lcd_clear()
            lcd.lcd_display_string("Keine Bewegung!",1)
            active = 0
            time.sleep(1)

            
        #Temperatur, Luftfeuchtigkeit und Druck messen
        temperatur = bme280.temperature
        feuchtigkeit = bme280.relative_humidity
        druck = bme280.pressure
            
        #Temperatur anzeigen
        print(f"Temperatur: {temperatur:.1f} °C")
        lcd.lcd_clear()
        lcd.lcd_display_string("Temperatur:",1)
        lcd.lcd_display_string(f"{temperatur:.1f} °C",2)
        time.sleep(1)

        #Luftfeuchtigkeit anzeigen
        print(f"Feuchtigkeit: {feuchtigkeit:.1f} %")
        lcd.lcd_clear()
        lcd.lcd_display_string("Feuchtigkeit:",1)
        lcd.lcd_display_string(f"{feuchtigkeit:.1f} %",2)                                           
        time.sleep(1)
            
        #Luftdruck anzeigen
        print(f"Druck: {druck:.1f} hPa")
        lcd.lcd_clear()
        lcd.lcd_display_string("Druck:",1)
        lcd.lcd_display_string(f"{druck:.1f} hPa",2)
        time.sleep(1)
            
#Abbruchbdingung
except KeyboardInterrupt:
    print("Programm beendet.")
    lcd.lcd_clear()
    lcd.lcd_display_string("Programm beendet!.",1)
    lcd.lcd_display_string(f"   Danke! :)   ",2)
    #die GPIO-Einstellungen aufräumen
    GPIO.cleanup()
