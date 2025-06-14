"""Config flow for Mitsubishi AE200 integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_NAME
from homeassistant.data_entry_flow import FlowResult

from .mitsubishi_ae200 import MitsubishiAE200

_LOGGER = logging.getLogger(__name__)

DOMAIN = "mitsubishi_ae200"

class MitsubishiAE200ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Mitsubishi AE200."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            host = user_input[CONF_HOST]
            name = user_input[CONF_NAME]

            try:
                # Try to connect to the device
                device = MitsubishiAE200(host)
                await device.connect()
                await device.disconnect()

                return self.async_create_entry(
                    title=name,
                    data={
                        CONF_HOST: host,
                        CONF_NAME: name,
                    },
                )
            except Exception as err:
                _LOGGER.exception("Error connecting to Mitsubishi AE200: %s", err)
                errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                    vol.Required(CONF_NAME, default="Mitsubishi AE200"): str,
                }
            ),
            errors=errors,
        ) 