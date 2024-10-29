import http.client
import json
import csv
import requests

# Define the URL and endpoint
url = "https://www.nseindia.com"
endpoint = "/api/live-analysis-oi-spurts-underlyings"
complete_url = url + endpoint


def fetch_data():
    s = requests.Session()
    headers = {
        'Host': 'www.nseindia.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
        'like Gecko) '
        'Chrome/80.0.3987.149 Safari/537.36',
        'accept-language': 'en,gu;q=0.9,hi;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept': '*/*'
    }
    # Perform an initial request to the base URL to set cookies
    # This request is to pick up necessary cookies
    r = s.get(url, timeout=10, headers=headers)
    cookies = dict(r.cookies)
    print('Cookies fetched successfully')

    # Now perform the request to the complete URL
    response = s.get(
        complete_url,
        timeout=10,
        headers=headers,
        cookies=cookies
    )
    # Print the status code of the response
    print('Got response')
    print('Response status code: ', response.status_code)
    response_json = response.json()
    print('response_json: ', response_json)

    return response_json


def save_to_csv(data, filename='underlyings.csv'):
    timestamp = data['timestamp']
    # Extract the list of data
    data_list = data['data']

    # Open a CSV file for appending, create if not exists
    with open(filename, mode='a+', newline='') as file:
        file.seek(0, 2)  # Move the cursor to the end of the file
        if file.tell() == 0:  # Check if the file is empty
            writer = csv.writer(file)
            header = ['timestamp'] + list(data_list[0].keys())
            writer.writerow(header)
        else:
            file.seek(0)  # Move the cursor to the start of the file
            last_line = list(csv.reader(file))[-1]
            last_timestamp = last_line[0]

            if timestamp == last_timestamp:
                print(f"Skipping data write: timestamp {
                      timestamp} is the same as the last recorded timestamp.")
                return  # Skip writing if the timestamp is the same

        # If the timestamp is different, write the data
        file.seek(0, 2)  # Move the cursor back to the end of the file
        writer = csv.writer(file)
        for item in data_list:
            row = [timestamp] + list(item.values())
            writer.writerow(row)


def main():
    try:
        print('Fetching data from NSE')
        # Fetch data from the API
        data = fetch_data()
        print('Fetched data from NSE')

        print('Saving data to CSV')
        # Save the data to a CSV file
        save_to_csv(data)

        print("Data saved to underlyings.csv")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
