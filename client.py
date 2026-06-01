import requests
import json
import random

# Generate 5 random weather temperatures (in Celsius)
def generate_weather_temperatures():
    return [round(random.uniform(-5, 40), 1) for _ in range(5)]

def send_to_server(temperatures):
    server_url = "http://localhost:5000/calculate"
    
    # Create JSON message
    message = {
        'temperatures': temperatures,
        'timestamp': '2025-12-01T10:00:00'
    }
    
    print(f" Sending: {json.dumps(message, indent=2)}")
    
    # Send to server
    response = requests.post(server_url, json=message)
    
    if response.status_code == 200:
        result = response.json()
        print(f" Received: {json.dumps(result, indent=2)}")
        return result
    else:
        print(f"❌ Error: {response.status_code}")
        return None

if __name__ == '__main__':
    temperatures = generate_weather_temperatures()
    print(f"Weather Temperatures: {temperatures}")
    result = send_to_server(temperatures)
    
    if result:
        print(f"\nStatistics:")
        print(f"   Average: {result['average']}°C")
        print(f"   Minimum: {result['minimum']}°C")
        print(f"   Maximum: {result['maximum']}°C")