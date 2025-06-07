# Water-Link Home Assistant custom integration

I was running a bash script to fetch my 'Water Link' digital water meter readings, and decided to leverage ChatGPT to convert it into a custom integration. 
As Water Link does not expose a proper API, the integration authenticates on the 'My Water-Link' portal, and retrieves the data from there. Note that this may not be very robust, as Water Link has changed their authentication procedures already a few times. Use this integration at your own risk.
Water Link is only available for certain Belgium customer's, so not point in using this integration if you are not covered by their services.

# Available Data
![image](https://github.com/user-attachments/assets/02f5c7e7-fa33-4fd5-8f06-baad1bc149ec)

# Installation

Copy waterlink_meter folder to your configuration/custom_components path and restart Home Assistant. Use the add integration UI to set up your device.

![image](https://github.com/user-attachments/assets/025b78f2-60b3-4431-8ca5-5c1f484ae6e4)

|Configuration | Description  |
|--|--|
| Username | The username that you use to login into My Wate Link  |
| Password| The password that you use to login into My Water Link  |
| Client ID| not sure if this needs to be configurable. If the present client ID does not work for you, you may have to inspect the traffic to My Water Link  |
| Meter ID| your 6-digit meter identification number (eg. 123456) You can find this ID in the URL eg https://portaaldigitalemeters.water-link.be/water-meter/XXXXXX|

# Configuration
![image](https://github.com/user-attachments/assets/fc7ea38c-a0f1-4078-a95b-51a523d71dba)

|Option| Description  |
|--|--|
| update_interval | The interval to update. Set two 2700s (2 hours). As my reading is only updated once a day, this should be sufficient |
