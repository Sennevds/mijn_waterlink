import logging
from datetime import timedelta

from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

from .waterlink_api import WaterlinkClient
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    username = config_entry.data["username"]
    password = config_entry.data["password"]
    client_id = config_entry.data["client_id"]
    meter_id = config_entry.data["meter_id"]

    update_interval = config_entry.options.get(
        "update_interval",
        config_entry.data.get("update_interval", 7200)  # default: 2 hours
    )

    client = WaterlinkClient(username, password, client_id, meter_id)

    async def async_update_data():
        _LOGGER.debug("Fetching Waterlink meter data update...")
        try:
            await hass.async_add_executor_job(client.authenticate)
            data = await hass.async_add_executor_job(client.get_meter_data)
            if not isinstance(data, dict):
                raise UpdateFailed("Waterlink API did not return a dict")
            notifications = await hass.async_add_executor_job(client.get_notifications)
            if not isinstance(notifications, dict):
                raise UpdateFailed("Waterlink API did not return a dict")
            return (data, notifications)
        except Exception as err:
            raise UpdateFailed(f"Waterlink API error: {err}")

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"water-link meter {meter_id}",
        update_method=async_update_data,
        update_interval=timedelta(seconds=update_interval),
    )

    await coordinator.async_config_entry_first_refresh()

    entity = WaterlinkSensor(
        coordinator,
        name=f"water-link meter {meter_id}",
        unit="m³",
    )

    async_add_entities([entity])

class WaterlinkSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, name, unit):
        super().__init__(coordinator)
        self._attr_name = name
        self._attr_unique_id = f"{name.replace(' ', '_').lower()}"
        self._attr_native_unit_of_measurement = unit
        self._attr_device_class = SensorDeviceClass.WATER
        self._attr_state_class = SensorStateClass.TOTAL_INCREASING

    @property
    def native_value(self):
        reading = self.coordinator.data.get("meterReading")
        if reading:
            try:
                return float(reading.replace(",", "."))
            except ValueError:
                _LOGGER.warning("Invalid reading format: %s", reading)
        return None

    @property
    def extra_state_attributes(self):
        data = self.coordinator.data
        return {
            "is_active": data.get("isActive"),
            "latest_reading_date": data.get("latestMeterReading"),
            "has_flow_limitation": data.get("hasFlowLimitation"),
            "is_up_to_date": data.get("isUpToDate"),
            "address": data.get("address"),
            "divergent_consumption": data.get("divergentConsumption"),
            "days_offset": data.get("daysOffset"),
            "no_data_permission": data.get("noDataPermission")
        }
        
class WaterlinkNotificationSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, name, unit):
        super().__init__(coordinator)
        self._attr_name = name
        self._attr_unique_id = f"{name.replace(' ', '_').lower()}"
        

    @property
    def native_value(self):
        reading = self.coordinator.data.get("meterReading")
        if reading:
            try:
                return float(reading.replace(",", "."))
            except ValueError:
                _LOGGER.warning("Invalid reading format: %s", reading)
        return None

    @property
    def extra_state_attributes(self):
        data = self.coordinator.data
        return {
            "is_active": data.get("isActive"),
            "latest_reading_date": data.get("latestMeterReading"),
            "has_flow_limitation": data.get("hasFlowLimitation"),
            "is_up_to_date": data.get("isUpToDate"),
            "address": data.get("address"),
            "divergent_consumption": data.get("divergentConsumption"),
            "days_offset": data.get("daysOffset"),
            "no_data_permission": data.get("noDataPermission")
        }

