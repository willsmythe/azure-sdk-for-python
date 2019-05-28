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

from .apim_resource import ApimResource


class ApiManagementServiceResource(ApimResource):
    """A single API Management service resource in List or Get response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource is set to
     Microsoft.ApiManagement.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param notification_sender_email: Email address from which the
     notification will be sent.
    :type notification_sender_email: str
    :ivar provisioning_state: The current provisioning state of the API
     Management service which can be one of the following:
     Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted.
    :vartype provisioning_state: str
    :ivar target_provisioning_state: The provisioning state of the API
     Management service, which is targeted by the long running operation
     started on the service.
    :vartype target_provisioning_state: str
    :ivar created_at_utc: Creation UTC date of the API Management service.The
     date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
     by the ISO 8601 standard.
    :vartype created_at_utc: datetime
    :ivar gateway_url: Gateway URL of the API Management service.
    :vartype gateway_url: str
    :ivar gateway_regional_url: Gateway URL of the API Management service in
     the Default Region.
    :vartype gateway_regional_url: str
    :ivar portal_url: Publisher portal endpoint Url of the API Management
     service.
    :vartype portal_url: str
    :ivar management_api_url: Management API endpoint URL of the API
     Management service.
    :vartype management_api_url: str
    :ivar scm_url: SCM endpoint URL of the API Management service.
    :vartype scm_url: str
    :param hostname_configurations: Custom hostname configuration of the API
     Management service.
    :type hostname_configurations:
     list[~azure.mgmt.apimanagement.models.HostnameConfiguration]
    :ivar public_ip_addresses: Public Static Load Balanced IP addresses of the
     API Management service in Primary region. Available only for Basic,
     Standard and Premium SKU.
    :vartype public_ip_addresses: list[str]
    :ivar private_ip_addresses: Private Static Load Balanced IP addresses of
     the API Management service in Primary region which is deployed in an
     Internal Virtual Network. Available only for Basic, Standard and Premium
     SKU.
    :vartype private_ip_addresses: list[str]
    :param virtual_network_configuration: Virtual network configuration of the
     API Management service.
    :type virtual_network_configuration:
     ~azure.mgmt.apimanagement.models.VirtualNetworkConfiguration
    :param additional_locations: Additional datacenter locations of the API
     Management service.
    :type additional_locations:
     list[~azure.mgmt.apimanagement.models.AdditionalLocation]
    :param custom_properties: Custom properties of the API Management service.
     Setting
     `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168`
     will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1
     and 1.2). Setting
     `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11`
     can be used to disable just TLS 1.1 and setting
     `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10`
     can be used to disable TLS 1.0 on an API Management service.
    :type custom_properties: dict[str, str]
    :param certificates: List of Certificates that need to be installed in the
     API Management service. Max supported certificates that can be installed
     is 10.
    :type certificates:
     list[~azure.mgmt.apimanagement.models.CertificateConfiguration]
    :param enable_client_certificate: Property only meant to be used for
     Consumption SKU Service. This enforces a client certificate to be
     presented on each request to the gateway. This also enables the ability to
     authenticate the certificate in the policy on the gateway. Default value:
     False .
    :type enable_client_certificate: bool
    :param virtual_network_type: The type of VPN in which API Management
     service needs to be configured in. None (Default Value) means the API
     Management service is not part of any Virtual Network, External means the
     API Management deployment is set up inside a Virtual Network having an
     Internet Facing Endpoint, and Internal means that API Management
     deployment is setup inside a Virtual Network having an Intranet Facing
     Endpoint only. Possible values include: 'None', 'External', 'Internal'.
     Default value: "None" .
    :type virtual_network_type: str or
     ~azure.mgmt.apimanagement.models.VirtualNetworkType
    :param publisher_email: Required. Publisher email.
    :type publisher_email: str
    :param publisher_name: Required. Publisher name.
    :type publisher_name: str
    :param sku: Required. SKU properties of the API Management service.
    :type sku:
     ~azure.mgmt.apimanagement.models.ApiManagementServiceSkuProperties
    :param identity: Managed service identity of the Api Management service.
    :type identity:
     ~azure.mgmt.apimanagement.models.ApiManagementServiceIdentity
    :param location: Required. Resource location.
    :type location: str
    :ivar etag: ETag of the resource.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'notification_sender_email': {'max_length': 100},
        'provisioning_state': {'readonly': True},
        'target_provisioning_state': {'readonly': True},
        'created_at_utc': {'readonly': True},
        'gateway_url': {'readonly': True},
        'gateway_regional_url': {'readonly': True},
        'portal_url': {'readonly': True},
        'management_api_url': {'readonly': True},
        'scm_url': {'readonly': True},
        'public_ip_addresses': {'readonly': True},
        'private_ip_addresses': {'readonly': True},
        'publisher_email': {'required': True, 'max_length': 100},
        'publisher_name': {'required': True, 'max_length': 100},
        'sku': {'required': True},
        'location': {'required': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'notification_sender_email': {'key': 'properties.notificationSenderEmail', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'target_provisioning_state': {'key': 'properties.targetProvisioningState', 'type': 'str'},
        'created_at_utc': {'key': 'properties.createdAtUtc', 'type': 'iso-8601'},
        'gateway_url': {'key': 'properties.gatewayUrl', 'type': 'str'},
        'gateway_regional_url': {'key': 'properties.gatewayRegionalUrl', 'type': 'str'},
        'portal_url': {'key': 'properties.portalUrl', 'type': 'str'},
        'management_api_url': {'key': 'properties.managementApiUrl', 'type': 'str'},
        'scm_url': {'key': 'properties.scmUrl', 'type': 'str'},
        'hostname_configurations': {'key': 'properties.hostnameConfigurations', 'type': '[HostnameConfiguration]'},
        'public_ip_addresses': {'key': 'properties.publicIPAddresses', 'type': '[str]'},
        'private_ip_addresses': {'key': 'properties.privateIPAddresses', 'type': '[str]'},
        'virtual_network_configuration': {'key': 'properties.virtualNetworkConfiguration', 'type': 'VirtualNetworkConfiguration'},
        'additional_locations': {'key': 'properties.additionalLocations', 'type': '[AdditionalLocation]'},
        'custom_properties': {'key': 'properties.customProperties', 'type': '{str}'},
        'certificates': {'key': 'properties.certificates', 'type': '[CertificateConfiguration]'},
        'enable_client_certificate': {'key': 'properties.enableClientCertificate', 'type': 'bool'},
        'virtual_network_type': {'key': 'properties.virtualNetworkType', 'type': 'str'},
        'publisher_email': {'key': 'properties.publisherEmail', 'type': 'str'},
        'publisher_name': {'key': 'properties.publisherName', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'ApiManagementServiceSkuProperties'},
        'identity': {'key': 'identity', 'type': 'ApiManagementServiceIdentity'},
        'location': {'key': 'location', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApiManagementServiceResource, self).__init__(**kwargs)
        self.notification_sender_email = kwargs.get('notification_sender_email', None)
        self.provisioning_state = None
        self.target_provisioning_state = None
        self.created_at_utc = None
        self.gateway_url = None
        self.gateway_regional_url = None
        self.portal_url = None
        self.management_api_url = None
        self.scm_url = None
        self.hostname_configurations = kwargs.get('hostname_configurations', None)
        self.public_ip_addresses = None
        self.private_ip_addresses = None
        self.virtual_network_configuration = kwargs.get('virtual_network_configuration', None)
        self.additional_locations = kwargs.get('additional_locations', None)
        self.custom_properties = kwargs.get('custom_properties', None)
        self.certificates = kwargs.get('certificates', None)
        self.enable_client_certificate = kwargs.get('enable_client_certificate', False)
        self.virtual_network_type = kwargs.get('virtual_network_type', "None")
        self.publisher_email = kwargs.get('publisher_email', None)
        self.publisher_name = kwargs.get('publisher_name', None)
        self.sku = kwargs.get('sku', None)
        self.identity = kwargs.get('identity', None)
        self.location = kwargs.get('location', None)
        self.etag = None
