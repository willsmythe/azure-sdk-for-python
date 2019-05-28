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


class ExtractedKeyValuePair(Model):
    """Representation of a key-value pair as a list
    of key and value tokens.

    :param key: List of tokens for the extracted key in a key-value pair.
    :type key:
     list[~azure.cognitiveservices.formrecognizer.models.ExtractedToken]
    :param value: List of tokens for the extracted value in a key-value pair.
    :type value:
     list[~azure.cognitiveservices.formrecognizer.models.ExtractedToken]
    """

    _attribute_map = {
        'key': {'key': 'key', 'type': '[ExtractedToken]'},
        'value': {'key': 'value', 'type': '[ExtractedToken]'},
    }

    def __init__(self, *, key=None, value=None, **kwargs) -> None:
        super(ExtractedKeyValuePair, self).__init__(**kwargs)
        self.key = key
        self.value = value
