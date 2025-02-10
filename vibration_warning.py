#!/usr/bin/python
import random
import time
import json
import paho.mqtt.client as mqtt

# Inställningar för MQTT
MQTT_BROKER = "lynx.iotopen.se"  
MQTT_PORT = 8883  
MQTT_TOPIC_WARNING = "1703/obj/generated/simulate/vibration/warning"  

# Autentiseringsuppgifter
MQTT_USER = "random"  
MQTT_PASSWORD = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 

# Vibration threshold for warnings
VIBRATION_THRESHOLD = 50  # Hz

# Skapa MQTT-klient och anslutningsinställningar
client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

# Aktivera TLS/SSL
client.tls_set()  

# Anslut till MQTT-brokern
try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"Kunde inte ansluta till MQTT-brokern: {e}")

def simulate_vibration():
    """Genererar ett slumpmässigt vibrationsvärde mellan 0 och 100 Hz."""
    return round(random.uniform(0, 100), 2)

try:
    while True:
        # Simulera vibrationsvärde
        vibration = simulate_vibration()
        
        # Bestäm om vibration är för hög (state_warning = 1, annars 0)
        warning_status = 1 if vibration > VIBRATION_THRESHOLD else 0

        # Skapa ett JSON-meddelande för varningar
        payload = json.dumps({"value": warning_status})

        # Skicka varningen till MQTT-topic
        client.publish(MQTT_TOPIC_WARNING, payload)
        print(f"Skickade varningsstatus: {warning_status} (Vibration: {vibration} Hz)")

        # Vänta 20 sekunder innan nästa mätning
        time.sleep(20)

except KeyboardInterrupt:
    print("Avslutar simulering...")
finally:
    client.disconnect()
