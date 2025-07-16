import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import DOMAIN
from .waterlink_api import WaterlinkClient

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up the Waterlink integration from a config entry."""
    username = config_entry.data["username"]
    password = config_entry.data["password"]
    client_id = config_entry.data["client_id"]
    meter_id = config_entry.data["meter_id"]

    client = WaterlinkClient(username, password, client_id, meter_id)

    # Pre-check API connectivity before forwarding to sensor platform
    try:
        _LOGGER.debug("Testing Waterlink API connectivity before setup...")
        await hass.async_add_executor_job(client.authenticate)
        await hass.async_add_executor_job(client.get_meter_data)
    except Exception as err:
        _LOGGER.warning("Waterlink API not ready: %s", err)
        raise ConfigEntryNotReady(f"Cannot connect to Waterlink API: {err}") from err

    # Forward to sensor platform only if API is reachable
    await hass.config_entries.async_forward_entry_setups(config_entry, ["sensor"])
    return True


async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Unload the Waterlink config entry."""
    return await hass.config_entries.async_unload_platforms(config_entry, ["sensor"])
