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


class OperationDefinition(Model):
    """The definition of a container registry operation.

    :param origin: The origin information of the container registry operation.
    :type origin: str
    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The display information for the container registry
     operation.
    :type display:
     ~azure.mgmt.containerregistry.v2019_04_01.models.OperationDisplayDefinition
    :param service_specification: The definition of Azure Monitoring service.
    :type service_specification:
     ~azure.mgmt.containerregistry.v2019_04_01.models.OperationServiceSpecificationDefinition
    """

    _attribute_map = {
        'origin': {'key': 'origin', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplayDefinition'},
        'service_specification': {'key': 'properties.serviceSpecification', 'type': 'OperationServiceSpecificationDefinition'},
    }

    def __init__(self, **kwargs):
        super(OperationDefinition, self).__init__(**kwargs)
        self.origin = kwargs.get('origin', None)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.service_specification = kwargs.get('service_specification', None)
