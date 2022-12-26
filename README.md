# SG Bus Arrival API
This script makes requests to the LTA DataMall API (http://datamall2.mytransport.sg/) to get the estimated arrival times for buses at a specific bus stop.

You will need to sign up for an API key and replace "YOUR_API_KEY" in the code with your own API key. The script calculates the time until each bus is expected to arrive and sends a notification if the time is less than the specified number of minutes (in this case, 10 minutes).

You can modify the script to use your own location and bus stop code, and to customize the notification method (e.g. by using a third-party library to send an email or text message). You can also adjust the frequency of updates and the number of minutes before arrival to send a notification.

# Change logs
## 2022-12-26
### BusArrivalAPI.py
This refactored version of the notify_on_arrival method takes an additional argument: the notification threshold (in minutes). It calculates the time until the bus is expected to arrive by subtracting the current time from the estimated arrival time and converting the result to minutes. If the time until arrival is less than or equal to the notification threshold, a notification is printed to the console.

# How do I integrate this script with Google nest hub
To integrate the script with Google Nest Hub, you will need to use the Google Assistant API to create a "smart home" action. A smart home action allows you to control and interact with your home's devices and services using voice commands through Google Assistant.

Here is an outline of the steps you can follow to create a smart home action for bus arrival notifications:
1. Set up a Google Cloud account and create a new project.
2. Enable the Google Assistant API for your project by going to the "APIs & Services" dashboard and searching for "Google Assistant API." Click on the API and then click the "Enable" button.
3. Create a new OAuth 2.0 client ID by going to the "Credentials" dashboard and clicking the "Create credentials" button. Select "OAuth client ID" from the dropdown menu and choose "Other" as the application type.
4. Use the Google Cloud Shell to clone the sample code for the Google Assistant API by running the following command:
git clone https://github.com/googleapis/google-assistant-api-samples
5. Navigate to the cloned repository and go to the google-assistant-api-samples/python/assistant/library directory.
6. Install the required libraries by running the following command:
pip install -r requirements.txt
7. Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to the JSON file containing your Google Cloud API key by running the following command:
export GOOGLE_APPLICATION_CREDENTIALS=path/to/key.json
8. Use the google-auth library to obtain an access token by running the following command:
python -m google.oauth2.credentials_flow
9. Use the google-api-python-client library to call the SG Bus Arrival API and integrate the data with the Google Assistant API. You can find more information about using the google-api-python-client library in the documentation https://developers.google.com/api-client-library/python/

# Integrate with Google Assistant API
1. Create a smart home action using the Google Assistant API. This will involve defining the name and functionality of your action, as well as creating a fulfillment server to handle the requests and responses.
2. Modify the script to work with the smart home action. This will involve adapting the code to use the Google Assistant API's request and response format, and creating functions to handle the different types of requests that your action will receive (e.g. "query" requests to get the current bus arrival times, and "execute" requests to set the notification parameters).
3. Deploy your fulfillment server and test your action using the Google Assistant Simulator or a device with Google Assistant (such as a Nest Hub).
4. Publish your action to make it available to users through Google Assistant.
For more detailed instructions and code examples, you can refer to the Google Assistant documentation on creating smart home actions: https://developers.google.com/assistant/smarthome/develop/
