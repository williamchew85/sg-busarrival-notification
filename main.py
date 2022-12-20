import requests
import time

# Set your location and bus stop code
latitude = 1.3521
longitude = 103.8198
bus_stop_code = '04111'

# Set the number of minutes before arrival to send notification
notification_minutes = 10

while True:
    # Make a request to the bus arrival API
    api_url = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2'
    headers = {'AccountKey': 'YOUR_API_KEY', 'accept': 'application/json'}
    params = {'BusStopCode': bus_stop_code}
    response = requests.get(api_url, headers=headers, params=params)
    data = response.json()

    # Loop through the arrival times for each bus
    for bus in data['Services']:
        for arrival in bus['NextBus']['EstimatedArrival']:
            # Calculate the time until arrival in minutes
            arrival_time = arrival['EstimatedArrival']
            arrival_minutes = (arrival_time - time.time()) / 60
            if arrival_minutes <= notification_minutes:
                # Send the notification
                message = f'{bus["ServiceNo"]} is arriving at {bus_stop_code} in {arrival_minutes:.0f} minutes'
                send_notification(message)
    
    # Wait for the next update
    time.sleep(60)

def send_notification(message):
    # Replace this with code to send the notification using your preferred method
    print(message)
