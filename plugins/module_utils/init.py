from ansible_module.turbo.module import AnsibleTurboModule

import importlib

# TODO: openstack_cloud_from_module, and take care of the environmnet variables

initialize_params = [
    "cloud",
    "auth"
]


def initialize(
    cloud=None, auth=None
):
    sdk = importlib.import_module('openstack')
    return {"sdk": sdk, "cloud": sdk.connect()}
