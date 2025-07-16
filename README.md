# Unofficial 'Mijn Water-Link' Home Assistant Custom Integration

![image](https://github.com/user-attachments/assets/69820796-f96d-44e2-b0c4-0dbd94a06e34)


I was running a bash script to fetch my 'Water-Link' digital water meter readings, and decided to leverage ChatGPT to convert it into a custom integration. It did a decent job, although i'm sure there could be many improvements (both to the original bash scripts, as to the genereated custom integration). Feel free to contribute.
As Water Link does not expose a proper API, the integration authenticates on ['Mijn Water-link' customer portal](https://portaaldigitalemeters.water-link.be/), and retrieves the data from there. Note that this may not be very robust, as Water-Link has changed their authentication procedures already a few times. Use this integration at your own discretion.
Water-Link is only available in Antwerp, Belgium, so no point in installing this integration if you are not an existing customer.

## Available Data

This integration will fetch the latest received datapoint from the 'Mijn Water-link' portal. Typically the water meter sends a value every day, but it can happen that it takes a few days as well. This means that the last received datapoint is always a bit outdated, typically anywhere from a few hours to a couple of days.

![image](https://github.com/user-attachments/assets/02f5c7e7-fa33-4fd5-8f06-baad1bc149ec)

## Installation

### HACS

Mijn Water Link is available in [HACS](https://hacs.xyz/) (Home Assistant Community Store).

Use this link to directly go to the repository in HACS

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=zheffie&repository=mijn_waterlink)

_or_

1. Install HACS if you don't have it already
2. Open HACS in Home Assistant
3. Search for "Mijn Waterlink"
4. Click the download button. ⬇️


### Manual
Copy the `custom_components/mijn-waterlink` folder to your `configuration` path and restart Home Assistant. Use the add integration UI to set up your device.

## Configuration
|Configuration | Description  |
|--|--|
| Username | The username that you use to login into 'Mijn Water-link' |
| Password| The password that you use to login into 'Mijn Water-link'  |
| Client ID| I'm not even sure if this needs to be configurable. If the present client ID does not work for you, you may have to inspect your own network traffic to 'Mijn Water-link' |
| Meter ID| your 6-digit meter identification number (eg. 123456) You can find this ID in your specific portal URL, eg. https://portaaldigitalemeters.water-link.be/water-meter/XXXXXX|

## Options
|Option| Description  |
|--|--|
| update_interval | The interval to fetch the reading from the Portal. Default is set to 2700s (2 hours). Note that the digital water meter only sends an update once a day, but in some occasions it may take a few days before an update is received  |
