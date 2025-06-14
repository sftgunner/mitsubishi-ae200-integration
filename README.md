# HomeAssistant - Mitsubishi AE200

Add support for Mitsubishi AE-200 air conditioner controller to HomeAssistant

## Installation

### Disclaimer

> :warning: This component is still in the alpha stage of development. It is highly likely that you will need to completely remove and reinstall this component in order to upgrade to the latest version, losing any entities defined in automations.

### Via HACS (preferred)

This component can be easily installed via the Home Assistant Community Store (HACS).

If you have not done so already, [follow the instructions to install HACS](https://hacs.xyz/docs/setup/download/) on your HomeAssistant instance.

Following that, [add this repository to the list of custom repositories in HACS](https://www.hacs.xyz/docs/faq/custom_repositories/), using the following url:

`https://github.com/sftgunner/mitsubishi-ae200-integration`

Then download the repo using HACS using the button below:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=sftgunner&repository=mitsubishi-ae200-integration&category=integration)


Then follow the steps in "Configuration" below.

### Configuration

Edit configuration.yaml and add below lines:

```	
climate:
  - platform: mitsubishi_ae200
    controller_id: name_of_controller  # used as part of entity id's
    ip_address: "<ip_address>"
```
