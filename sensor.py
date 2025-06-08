from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator
from datetime import timedelta
from .waterlink_api import WaterlinkClient
from .const import DOMAIN
import logging
from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
    SensorDeviceClass,
    SensorStateClass,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    username = config_entry.data["username"]
    password = config_entry.data["password"]
    client_id = config_entry.data["client_id"]
    meter_id = config_entry.data["meter_id"]

    update_interval = config_entry.options.get(
        "update_interval",
        config_entry.data.get("update_interval", 7200)
    )

    client = WaterlinkClient(username, password, client_id, meter_id)

    async def async_update_data():
        _LOGGER.debug("Authenticating and fetching data from Waterlink...")
        await hass.async_add_executor_job(client.authenticate)
        return await hass.async_add_executor_job(client.get_meter_data)

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"water-link meter {meter_id}",
        update_method=async_update_data,
        update_interval=timedelta(seconds=update_interval),
    )

    await coordinator.async_config_entry_first_refresh()

    reading = coordinator.data.get("meterReading")
    value = float(reading.replace(',', '.')) if reading else None

    entity = WaterlinkSensor(
        coordinator,
        name=f"water-link meter {meter_id}",
        state=value,
        unit="m³",
        attributes={
            "is_active": coordinator.data.get("isActive"),
            "latest_reading_date": coordinator.data.get("latestMeterReading"),
            "has_flow_limitation": coordinator.data.get("hasFlowLimitation"),
            "is_up_to_date": coordinator.data.get("isUpToDate"),
            "address": coordinator.data.get("address"),
            "divergent_consumption": coordinator.data.get("divergentConsumption"),
            "days_offset": coordinator.data.get("daysOffset"),
            "no_data_permission": coordinator.data.get("noDataPermission")
        }
    )

    async_add_entities([entity])

class WaterlinkSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, name, state, unit, attributes):
        super().__init__(coordinator)
        self._attr_name = name
        self._state = state
        self._attr_native_unit_of_measurement = unit
        self._attr_extra_state_attributes = attributes
        self._attr_unique_id = f"{name.replace(' ', '_').lower()}"
        self._attr_device_class = SensorDeviceClass.WATER
        self._attr_state_class = SensorStateClass.TOTAL_INCREASING

    @property
    def state(self):
        return self._state
