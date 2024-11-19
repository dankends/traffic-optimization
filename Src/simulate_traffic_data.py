import time
import json
import random
from datetime import datetime
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# AWS IoT Core credentials and configuration
client = AWSIoTMQTTClient("TrafficLightSimulator")
client.configureEndpoint("a18dlidfhpm5i7-ats.iot.ca-central-1.amazonaws.com", 8883)
client.configureCredentials("AmazonRootCA1.pem", "private.pem.key", "certificate.pem.crt")

# Connect to AWS IoT
client.connect()



# Helper functions to simulate realistic data
def get_vehicle_count():
    # Random vehicle count with some noise
    return int(random.gauss(50, 15))

def get_average_speed():
    # Speed decreases with high vehicle count
    base_speed = 60
    count_factor = max(0, (100 - get_vehicle_count()) / 100)
    return round(random.gauss(base_speed * count_factor, 5), 1)

def get_CO2_level(vehicle_count):
    # CO2 level increases with vehicle count
    base_CO2 = 0.04
    CO2_increase = 0.0002 * vehicle_count
    return round(base_CO2 + CO2_increase, 4)

def get_temperature():
    # Random temperature simulating a range (20-35°C)
    return round(random.uniform(20, 35), 1)

def get_humidity():
    # Random humidity simulating a range (40-80%)
    return round(random.uniform(40, 80), 1)

def get_congestion_level(vehicle_count):
    # Assign congestion level based on vehicle count
    if vehicle_count < 30:
        return "Low"
    elif 30 <= vehicle_count < 70:
        return "Medium"
    else:
        return "High"

# Function to generate data for a single traffic light
def generate_traffic_data():
    vehicle_count = get_vehicle_count()
    average_speed = get_average_speed()
    CO2_level = get_CO2_level(vehicle_count)
    temperature = get_temperature()
    humidity = get_humidity()
    congestion_level = get_congestion_level(vehicle_count)
    
    return {
        "traffic_light_id": f"TL-{random.randint(100, 200)}",
        "timestamp": int(time.time()),
        "vehicle_count": vehicle_count,
        "average_speed": average_speed,
        "CO2_level": CO2_level,
        "temperature": temperature,
        "humidity": humidity,
        "congestion_level": congestion_level
    }

# Publish data every 5 seconds
while True:
    data = generate_traffic_data()
    client.publish("TrafficData/TrafficLight", json.dumps(data), 1)
    print(f"Data sent at {datetime.now()}: {data}")
    time.sleep(1)
