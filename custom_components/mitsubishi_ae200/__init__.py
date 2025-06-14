"""The Mitsubishi AE200 integration."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_NAME, Platform
from homeassistant.core import HomeAssistant

from .mitsubishi_ae200 import MitsubishiAE200

_LOGGER = logging.getLogger(__name__)

DOMAIN = "mitsubishi_ae200"
PLATFORMS = [Platform.CLIMATE]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Mitsubishi AE200 from a config entry."""
    host = entry.data[CONF_HOST]
    name = entry.data[CONF_NAME]

    device = MitsubishiAE200(host)
    await device.connect()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = device

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        device = hass.data[DOMAIN].pop(entry.entry_id)
        await device.disconnect()

    return unload_ok