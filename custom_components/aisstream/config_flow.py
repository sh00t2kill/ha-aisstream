import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_API_KEY

from .const import DOMAIN, CONF_MMSI_LIST


class AISstreamConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the AISstream integration setup UI."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            mmsi_list = [
                m.strip()
                for m in user_input[CONF_MMSI_LIST].split(",")
                if m.strip().isdigit()
            ]
            if not mmsi_list:
                errors[CONF_MMSI_LIST] = "invalid_mmsi"
            else:
                return self.async_create_entry(
                    title="AISstream",
                    data={
                        CONF_API_KEY: user_input[CONF_API_KEY],
                        CONF_MMSI_LIST: mmsi_list,
                    },
                )

        schema = vol.Schema({
            vol.Required(CONF_API_KEY): str,
            vol.Required(CONF_MMSI_LIST): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
