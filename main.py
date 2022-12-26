import time
import requests

class BusArrivalAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://datamall2.mytransport.sg/ltaodataservice/"

    def get_bus_arrival(self, bus_stop_code, bus_number):
        headers = {
            "AccountKey": self.api_key,
            "accept": "application/json"
        }
        url = f"{self.base_url}BusArrivalv2?BusStopCode={bus_stop_code}&ServiceNo={bus_number}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Request failed with status code {response.status_code}")

    def notify_on_arrival(self, bus_stop_code, bus_number, arrival_time):
        while True:
            arrival_data = self.get_bus_arrival(bus_stop_code, bus_number)
            bus_arrival = arrival_data["Services"][0]["NextBus"]["EstimatedArrival"]
            if bus_arrival == arrival_time:
                print("Your bus is about to arrive!")
                break
            time.sleep(10)

# Create an instance of the BusArrivalAPI class
api = BusArrivalAPI("your_api_key_here")

# Set the desired bus stop code and bus number
bus_stop_code = "12345"
bus_number = "123"

# Set the desired arrival time (in the format "YYYY-MM-DDTHH:MM:SS+08:00")
arrival_time = "2022-12-22T12:00:00+08:00"

# Start the notification loop
api.notify_on_arrival(bus_stop_code, bus_number, arrival_time)
