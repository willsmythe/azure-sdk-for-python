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

from msrest.paging import Paged


class ApplicationGatewayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationGateway <azure.mgmt.network.v2018_02_01.models.ApplicationGateway>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationGateway]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationGatewayPaged, self).__init__(*args, **kwargs)
class ApplicationGatewaySslPredefinedPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationGatewaySslPredefinedPolicy <azure.mgmt.network.v2018_02_01.models.ApplicationGatewaySslPredefinedPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationGatewaySslPredefinedPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationGatewaySslPredefinedPolicyPaged, self).__init__(*args, **kwargs)
class ApplicationSecurityGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationSecurityGroup <azure.mgmt.network.v2018_02_01.models.ApplicationSecurityGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationSecurityGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationSecurityGroupPaged, self).__init__(*args, **kwargs)
class DdosProtectionPlanPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DdosProtectionPlan <azure.mgmt.network.v2018_02_01.models.DdosProtectionPlan>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DdosProtectionPlan]'}
    }

    def __init__(self, *args, **kwargs):

        super(DdosProtectionPlanPaged, self).__init__(*args, **kwargs)
class EndpointServiceResultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`EndpointServiceResult <azure.mgmt.network.v2018_02_01.models.EndpointServiceResult>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[EndpointServiceResult]'}
    }

    def __init__(self, *args, **kwargs):

        super(EndpointServiceResultPaged, self).__init__(*args, **kwargs)
class ExpressRouteCircuitAuthorizationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCircuitAuthorization <azure.mgmt.network.v2018_02_01.models.ExpressRouteCircuitAuthorization>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCircuitAuthorization]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCircuitAuthorizationPaged, self).__init__(*args, **kwargs)
class ExpressRouteCircuitPeeringPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCircuitPeering <azure.mgmt.network.v2018_02_01.models.ExpressRouteCircuitPeering>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCircuitPeering]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCircuitPeeringPaged, self).__init__(*args, **kwargs)
class ExpressRouteCircuitPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCircuit <azure.mgmt.network.v2018_02_01.models.ExpressRouteCircuit>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCircuit]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCircuitPaged, self).__init__(*args, **kwargs)
class ExpressRouteServiceProviderPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteServiceProvider <azure.mgmt.network.v2018_02_01.models.ExpressRouteServiceProvider>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteServiceProvider]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteServiceProviderPaged, self).__init__(*args, **kwargs)
class ExpressRouteCrossConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCrossConnection <azure.mgmt.network.v2018_02_01.models.ExpressRouteCrossConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCrossConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCrossConnectionPaged, self).__init__(*args, **kwargs)
class ExpressRouteCrossConnectionPeeringPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCrossConnectionPeering <azure.mgmt.network.v2018_02_01.models.ExpressRouteCrossConnectionPeering>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCrossConnectionPeering]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCrossConnectionPeeringPaged, self).__init__(*args, **kwargs)
class LoadBalancerPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LoadBalancer <azure.mgmt.network.v2018_02_01.models.LoadBalancer>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LoadBalancer]'}
    }

    def __init__(self, *args, **kwargs):

        super(LoadBalancerPaged, self).__init__(*args, **kwargs)
class BackendAddressPoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BackendAddressPool <azure.mgmt.network.v2018_02_01.models.BackendAddressPool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BackendAddressPool]'}
    }

    def __init__(self, *args, **kwargs):

        super(BackendAddressPoolPaged, self).__init__(*args, **kwargs)
class FrontendIPConfigurationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`FrontendIPConfiguration <azure.mgmt.network.v2018_02_01.models.FrontendIPConfiguration>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FrontendIPConfiguration]'}
    }

    def __init__(self, *args, **kwargs):

        super(FrontendIPConfigurationPaged, self).__init__(*args, **kwargs)
class InboundNatRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`InboundNatRule <azure.mgmt.network.v2018_02_01.models.InboundNatRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[InboundNatRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(InboundNatRulePaged, self).__init__(*args, **kwargs)
class LoadBalancingRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`LoadBalancingRule <azure.mgmt.network.v2018_02_01.models.LoadBalancingRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LoadBalancingRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(LoadBalancingRulePaged, self).__init__(*args, **kwargs)
class NetworkInterfacePaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkInterface <azure.mgmt.network.v2018_02_01.models.NetworkInterface>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkInterface]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkInterfacePaged, self).__init__(*args, **kwargs)
class ProbePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Probe <azure.mgmt.network.v2018_02_01.models.Probe>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Probe]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProbePaged, self).__init__(*args, **kwargs)
class NetworkInterfaceIPConfigurationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkInterfaceIPConfiguration <azure.mgmt.network.v2018_02_01.models.NetworkInterfaceIPConfiguration>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkInterfaceIPConfiguration]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkInterfaceIPConfigurationPaged, self).__init__(*args, **kwargs)
class NetworkSecurityGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkSecurityGroup <azure.mgmt.network.v2018_02_01.models.NetworkSecurityGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkSecurityGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkSecurityGroupPaged, self).__init__(*args, **kwargs)
class SecurityRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`SecurityRule <azure.mgmt.network.v2018_02_01.models.SecurityRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SecurityRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(SecurityRulePaged, self).__init__(*args, **kwargs)
class NetworkWatcherPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkWatcher <azure.mgmt.network.v2018_02_01.models.NetworkWatcher>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkWatcher]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkWatcherPaged, self).__init__(*args, **kwargs)
class PacketCaptureResultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PacketCaptureResult <azure.mgmt.network.v2018_02_01.models.PacketCaptureResult>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PacketCaptureResult]'}
    }

    def __init__(self, *args, **kwargs):

        super(PacketCaptureResultPaged, self).__init__(*args, **kwargs)
class ConnectionMonitorResultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ConnectionMonitorResult <azure.mgmt.network.v2018_02_01.models.ConnectionMonitorResult>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ConnectionMonitorResult]'}
    }

    def __init__(self, *args, **kwargs):

        super(ConnectionMonitorResultPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.network.v2018_02_01.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class PublicIPAddressPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PublicIPAddress <azure.mgmt.network.v2018_02_01.models.PublicIPAddress>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PublicIPAddress]'}
    }

    def __init__(self, *args, **kwargs):

        super(PublicIPAddressPaged, self).__init__(*args, **kwargs)
class RouteFilterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RouteFilter <azure.mgmt.network.v2018_02_01.models.RouteFilter>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RouteFilter]'}
    }

    def __init__(self, *args, **kwargs):

        super(RouteFilterPaged, self).__init__(*args, **kwargs)
class RouteFilterRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RouteFilterRule <azure.mgmt.network.v2018_02_01.models.RouteFilterRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RouteFilterRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(RouteFilterRulePaged, self).__init__(*args, **kwargs)
class RouteTablePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RouteTable <azure.mgmt.network.v2018_02_01.models.RouteTable>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RouteTable]'}
    }

    def __init__(self, *args, **kwargs):

        super(RouteTablePaged, self).__init__(*args, **kwargs)
class RoutePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Route <azure.mgmt.network.v2018_02_01.models.Route>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Route]'}
    }

    def __init__(self, *args, **kwargs):

        super(RoutePaged, self).__init__(*args, **kwargs)
class BgpServiceCommunityPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BgpServiceCommunity <azure.mgmt.network.v2018_02_01.models.BgpServiceCommunity>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BgpServiceCommunity]'}
    }

    def __init__(self, *args, **kwargs):

        super(BgpServiceCommunityPaged, self).__init__(*args, **kwargs)
class UsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Usage <azure.mgmt.network.v2018_02_01.models.Usage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Usage]'}
    }

    def __init__(self, *args, **kwargs):

        super(UsagePaged, self).__init__(*args, **kwargs)
class VirtualNetworkPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetwork <azure.mgmt.network.v2018_02_01.models.VirtualNetwork>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetwork]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkPaged, self).__init__(*args, **kwargs)
class VirtualNetworkUsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkUsage <azure.mgmt.network.v2018_02_01.models.VirtualNetworkUsage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkUsage]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkUsagePaged, self).__init__(*args, **kwargs)
class SubnetPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Subnet <azure.mgmt.network.v2018_02_01.models.Subnet>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Subnet]'}
    }

    def __init__(self, *args, **kwargs):

        super(SubnetPaged, self).__init__(*args, **kwargs)
class VirtualNetworkPeeringPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkPeering <azure.mgmt.network.v2018_02_01.models.VirtualNetworkPeering>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkPeering]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkPeeringPaged, self).__init__(*args, **kwargs)
class VirtualNetworkGatewayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkGateway <azure.mgmt.network.v2018_02_01.models.VirtualNetworkGateway>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkGateway]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkGatewayPaged, self).__init__(*args, **kwargs)
class VirtualNetworkGatewayConnectionListEntityPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkGatewayConnectionListEntity <azure.mgmt.network.v2018_02_01.models.VirtualNetworkGatewayConnectionListEntity>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkGatewayConnectionListEntity]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkGatewayConnectionListEntityPaged, self).__init__(*args, **kwargs)
class VirtualNetworkGatewayConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkGatewayConnection <azure.mgmt.network.v2018_02_01.models.VirtualNetworkGatewayConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkGatewayConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkGatewayConnectionPaged, self).__init__(*args, **kwargs)
class LocalNetworkGatewayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LocalNetworkGateway <azure.mgmt.network.v2018_02_01.models.LocalNetworkGateway>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LocalNetworkGateway]'}
    }

    def __init__(self, *args, **kwargs):

        super(LocalNetworkGatewayPaged, self).__init__(*args, **kwargs)
