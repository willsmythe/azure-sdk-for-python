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


class ImportSource(Model):
    """ImportSource.

    All required parameters must be populated in order to send to Azure.

    :param resource_id: The resource identifier of the source Azure Container
     Registry.
    :type resource_id: str
    :param registry_uri: The address of the source registry (e.g.
     'mcr.microsoft.com').
    :type registry_uri: str
    :param credentials: Credentials used when importing from a registry uri.
    :type credentials:
     ~azure.mgmt.containerregistry.v2019_05_01_preview.models.ImportSourceCredentials
    :param source_image: Required. Repository name of the source image.
     Specify an image by repository ('hello-world'). This will use the 'latest'
     tag.
     Specify an image by tag ('hello-world:latest').
     Specify an image by sha256-based manifest digest
     ('hello-world@sha256:abc123').
    :type source_image: str
    """

    _validation = {
        'source_image': {'required': True},
    }

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'registry_uri': {'key': 'registryUri', 'type': 'str'},
        'credentials': {'key': 'credentials', 'type': 'ImportSourceCredentials'},
        'source_image': {'key': 'sourceImage', 'type': 'str'},
    }

    def __init__(self, *, source_image: str, resource_id: str=None, registry_uri: str=None, credentials=None, **kwargs) -> None:
        super(ImportSource, self).__init__(**kwargs)
        self.resource_id = resource_id
        self.registry_uri = registry_uri
        self.credentials = credentials
        self.source_image = source_image
