# SG Bus Arrival API
This script makes requests to the LTA DataMall API (http://datamall2.mytransport.sg/) to get the estimated arrival times for buses at a specific bus stop.

You will need to sign up for an API key and replace "YOUR_API_KEY" in the code with your own API key. The script calculates the time until each bus is expected to arrive and sends a notification if the time is less than the specified number of minutes (in this case, 10 minutes).

You can modify the script to use your own location and bus stop code, and to customize the notification method (e.g. by using a third-party library to send an email or text message). You can also adjust the frequency of updates and the number of minutes before arrival to send a notification.

# How do I integrate this script with Google nest hub
To integrate the script with Google Nest Hub, you will need to use the Google Assistant API to create a "smart home" action. A smart home action allows you to control and interact with your home's devices and services using voice commands through Google Assistant.

Here is an outline of the steps you can follow to create a smart home action for bus arrival notifications:

Set up a Google Cloud project and enable the Google Assistant API.
1. Create a smart home action using the Google Assistant API. This will involve defining the name and functionality of your action, as well as creating a fulfillment server to handle the requests and responses.
2. Modify the script to work with the smart home action. This will involve adapting the code to use the Google Assistant API's request and response format, and creating functions to handle the different types of requests that your action will receive (e.g. "query" requests to get the current bus arrival times, and "execute" requests to set the notification parameters).
3. Deploy your fulfillment server and test your action using the Google Assistant Simulator or a device with Google Assistant (such as a Nest Hub).
4. Publish your action to make it available to users through Google Assistant.
For more detailed instructions and code examples, you can refer to the Google Assistant documentation on creating smart home actions: https://developers.google.com/assistant/smarthome/develop/
