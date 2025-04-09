#!/usr/bin/python
import random
import time
import json
import paho.mqtt.client as mqtt

# Inställningar för MQTT
MQTT_BROKER = "lynx.iotopen.se"  
MQTT_PORT = 8883  
MQTT_TOPIC = "1703/obj/generated/simulate/presence" 

# Autentiseringsuppgifter
MQTT_USER = "random"  
MQTT_PASSWORD = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 

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

def simulate_presence():
    """Genererar en slumpmässig närvarostatus: 1 = närvaro, 0 = ingen närvaro."""
    return random.choice([0, 1])

try:
    while True:
        # Simulera närvarovärde
        presence_status = simulate_presence()

        # Skapa ett JSON-meddelande
        payload = json.dumps({"value": presence_status})

        # Skicka meddelandet till MQTT-topic
        client.publish(MQTT_TOPIC, payload)
        status_message = "Närvaro upptäckt" if presence_status == 1 else "Ingen närvaro"
        print(f"Skickade närvarostatus: {presence_status} ({status_message})")

        # Vänta 30 sekunder innan nästa mätning
        time.sleep(30)

except KeyboardInterrupt:
    print("Avslutar simulering...")
finally:
    client.disconnect()
