# Unofficial 'Mijn Water-Link' Home Assistant Custom Integration

![image](https://github.com/user-attachments/assets/69820796-f96d-44e2-b0c4-0dbd94a06e34)

I was running a bash script to fetch my 'Water-Link' digital water meter readings, and decided to leverage ChatGPT to convert it into a custom integration. It did a decent job, although i'm sure there could be many improvements (both to the original bash scripts, as to the genereated custom integration). Feel free to contribute.
As Water Link does not expose a proper API, the integration authenticates on ['My Water-Link' customer portal](https://portaaldigitalemeters.water-link.be/), and retrieves the data from there. Note that this may not be very robust, as Water-Link has changed their authentication procedures already a few times. Use this integration at your own discretion.
Water-Link is only available in Belgium, so no point in using this integration if you are not an existing customer.

# Available Data
![image](https://github.com/user-attachments/assets/02f5c7e7-fa33-4fd5-8f06-baad1bc149ec)

# Installation
Currently this integration is not yet available over HACS, so you will have to manually add it to your Home Assistant instance.
Copy the `custom_components/mijn-waterlink` folder to your `configuration` path and restart Home Assistant. Use the add integration UI to set up your device.

![image](https://github.com/user-attachments/assets/025b78f2-60b3-4431-8ca5-5c1f484ae6e4)

|Configuration | Description  |
|--|--|
| Username | The username that you use to login into My Water-Link portal. Doublecheck that these credentials are CORRECT |
| Password| The password that you use to login into My Water-Link portal. Doublecheck that these credentials are CORRECT  |
| Client ID| I'm not even sure if this needs to be configurable. If the present client ID does not work for you, you may have to inspect your own network traffic to My Water-Link |
| Meter ID| your 6-digit meter identification number (eg. 123456) You can find this ID in your specific portal URL, eg. https://portaaldigitalemeters.water-link.be/water-meter/XXXXXX|

# Configuration
![image](https://github.com/user-attachments/assets/fc7ea38c-a0f1-4078-a95b-51a523d71dba)

|Option| Description  |
|--|--|
| update_interval | The interval to fetch the reading from the Portal. Default is set two 2700s (2 hours). Note that the digital water meter only sends an update once a day.  |
