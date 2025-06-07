# Water-Link Home Assistant custom integration

I was running a bash script to fetch my 'Water Link' digital water meter readings, and decided to leverage ChatGPT to convert it into a custom integration. 
As Water Link does not expose a proper API, the integration authenticates on the 'My Water-Link' section of their website, and retrieves the data from there. Note that this may not be very robust, as Water Link has changed their authentication procedures already a few times. Use this integration at your own risk
Water Link is only available for certain Belgium customer's, so not point in using this integration if you are not covered by their services.

# Setup
|Configuration | Description  |
|--|--|
| username | The username that you use to login into My Wate Link  |
| password| The password that you use to login into My Water Link  |
| client_id| not sure if this needs to be configurable  |
| meter| your meter identification number as displayed in My Water Link|

# Configuration
|Option| Description  |
|--|--|
| update | The interval to update. Set two 2700s (2 hours). As my reading is only updated once a day, this should be sufficient |
