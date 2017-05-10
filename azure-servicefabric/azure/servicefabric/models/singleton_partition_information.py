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

from .partition_information import PartitionInformation


class SingletonPartitionInformation(PartitionInformation):
    """Information about a partition that is singleton. The services with
    singletone partitioning scheme are effectively non-partitioned. They only
    have one partition.

    :param id:
    :type id: str
    :param ServicePartitionKind: Polymorphic Discriminator
    :type ServicePartitionKind: str
    """ 

    _validation = {
        'ServicePartitionKind': {'required': True},
    }

    def __init__(self, id=None):
        super(SingletonPartitionInformation, self).__init__(id=id)
        self.ServicePartitionKind = 'Singleton'