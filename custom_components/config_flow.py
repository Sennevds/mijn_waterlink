import voluptuous as vol
from homeassistant.config_entries import OptionsFlowWithConfigEntry
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

class WaterlinkConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title=f"water-link meter {user_input['meter_id']}", data=user_input)

        data_schema = vol.Schema({
            vol.Required("username"): str,
            vol.Required("password"): str,
            vol.Required("client_id", default="07967700-64cf-4f26-825c-b13042574400"): str,
            vol.Required("meter_id"): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return WaterlinkOptionsFlowHandler(config_entry)


class WaterlinkOptionsFlowHandler(OptionsFlowWithConfigEntry):
    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        update_interval = self.options.get("update_interval", 7200)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional("update_interval", default=update_interval): int
            })
        )

