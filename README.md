# Water-Link Home Assistant custom integration

I was running a bash script to fetch my 'Water Link' digital water meter readings, and decided to leverage ChatGPT to convert it into a custom integration. 
As Water Link does not expose a proper API, the integration authenticates on ['My Water-Link' customer portal](https://portaaldigitalemeters.water-link.be/), and retrieves the data from there. Note that this may not be very robust, as Water Link has changed their authentication procedures already a few times. Use this integration at your own discretion.
Water Link is only available in Belgium, so no point in using this integration if you are not a current customer.

# Available Data
![image](https://github.com/user-attachments/assets/02f5c7e7-fa33-4fd5-8f06-baad1bc149ec)

# Installation

Copy waterlink_meter folder to your configuration/custom_components path and restart Home Assistant. Use the add integration UI to set up your device.

![image](https://github.com/user-attachments/assets/025b78f2-60b3-4431-8ca5-5c1f484ae6e4)

|Configuration | Description  |
|--|--|
| Username | The username that you use to login into My Water Link portal |
| Password| The password that you use to login into My Water Link portal  |
| Client ID| I'm not even sure if this needs to be configurable. If the present client ID does not work for you, you may have to inspect your own network traffic to My Water Link |
| Meter ID| your 6-digit meter identification number (eg. 123456) You can find this ID in your specific portal URL, eg. https://portaaldigitalemeters.water-link.be/water-meter/XXXXXX|

# Configuration
![image](https://github.com/user-attachments/assets/fc7ea38c-a0f1-4078-a95b-51a523d71dba)

|Option| Description  |
|--|--|
| update_interval | The interval to fetch the reading from the Portal. Default is set two 2700s (2 hours). Note that the digital water meter only sends updates once day.  |
