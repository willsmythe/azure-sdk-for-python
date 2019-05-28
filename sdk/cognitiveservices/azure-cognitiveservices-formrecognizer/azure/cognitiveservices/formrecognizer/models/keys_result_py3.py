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


class KeysResult(Model):
    """Result of an operation to get
    the keys extracted by a model.

    :param clusters: Object mapping ClusterIds to Key lists.
    :type clusters: dict[str, list[str]]
    """

    _attribute_map = {
        'clusters': {'key': 'clusters', 'type': '{[str]}'},
    }

    def __init__(self, *, clusters=None, **kwargs) -> None:
        super(KeysResult, self).__init__(**kwargs)
        self.clusters = clusters
