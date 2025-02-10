#!/usr/bin/python
import random
import time
import json
import paho.mqtt.client as mqtt

# Inställningar för MQTT
MQTT_BROKER = "lynx.iotopen.se"  
MQTT_PORT = 8883  
MQTT_TOPIC = "1703/obj/generated/simulate/noise"  

# Autentiseringsuppgifter
MQTT_USER = "random"  
MQTT_PASSWORD = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  

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

def simulate_noise():
    """Genererar ett slumpmässigt bullervärde mellan 30 och 120 dB."""
    return round(random.uniform(30, 120), 2)

try:
    while True:
        # Simulera bullernivå
        noise_level = simulate_noise()
        # Skapa ett JSON-meddelande
        payload = json.dumps({"value": noise_level})
        # Skicka meddelandet till MQTT-topic
        client.publish(MQTT_TOPIC, payload)
        print(f"Skickade bullernivå: {noise_level} dB")
        
        # Vänta 10 sekunder innan nästa mätning
        time.sleep(10)

except KeyboardInterrupt:
    print("Avslutar simulering...")
finally:
    client.disconnect()
