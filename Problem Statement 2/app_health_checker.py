import requests
import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Setup logging to store logs in the logs directory
logging.basicConfig(filename='logs/app_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define application URL and expected HTTP status code
APP_URL = 'https://www.google.com/'  # Replace with your app's URL
EXPECTED_STATUS = 200

def check_application_health():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == EXPECTED_STATUS:
            logging.info(f"Application is UP. Status code: {response.status_code}")
            print("Application is UP.")
        else:
            logging.warning(f"Application is DOWN. Status code: {response.status_code}")
            print("Application is DOWN.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error reaching the application: {e}")
        print("Application is DOWN.")

if __name__ == '__main__':
    check_application_health()
