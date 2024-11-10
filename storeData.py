import csv
import requests
import time
from datetime import datetime

# Define the URL and endpoint
url = "https://www.nseindia.com"
endpoint = "/api/live-analysis-oi-spurts-underlyings"
complete_url = url + endpoint


class DataCollector:
    def __init__(self):
        self.is_running = False
        self.output_file = 'underlyings.csv'

    def set_output_file(self, filename):
        self.output_file = filename

    def fetch_data(self):
        # Existing fetch_data function content
        s = requests.Session()
        headers = {
            'Host': 'www.nseindia.com',
            'user-agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Safari/537.36'
            ),
            'accept-language': 'en,gu;q=0.9,hi;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept': '*/*'
        }
        r = s.get(url, timeout=10, headers=headers)
        cookies = dict(r.cookies)
        print('Cookies fetched successfully')

        response = s.get(
            complete_url,
            timeout=10,
            headers=headers,
            cookies=cookies
        )
        print('Got response')
        print('Response status code: ', response.status_code)
        return response.json()

    def save_to_csv(self, data):
        # Modified save_to_csv function to use instance variable
        timestamp = data['timestamp']
        data_list = data['data']

        with open(self.output_file, mode='a+', newline='') as file:
            file.seek(0, 2)
            if file.tell() == 0:
                writer = csv.writer(file)
                header = ['timestamp'] + list(data_list[0].keys())
                writer.writerow(header)
            else:
                file.seek(0)
                last_line = list(csv.reader(file))[-1]
                last_timestamp = last_line[0]

                if timestamp == last_timestamp:
                    print(f"Skipping data write: timestamp {
                          timestamp} is the same as the last recorded timestamp.")
                    return

            file.seek(0, 2)
            writer = csv.writer(file)
            for item in data_list:
                row = [timestamp] + list(item.values())
                writer.writerow(row)

    def start_collection(self, interval=90):
        self.is_running = True
        while self.is_running:
            try:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n[{current_time}] Fetching data from NSE")

                data = self.fetch_data()
                print('Fetched data from NSE')

                print('Saving data to CSV')
                self.save_to_csv(data)

                print(f"Data saved to {self.output_file}")
                print(f"Waiting {interval} seconds before next fetch...")
                time.sleep(interval)

            except Exception as e:
                print(f"An error occurred: {e}")
                print("Retrying in 60 seconds...")
                time.sleep(60)

    def stop_collection(self):
        print("Collection stopped")
        self.is_running = False
