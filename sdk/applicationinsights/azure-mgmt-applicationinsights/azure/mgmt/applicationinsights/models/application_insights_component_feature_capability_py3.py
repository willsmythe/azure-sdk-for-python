# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationInsightsComponentFeatureCapability(Model):
    """An Application Insights component feature capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the capability.
    :vartype name: str
    :ivar description: The description of the capability.
    :vartype description: str
    :ivar value: The value of the capability.
    :vartype value: str
    :ivar unit: The unit of the capability.
    :vartype unit: str
    :ivar meter_id: The meter used for the capability.
    :vartype meter_id: str
    :ivar meter_rate_frequency: The meter rate of the meter.
    :vartype meter_rate_frequency: str
    """

    _validation = {
        'name': {'readonly': True},
        'description': {'readonly': True},
        'value': {'readonly': True},
        'unit': {'readonly': True},
        'meter_id': {'readonly': True},
        'meter_rate_frequency': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'value': {'key': 'Value', 'type': 'str'},
        'unit': {'key': 'Unit', 'type': 'str'},
        'meter_id': {'key': 'MeterId', 'type': 'str'},
        'meter_rate_frequency': {'key': 'MeterRateFrequency', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ApplicationInsightsComponentFeatureCapability, self).__init__(**kwargs)
        self.name = None
        self.description = None
        self.value = None
        self.unit = None
        self.meter_id = None
        self.meter_rate_frequency = None
