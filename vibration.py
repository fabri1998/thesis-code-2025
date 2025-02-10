#!/usr/bin/python
import random
import time
import json
import paho.mqtt.client as mqtt

# Inställningar för MQTT
MQTT_BROKER = "lynx.iotopen.se"  
MQTT_PORT = 8883  
MQTT_TOPIC = "1703/obj/generated/simulate/vibration"

# Autentiseringsuppgifter
MQTT_USER = "random"  
MQTT_PASSWORD = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  

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
        # Skapa ett JSON-meddelande
        payload = json.dumps({"value": vibration})
        # Skicka meddelandet till MQTT-topic
        client.publish(MQTT_TOPIC, payload)
        print(f"Skickade vibrationsvärde: {vibration} Hz")
        
        # Vänta 10 sekunder innan nästa mätning
        time.sleep(10)

except KeyboardInterrupt:
    print("Avslutar simulering...")
finally:
    client.disconnect()
