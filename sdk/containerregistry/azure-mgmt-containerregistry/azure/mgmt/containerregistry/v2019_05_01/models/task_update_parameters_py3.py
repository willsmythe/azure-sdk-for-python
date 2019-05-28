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


class TaskUpdateParameters(Model):
    """The parameters for updating a task.

    :param identity: Identity for the resource.
    :type identity:
     ~azure.mgmt.containerregistry.v2019_05_01.models.IdentityProperties
    :param status: The current status of task. Possible values include:
     'Disabled', 'Enabled'
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_05_01.models.TaskStatus
    :param platform: The platform properties against which the run has to
     happen.
    :type platform:
     ~azure.mgmt.containerregistry.v2019_05_01.models.PlatformUpdateParameters
    :param agent_configuration: The machine configuration of the run agent.
    :type agent_configuration:
     ~azure.mgmt.containerregistry.v2019_05_01.models.AgentProperties
    :param timeout: Run timeout in seconds.
    :type timeout: int
    :param step: The properties for updating a task step.
    :type step:
     ~azure.mgmt.containerregistry.v2019_05_01.models.TaskStepUpdateParameters
    :param trigger: The properties for updating trigger properties.
    :type trigger:
     ~azure.mgmt.containerregistry.v2019_05_01.models.TriggerUpdateParameters
    :param credentials: The parameters that describes a set of credentials
     that will be used when this run is invoked.
    :type credentials:
     ~azure.mgmt.containerregistry.v2019_05_01.models.Credentials
    :param tags: The ARM resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'IdentityProperties'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'platform': {'key': 'properties.platform', 'type': 'PlatformUpdateParameters'},
        'agent_configuration': {'key': 'properties.agentConfiguration', 'type': 'AgentProperties'},
        'timeout': {'key': 'properties.timeout', 'type': 'int'},
        'step': {'key': 'properties.step', 'type': 'TaskStepUpdateParameters'},
        'trigger': {'key': 'properties.trigger', 'type': 'TriggerUpdateParameters'},
        'credentials': {'key': 'properties.credentials', 'type': 'Credentials'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, identity=None, status=None, platform=None, agent_configuration=None, timeout: int=None, step=None, trigger=None, credentials=None, tags=None, **kwargs) -> None:
        super(TaskUpdateParameters, self).__init__(**kwargs)
        self.identity = identity
        self.status = status
        self.platform = platform
        self.agent_configuration = agent_configuration
        self.timeout = timeout
        self.step = step
        self.trigger = trigger
        self.credentials = credentials
        self.tags = tags
