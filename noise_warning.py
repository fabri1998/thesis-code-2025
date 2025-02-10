#!/usr/bin/python
import random
import time
import json
import paho.mqtt.client as mqtt

# Inställningar för MQTT
MQTT_BROKER = "lynx.iotopen.se"  
MQTT_PORT = 8883  
MQTT_TOPIC_WARNING = "1703/obj/generated/simulate/noise/warning"  

# Autentiseringsuppgifter
MQTT_USER = "random"  
MQTT_PASSWORD = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  

# Noise threshold for warnings
NOISE_THRESHOLD = 80  # dB

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
        
        # Bestäm om bullernivån är för hög (state_warning = 1, annars 0)
        warning_status = 1 if noise_level > NOISE_THRESHOLD else 0

        # Skapa ett JSON-meddelande för varningar
        payload = json.dumps({"value": warning_status})

        # Skicka varningen till MQTT-topic
        client.publish(MQTT_TOPIC_WARNING, payload)
        print(f"Skickade varningsstatus: {warning_status} (Bullernivå: {noise_level} dB)")

        # Vänta 20 sekunder innan nästa mätning
        time.sleep(20)

except KeyboardInterrupt:
    print("Avslutar simulering...")
finally:
    client.disconnect()
