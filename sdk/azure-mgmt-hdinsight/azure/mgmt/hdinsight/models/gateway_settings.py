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


class GatewaySettings(Model):
    """Gateway settings.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar is_credential_enabled: Indicates whether or not the gateway settings
     based authorization is enabled.
    :vartype is_credential_enabled: str
    :ivar user_name: The gateway settings user name.
    :vartype user_name: str
    :ivar password: The gateway settings user password.
    :vartype password: str
    """

    _validation = {
        'is_credential_enabled': {'readonly': True},
        'user_name': {'readonly': True},
        'password': {'readonly': True},
    }

    _attribute_map = {
        'is_credential_enabled': {'key': 'restAuthCredential\\.isEnabled', 'type': 'str'},
        'user_name': {'key': 'restAuthCredential\\.username', 'type': 'str'},
        'password': {'key': 'restAuthCredential\\.password', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GatewaySettings, self).__init__(**kwargs)
        self.is_credential_enabled = None
        self.user_name = None
        self.password = None
