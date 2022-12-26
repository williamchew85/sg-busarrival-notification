import datetime

class BusArrivalData:
    def __init__(self, bus_stop_code, bus_number):
        self.bus_stop_code = bus_stop_code
        self.bus_number = bus_number

    def get_data(self):
        # Retrieve the bus arrival data from the API here
        # Set up the API request URL
        base_url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"
        api_key = "your_api_key"
        params = {
            "BusStopCode": self.bus_stop_code,
            "ServiceNo": self.bus_number,
            "AccountKey": api_key
        }

        # Send the request to the API
        response = requests.get(base_url, params=params)

        # Process the API response
        data = response.json()
        arrival_times = []
        for bus in data:
            expected_arrival_time = bus["ExpectedArrival"]
            arrival_time = datetime.datetime.strptime(expected_arrival_time, "%Y-%m-%dT%H:%M:%S+08:00")
            arrival_times.append(arrival_time)
        return arrival_times

if __name__ == "__main__":
    bus_stop_code = sys.argv[1]
    bus_number = sys.argv[2]
    arrival_data = BusArrivalData(bus_stop_code, bus_number)
    arrival_times = arrival_data.get_data()

    for arrival_time in arrival_times:
        time_until_arrival = arrival_time - datetime.datetime.now()
        if time_until_arrival.total_seconds() / 60 < 10:
            # Send notification here
            print(f"Bus arriving in {time_until_arrival} minutes")
