import requests
import json

# Test the API with a simple text
url = "http://127.0.0.1:5000/api/analyze"

data = {
    'text': 'This is a smart home thermostat that connects to WiFi and can be controlled remotely via a mobile app. It is sold in the EU market for $199.',
    'model': 'gemini-2.5-flash'
}

try:
    response = requests.post(url, data=data, timeout=60)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}...")
    
    if response.status_code == 200:
        result = response.json()
        print(f"\nSuccess: {result.get('success')}")
        if result.get('success'):
            analysis = result.get('result', {})
            print(f"Product: {analysis.get('product_name')}")
            print(f"In Scope: {analysis.get('classification', {}).get('in_scope')}")
            print(f"Confidence: {analysis.get('classification', {}).get('confidence_score')}")
        else:
            print(f"Error: {result.get('error')}")
    
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
