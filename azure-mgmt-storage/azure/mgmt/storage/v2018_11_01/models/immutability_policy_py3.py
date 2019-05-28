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

from .azure_entity_resource_py3 import AzureEntityResource


class ImmutabilityPolicy(AzureEntityResource):
    """The ImmutabilityPolicy property of a blob container, including Id, resource
    name, resource type, Etag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    :param immutability_period_since_creation_in_days: Required. The
     immutability period for the blobs in the container since the policy
     creation, in days.
    :type immutability_period_since_creation_in_days: int
    :ivar state: The ImmutabilityPolicy state of a blob container, possible
     values include: Locked and Unlocked. Possible values include: 'Locked',
     'Unlocked'
    :vartype state: str or
     ~azure.mgmt.storage.v2018_11_01.models.ImmutabilityPolicyState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
        'immutability_period_since_creation_in_days': {'required': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'immutability_period_since_creation_in_days': {'key': 'properties.immutabilityPeriodSinceCreationInDays', 'type': 'int'},
        'state': {'key': 'properties.state', 'type': 'str'},
    }

    def __init__(self, *, immutability_period_since_creation_in_days: int, **kwargs) -> None:
        super(ImmutabilityPolicy, self).__init__(**kwargs)
        self.immutability_period_since_creation_in_days = immutability_period_since_creation_in_days
        self.state = None
