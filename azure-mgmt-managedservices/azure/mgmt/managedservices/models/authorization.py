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


class Authorization(Model):
    """Authorization tuple containing principal Id (of user/service
    principal/security group) and role definition id.

    All required parameters must be populated in order to send to Azure.

    :param principal_id: Required. Principal Id of the security group/service
     principal/user that would be assigned permissions to the projected
     subscription
    :type principal_id: str
    :param role_definition_id: Required. The role definition identifier. This
     role will define all the permissions that the security group/service
     principal/user must have on the projected subscription. This role cannot
     be an owner role.
    :type role_definition_id: str
    """

    _validation = {
        'principal_id': {'required': True},
        'role_definition_id': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Authorization, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)
        self.role_definition_id = kwargs.get('role_definition_id', None)
