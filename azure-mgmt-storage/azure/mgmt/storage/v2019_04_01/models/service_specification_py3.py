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


class ServiceSpecification(Model):
    """One property of operation, include metric specifications.

    :param metric_specifications: Metric specifications of operation.
    :type metric_specifications:
     list[~azure.mgmt.storage.v2019_04_01.models.MetricSpecification]
    """

    _attribute_map = {
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[MetricSpecification]'},
    }

    def __init__(self, *, metric_specifications=None, **kwargs) -> None:
        super(ServiceSpecification, self).__init__(**kwargs)
        self.metric_specifications = metric_specifications
