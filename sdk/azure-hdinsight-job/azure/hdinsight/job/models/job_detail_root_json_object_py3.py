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


class JobDetailRootJsonObject(Model):
    """The object containing the job details.

    :param callback: The callback URL, if any.
    :type callback: object
    :param completed: The string representing completed status, for example
     'done'.
    :type completed: str
    :param exit_value: The job's exit value.
    :type exit_value: int
    :param id: The job ID.
    :type id: str
    :param msg: The message returned.
    :type msg: object
    :param parent_id: The parent job ID.
    :type parent_id: str
    :param percent_complete: The job completion percentage, for example '75%
     complete'.
    :type percent_complete: str
    :param profile: The object containing the job profile information.
    :type profile: ~azure.hdinsight.job.models.Profile
    :param status: The object containing the job status information.
    :type status: ~azure.hdinsight.job.models.Status
    :param user: The user name of the job creator.
    :type user: str
    :param userargs: The arguments passed in by the user.
    :type userargs: ~azure.hdinsight.job.models.Userargs
    """

    _attribute_map = {
        'callback': {'key': 'callback', 'type': 'object'},
        'completed': {'key': 'completed', 'type': 'str'},
        'exit_value': {'key': 'exitValue', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'msg': {'key': 'msg', 'type': 'object'},
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'str'},
        'profile': {'key': 'profile', 'type': 'Profile'},
        'status': {'key': 'status', 'type': 'Status'},
        'user': {'key': 'user', 'type': 'str'},
        'userargs': {'key': 'userargs', 'type': 'Userargs'},
    }

    def __init__(self, *, callback=None, completed: str=None, exit_value: int=None, id: str=None, msg=None, parent_id: str=None, percent_complete: str=None, profile=None, status=None, user: str=None, userargs=None, **kwargs) -> None:
        super(JobDetailRootJsonObject, self).__init__(**kwargs)
        self.callback = callback
        self.completed = completed
        self.exit_value = exit_value
        self.id = id
        self.msg = msg
        self.parent_id = parent_id
        self.percent_complete = percent_complete
        self.profile = profile
        self.status = status
        self.user = user
        self.userargs = userargs
