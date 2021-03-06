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


class PythonPackageCreateParameters(Model):
    """The parameters supplied to the create or update module operation.

    All required parameters must be populated in order to send to Azure.

    :param content_link: Required. Gets or sets the module content link.
    :type content_link: ~azure.mgmt.automation.models.ContentLink
    :param tags: Gets or sets the tags attached to the resource.
    :type tags: dict[str, str]
    """

    _validation = {
        'content_link': {'required': True},
    }

    _attribute_map = {
        'content_link': {'key': 'properties.contentLink', 'type': 'ContentLink'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(PythonPackageCreateParameters, self).__init__(**kwargs)
        self.content_link = kwargs.get('content_link', None)
        self.tags = kwargs.get('tags', None)
