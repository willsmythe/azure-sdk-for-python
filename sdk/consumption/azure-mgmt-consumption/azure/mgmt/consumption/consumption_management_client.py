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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.usage_details_operations import UsageDetailsOperations
from .operations.marketplaces_operations import MarketplacesOperations
from .operations.budgets_operations import BudgetsOperations
from .operations.tags_operations import TagsOperations
from .operations.charges_operations import ChargesOperations
from .operations.balances_operations import BalancesOperations
from .operations.reservations_summaries_operations import ReservationsSummariesOperations
from .operations.reservations_details_operations import ReservationsDetailsOperations
from .operations.reservation_recommendations_operations import ReservationRecommendationsOperations
from .operations.price_sheet_operations import PriceSheetOperations
from .operations.forecasts_operations import ForecastsOperations
from .operations.operations import Operations
from .operations.aggregated_cost_operations import AggregatedCostOperations
from . import models


class ConsumptionManagementClientConfiguration(AzureConfiguration):
    """Configuration for ConsumptionManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ConsumptionManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-consumption/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ConsumptionManagementClient(SDKClient):
    """Consumption management client provides access to consumption resources for Azure Enterprise Subscriptions.

    :ivar config: Configuration for client.
    :vartype config: ConsumptionManagementClientConfiguration

    :ivar usage_details: UsageDetails operations
    :vartype usage_details: azure.mgmt.consumption.operations.UsageDetailsOperations
    :ivar marketplaces: Marketplaces operations
    :vartype marketplaces: azure.mgmt.consumption.operations.MarketplacesOperations
    :ivar budgets: Budgets operations
    :vartype budgets: azure.mgmt.consumption.operations.BudgetsOperations
    :ivar tags: Tags operations
    :vartype tags: azure.mgmt.consumption.operations.TagsOperations
    :ivar charges: Charges operations
    :vartype charges: azure.mgmt.consumption.operations.ChargesOperations
    :ivar balances: Balances operations
    :vartype balances: azure.mgmt.consumption.operations.BalancesOperations
    :ivar reservations_summaries: ReservationsSummaries operations
    :vartype reservations_summaries: azure.mgmt.consumption.operations.ReservationsSummariesOperations
    :ivar reservations_details: ReservationsDetails operations
    :vartype reservations_details: azure.mgmt.consumption.operations.ReservationsDetailsOperations
    :ivar reservation_recommendations: ReservationRecommendations operations
    :vartype reservation_recommendations: azure.mgmt.consumption.operations.ReservationRecommendationsOperations
    :ivar price_sheet: PriceSheet operations
    :vartype price_sheet: azure.mgmt.consumption.operations.PriceSheetOperations
    :ivar forecasts: Forecasts operations
    :vartype forecasts: azure.mgmt.consumption.operations.ForecastsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.consumption.operations.Operations
    :ivar aggregated_cost: AggregatedCost operations
    :vartype aggregated_cost: azure.mgmt.consumption.operations.AggregatedCostOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ConsumptionManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ConsumptionManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-04-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.usage_details = UsageDetailsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.marketplaces = MarketplacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.budgets = BudgetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tags = TagsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.charges = ChargesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.balances = BalancesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.reservations_summaries = ReservationsSummariesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.reservations_details = ReservationsDetailsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.reservation_recommendations = ReservationRecommendationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.price_sheet = PriceSheetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.forecasts = ForecastsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.aggregated_cost = AggregatedCostOperations(
            self._client, self.config, self._serialize, self._deserialize)
