# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.analytics.data.v1alpha AlphaAnalyticsData API."""

import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.path_template
import grpc

from google.analytics.data.v1alpha.gapic import alpha_analytics_data_client_config
from google.analytics.data.v1alpha.gapic import enums
from google.analytics.data.v1alpha.gapic.transports import (
    alpha_analytics_data_grpc_transport,
)
from google.analytics.data.v1alpha.proto import analytics_data_api_pb2
from google.analytics.data.v1alpha.proto import analytics_data_api_pb2_grpc
from google.analytics.data.v1alpha.proto import data_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-analytics-data",
).version


class AlphaAnalyticsDataClient(object):
    """Google Analytics reporting data service."""

    SERVICE_ADDRESS = "analyticsdata.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.analytics.data.v1alpha.AlphaAnalyticsData"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AlphaAnalyticsDataClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def metadata_path(cls,):
        """Return a fully-qualified metadata string."""
        return google.api_core.path_template.expand("metadata",)

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.AlphaAnalyticsDataGrpcTransport,
                    Callable[[~.Credentials, type], ~.AlphaAnalyticsDataGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = alpha_analytics_data_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=alpha_analytics_data_grpc_transport.AlphaAnalyticsDataGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = alpha_analytics_data_grpc_transport.AlphaAnalyticsDataGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def run_report(
        self,
        entity=None,
        dimensions=None,
        metrics=None,
        date_ranges=None,
        offset=None,
        limit=None,
        metric_aggregations=None,
        dimension_filter=None,
        metric_filter=None,
        order_bys=None,
        currency_code=None,
        cohort_spec=None,
        keep_empty_rows=None,
        return_property_quota=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns a customized report of your Google Analytics event data. Reports
        contain statistics derived from data collected by the Google Analytics
        tracking code. The data returned from the API is as a table with columns
        for the requested dimensions and metrics. Metrics are individual
        measurements of user activity on your property, such as active users or
        event count. Dimensions break down metrics across some common criteria,
        such as country or event name.

        Example:
            >>> from google.analytics.data import v1alpha
            >>>
            >>> client = v1alpha.AlphaAnalyticsDataClient()
            >>>
            >>> response = client.run_report()

        Args:
            entity (Union[dict, ~google.analytics.data.v1alpha.types.Entity]): A property whose events are tracked. Within a batch request, this entity
                should either be unspecified or consistent with the batch-level entity.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.Entity`
            dimensions (list[Union[dict, ~google.analytics.data.v1alpha.types.Dimension]]): The dimensions requested and displayed.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.Dimension`
            metrics (list[Union[dict, ~google.analytics.data.v1alpha.types.Metric]]): The metrics requested and displayed.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.Metric`
            date_ranges (list[Union[dict, ~google.analytics.data.v1alpha.types.DateRange]]): Date ranges of data to read. If multiple date ranges are requested,
                each response row will contain a zero based date range index. If two
                date ranges overlap, the event data for the overlapping days is included
                in the response rows for both date ranges. In a cohort request, this
                ``dateRanges`` must be unspecified.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.DateRange`
            offset (long): The row count of the start row. The first row is counted as row 0.
            limit (long): The number of rows to return. If unspecified, 10 rows are returned. If
                -1, all rows are returned.
            metric_aggregations (list[~google.analytics.data.v1alpha.types.MetricAggregation]): Aggregation of metrics. Aggregated metric values will be shown in
                rows where the dimension_values are set to
                "RESERVED_(MetricAggregation)".
            dimension_filter (Union[dict, ~google.analytics.data.v1alpha.types.FilterExpression]): The filter clause of dimensions. Dimensions must be requested to be used in
                this filter. Metrics cannot be used in this filter.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.FilterExpression`
            metric_filter (Union[dict, ~google.analytics.data.v1alpha.types.FilterExpression]): The filter clause of metrics. Applied at post aggregation phase, similar to
                SQL having-clause. Metrics must be requested to be used in this filter.
                Dimensions cannot be used in this filter.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.FilterExpression`
            order_bys (list[Union[dict, ~google.analytics.data.v1alpha.types.OrderBy]]): Specifies how rows are ordered in the response.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.OrderBy`
            currency_code (str): A currency code in ISO4217 format, such as "AED", "USD", "JPY".
                If the field is empty, the report uses the entity's default currency.
            cohort_spec (Union[dict, ~google.analytics.data.v1alpha.types.CohortSpec]): Cohort group associated with this request. If there is a cohort group
                in the request the 'cohort' dimension must be present.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.CohortSpec`
            keep_empty_rows (bool): If false or unspecified, each row with all metrics equal to 0 will not be
                returned. If true, these rows will be returned if they are not separately
                removed by a filter.
            return_property_quota (bool): Toggles whether to return the current state of this Analytics
                Property's quota. Quota is returned in
                `PropertyQuota <#PropertyQuota>`__.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.data.v1alpha.types.RunReportResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "run_report" not in self._inner_api_calls:
            self._inner_api_calls[
                "run_report"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.run_report,
                default_retry=self._method_configs["RunReport"].retry,
                default_timeout=self._method_configs["RunReport"].timeout,
                client_info=self._client_info,
            )

        request = analytics_data_api_pb2.RunReportRequest(
            entity=entity,
            dimensions=dimensions,
            metrics=metrics,
            date_ranges=date_ranges,
            offset=offset,
            limit=limit,
            metric_aggregations=metric_aggregations,
            dimension_filter=dimension_filter,
            metric_filter=metric_filter,
            order_bys=order_bys,
            currency_code=currency_code,
            cohort_spec=cohort_spec,
            keep_empty_rows=keep_empty_rows,
            return_property_quota=return_property_quota,
        )
        return self._inner_api_calls["run_report"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def run_pivot_report(
        self,
        entity=None,
        dimensions=None,
        metrics=None,
        dimension_filter=None,
        metric_filter=None,
        pivots=None,
        date_ranges=None,
        currency_code=None,
        cohort_spec=None,
        keep_empty_rows=None,
        return_property_quota=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns a customized pivot report of your Google Analytics event data.
        Pivot reports are more advanced and expressive formats than regular
        reports. In a pivot report, dimensions are only visible if they are
        included in a pivot. Multiple pivots can be specified to further dissect
        your data.

        Example:
            >>> from google.analytics.data import v1alpha
            >>>
            >>> client = v1alpha.AlphaAnalyticsDataClient()
            >>>
            >>> response = client.run_pivot_report()

        Args:
            entity (Union[dict, ~google.analytics.data.v1alpha.types.Entity]): A property whose events are tracked. Within a batch request, this entity
                should either be unspecified or consistent with the batch-level entity.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.Entity`
            dimensions (list[Union[dict, ~google.analytics.data.v1alpha.types.Dimension]]): The dimensions requested. All defined dimensions must be used by one
                of the following: dimension_expression, dimension_filter, pivots,
                order_bys.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.Dimension`
            metrics (list[Union[dict, ~google.analytics.data.v1alpha.types.Metric]]): The metrics requested, at least one metric needs to be specified.
                All defined metrics must be used by one of the following:
                metric_expression, metric_filter, order_bys.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.Metric`
            dimension_filter (Union[dict, ~google.analytics.data.v1alpha.types.FilterExpression]): The filter clause of dimensions. Dimensions must be requested to be used in
                this filter. Metrics cannot be used in this filter.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.FilterExpression`
            metric_filter (Union[dict, ~google.analytics.data.v1alpha.types.FilterExpression]): The filter clause of metrics. Applied at post aggregation phase, similar to
                SQL having-clause. Metrics must be requested to be used in this filter.
                Dimensions cannot be used in this filter.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.FilterExpression`
            pivots (list[Union[dict, ~google.analytics.data.v1alpha.types.Pivot]]): Describes the visual format of the report's dimensions in columns or rows.
                The union of the fieldNames (dimension names) in all pivots must be a
                subset of dimension names defined in Dimensions. No two pivots can share a
                dimension. A dimension is only visible if it appears in a pivot.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.Pivot`
            date_ranges (list[Union[dict, ~google.analytics.data.v1alpha.types.DateRange]]): The date range to retrieve event data for the report. If multiple
                date ranges are specified, event data from each date range is used in
                the report. A special dimension with field name "dateRange" can be
                included in a Pivot's field names; if included, the report compares
                between date ranges. In a cohort request, this ``dateRanges`` must be
                unspecified.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.DateRange`
            currency_code (str): A currency code in ISO4217 format, such as "AED", "USD", "JPY".
                If the field is empty, the report uses the entity's default currency.
            cohort_spec (Union[dict, ~google.analytics.data.v1alpha.types.CohortSpec]): Cohort group associated with this request. If there is a cohort group
                in the request the 'cohort' dimension must be present.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.CohortSpec`
            keep_empty_rows (bool): If false or unspecified, each row with all metrics equal to 0 will not be
                returned. If true, these rows will be returned if they are not separately
                removed by a filter.
            return_property_quota (bool): Toggles whether to return the current state of this Analytics
                Property's quota. Quota is returned in
                `PropertyQuota <#PropertyQuota>`__.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.data.v1alpha.types.RunPivotReportResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "run_pivot_report" not in self._inner_api_calls:
            self._inner_api_calls[
                "run_pivot_report"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.run_pivot_report,
                default_retry=self._method_configs["RunPivotReport"].retry,
                default_timeout=self._method_configs["RunPivotReport"].timeout,
                client_info=self._client_info,
            )

        request = analytics_data_api_pb2.RunPivotReportRequest(
            entity=entity,
            dimensions=dimensions,
            metrics=metrics,
            dimension_filter=dimension_filter,
            metric_filter=metric_filter,
            pivots=pivots,
            date_ranges=date_ranges,
            currency_code=currency_code,
            cohort_spec=cohort_spec,
            keep_empty_rows=keep_empty_rows,
            return_property_quota=return_property_quota,
        )
        return self._inner_api_calls["run_pivot_report"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def batch_run_reports(
        self,
        entity=None,
        requests=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns multiple reports in a batch. All reports must be for the same
        Entity.

        Example:
            >>> from google.analytics.data import v1alpha
            >>>
            >>> client = v1alpha.AlphaAnalyticsDataClient()
            >>>
            >>> response = client.batch_run_reports()

        Args:
            entity (Union[dict, ~google.analytics.data.v1alpha.types.Entity]): A property whose events are tracked. This entity must be specified for the
                batch. The entity within RunReportRequest may either be unspecified or
                consistent with this entity.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.Entity`
            requests (list[Union[dict, ~google.analytics.data.v1alpha.types.RunReportRequest]]): Individual requests. Each request has a separate report response. Each
                batch request is allowed up to 5 requests.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.RunReportRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.data.v1alpha.types.BatchRunReportsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "batch_run_reports" not in self._inner_api_calls:
            self._inner_api_calls[
                "batch_run_reports"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_run_reports,
                default_retry=self._method_configs["BatchRunReports"].retry,
                default_timeout=self._method_configs["BatchRunReports"].timeout,
                client_info=self._client_info,
            )

        request = analytics_data_api_pb2.BatchRunReportsRequest(
            entity=entity, requests=requests,
        )
        return self._inner_api_calls["batch_run_reports"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def batch_run_pivot_reports(
        self,
        entity=None,
        requests=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns multiple pivot reports in a batch. All reports must be for the same
        Entity.

        Example:
            >>> from google.analytics.data import v1alpha
            >>>
            >>> client = v1alpha.AlphaAnalyticsDataClient()
            >>>
            >>> response = client.batch_run_pivot_reports()

        Args:
            entity (Union[dict, ~google.analytics.data.v1alpha.types.Entity]): A property whose events are tracked. This entity must be specified for the
                batch. The entity within RunPivotReportRequest may either be unspecified or
                consistent with this entity.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.Entity`
            requests (list[Union[dict, ~google.analytics.data.v1alpha.types.RunPivotReportRequest]]): Individual requests. Each request has a separate pivot report response.
                Each batch request is allowed up to 5 requests.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.data.v1alpha.types.RunPivotReportRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.data.v1alpha.types.BatchRunPivotReportsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "batch_run_pivot_reports" not in self._inner_api_calls:
            self._inner_api_calls[
                "batch_run_pivot_reports"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_run_pivot_reports,
                default_retry=self._method_configs["BatchRunPivotReports"].retry,
                default_timeout=self._method_configs["BatchRunPivotReports"].timeout,
                client_info=self._client_info,
            )

        request = analytics_data_api_pb2.BatchRunPivotReportsRequest(
            entity=entity, requests=requests,
        )
        return self._inner_api_calls["batch_run_pivot_reports"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_metadata(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns metadata for dimensions and metrics available in reporting methods.
        Used to explore the dimensions and metrics. Dimensions and metrics will be
        mostly added over time, but renames and deletions may occur.

        Example:
            >>> from google.analytics.data import v1alpha
            >>>
            >>> client = v1alpha.AlphaAnalyticsDataClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> response = client.get_metadata(name)

        Args:
            name (str): Required. The name of the metadata to retrieve. Either has the form
                'metadata' or 'properties/{property}/metadata'. This name field is
                specified in the URL path and not URL parameters. Property is a numeric
                Google Analytics App + Web Property Id.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.data.v1alpha.types.Metadata` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_metadata" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_metadata"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_metadata,
                default_retry=self._method_configs["GetMetadata"].retry,
                default_timeout=self._method_configs["GetMetadata"].timeout,
                client_info=self._client_info,
            )

        request = analytics_data_api_pb2.GetMetadataRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_metadata"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
