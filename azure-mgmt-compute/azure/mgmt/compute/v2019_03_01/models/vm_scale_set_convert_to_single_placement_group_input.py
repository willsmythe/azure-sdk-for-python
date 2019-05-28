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


class VMScaleSetConvertToSinglePlacementGroupInput(Model):
    """VMScaleSetConvertToSinglePlacementGroupInput.

    :param active_placement_group_id: Id of the placement group in which you
     want future virtual machine instances to be placed. To query placement
     group Id, please use Virtual Machine Scale Set VMs - Get API. If not
     provided, the platform will choose one with maximum number of virtual
     machine instances.
    :type active_placement_group_id: str
    """

    _attribute_map = {
        'active_placement_group_id': {'key': 'activePlacementGroupId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VMScaleSetConvertToSinglePlacementGroupInput, self).__init__(**kwargs)
        self.active_placement_group_id = kwargs.get('active_placement_group_id', None)
