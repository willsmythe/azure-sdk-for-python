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


class ApiRevisionInfoContract(Model):
    """Object used to create an API Revision or Version based on an existing API
    Revision.

    :param source_api_id: Resource identifier of API to be used to create the
     revision from.
    :type source_api_id: str
    :param api_version_name: Version identifier for the new API Version.
    :type api_version_name: str
    :param api_revision_description: Description of new API Revision.
    :type api_revision_description: str
    :param api_version_set: Version set details
    :type api_version_set:
     ~azure.mgmt.apimanagement.models.ApiVersionSetContractDetails
    """

    _validation = {
        'api_version_name': {'max_length': 100},
        'api_revision_description': {'max_length': 256},
    }

    _attribute_map = {
        'source_api_id': {'key': 'sourceApiId', 'type': 'str'},
        'api_version_name': {'key': 'apiVersionName', 'type': 'str'},
        'api_revision_description': {'key': 'apiRevisionDescription', 'type': 'str'},
        'api_version_set': {'key': 'apiVersionSet', 'type': 'ApiVersionSetContractDetails'},
    }

    def __init__(self, **kwargs):
        super(ApiRevisionInfoContract, self).__init__(**kwargs)
        self.source_api_id = kwargs.get('source_api_id', None)
        self.api_version_name = kwargs.get('api_version_name', None)
        self.api_revision_description = kwargs.get('api_revision_description', None)
        self.api_version_set = kwargs.get('api_version_set', None)
