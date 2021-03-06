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


class OperationMetricAvailability(Model):
    """Defines how often data for a metric becomes available.

    :param time_grain: The granularity for the metric.
    :type time_grain: str
    :param blob_duration: Blob created in the customer storage account, per
     hour.
    :type blob_duration: str
    """

    _attribute_map = {
        'time_grain': {'key': 'timeGrain', 'type': 'str'},
        'blob_duration': {'key': 'blobDuration', 'type': 'str'},
    }

    def __init__(self, *, time_grain: str=None, blob_duration: str=None, **kwargs) -> None:
        super(OperationMetricAvailability, self).__init__(**kwargs)
        self.time_grain = time_grain
        self.blob_duration = blob_duration
