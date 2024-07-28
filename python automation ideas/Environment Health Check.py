import requests

def check_service_health(service_url):
    response = requests.get(service_url)
    if response.status_code == 200:
        print(f"Service is healthy: {service_url}")
    else:
        print(f"Service is unhealthy: {service_url}, status code: {response.status_code}")

if __name__ == "__main__":
    services = [
        "http://my-service1.example.com/health",
        "http://my-service2.example.com/health"
    ]
    for service in services:
        check_service_health(service)
