# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.analytics.data_v1beta.types import analytics_data_api
from google.analytics.data_v1beta.types import data
from .transports.base import BetaAnalyticsDataTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import BetaAnalyticsDataGrpcAsyncIOTransport
from .client import BetaAnalyticsDataClient


class BetaAnalyticsDataAsyncClient:
    """Google Analytics reporting data service."""

    _client: BetaAnalyticsDataClient

    DEFAULT_ENDPOINT = BetaAnalyticsDataClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = BetaAnalyticsDataClient.DEFAULT_MTLS_ENDPOINT

    metadata_path = staticmethod(BetaAnalyticsDataClient.metadata_path)
    parse_metadata_path = staticmethod(BetaAnalyticsDataClient.parse_metadata_path)
    common_billing_account_path = staticmethod(
        BetaAnalyticsDataClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(BetaAnalyticsDataClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        BetaAnalyticsDataClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_organization_path
    )
    common_project_path = staticmethod(BetaAnalyticsDataClient.common_project_path)
    parse_common_project_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_project_path
    )
    common_location_path = staticmethod(BetaAnalyticsDataClient.common_location_path)
    parse_common_location_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            BetaAnalyticsDataAsyncClient: The constructed client.
        """
        return BetaAnalyticsDataClient.from_service_account_info.__func__(BetaAnalyticsDataAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            BetaAnalyticsDataAsyncClient: The constructed client.
        """
        return BetaAnalyticsDataClient.from_service_account_file.__func__(BetaAnalyticsDataAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return BetaAnalyticsDataClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> BetaAnalyticsDataTransport:
        """Returns the transport used by the client instance.

        Returns:
            BetaAnalyticsDataTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(BetaAnalyticsDataClient).get_transport_class, type(BetaAnalyticsDataClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, BetaAnalyticsDataTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the beta analytics data client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.BetaAnalyticsDataTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = BetaAnalyticsDataClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def run_report(
        self,
        request: Union[analytics_data_api.RunReportRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> analytics_data_api.RunReportResponse:
        r"""Returns a customized report of your Google Analytics
        event data. Reports contain statistics derived from data
        collected by the Google Analytics tracking code. The
        data returned from the API is as a table with columns
        for the requested dimensions and metrics. Metrics are
        individual measurements of user activity on your
        property, such as active users or event count.
        Dimensions break down metrics across some common
        criteria, such as country or event name.


        .. code-block::

            from google.analytics import data_v1beta

            def sample_run_report():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1beta.RunReportRequest(
                )

                # Make the request
                response = client.run_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1beta.types.RunReportRequest, dict]):
                The request object. The request to generate a report.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.analytics.data_v1beta.types.RunReportResponse:
                The response report table
                corresponding to a request.

        """
        # Create or coerce a protobuf request object.
        request = analytics_data_api.RunReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.run_report,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def run_pivot_report(
        self,
        request: Union[analytics_data_api.RunPivotReportRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> analytics_data_api.RunPivotReportResponse:
        r"""Returns a customized pivot report of your Google
        Analytics event data. Pivot reports are more advanced
        and expressive formats than regular reports. In a pivot
        report, dimensions are only visible if they are included
        in a pivot. Multiple pivots can be specified to further
        dissect your data.


        .. code-block::

            from google.analytics import data_v1beta

            def sample_run_pivot_report():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1beta.RunPivotReportRequest(
                )

                # Make the request
                response = client.run_pivot_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1beta.types.RunPivotReportRequest, dict]):
                The request object. The request to generate a pivot
                report.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.analytics.data_v1beta.types.RunPivotReportResponse:
                The response pivot report table
                corresponding to a pivot request.

        """
        # Create or coerce a protobuf request object.
        request = analytics_data_api.RunPivotReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.run_pivot_report,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def batch_run_reports(
        self,
        request: Union[analytics_data_api.BatchRunReportsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> analytics_data_api.BatchRunReportsResponse:
        r"""Returns multiple reports in a batch. All reports must
        be for the same GA4 Property.


        .. code-block::

            from google.analytics import data_v1beta

            def sample_batch_run_reports():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1beta.BatchRunReportsRequest(
                )

                # Make the request
                response = client.batch_run_reports(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1beta.types.BatchRunReportsRequest, dict]):
                The request object. The batch request containing
                multiple report requests.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.analytics.data_v1beta.types.BatchRunReportsResponse:
                The batch response containing
                multiple reports.

        """
        # Create or coerce a protobuf request object.
        request = analytics_data_api.BatchRunReportsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_run_reports,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def batch_run_pivot_reports(
        self,
        request: Union[analytics_data_api.BatchRunPivotReportsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> analytics_data_api.BatchRunPivotReportsResponse:
        r"""Returns multiple pivot reports in a batch. All
        reports must be for the same GA4 Property.


        .. code-block::

            from google.analytics import data_v1beta

            def sample_batch_run_pivot_reports():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1beta.BatchRunPivotReportsRequest(
                )

                # Make the request
                response = client.batch_run_pivot_reports(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1beta.types.BatchRunPivotReportsRequest, dict]):
                The request object. The batch request containing
                multiple pivot report requests.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.analytics.data_v1beta.types.BatchRunPivotReportsResponse:
                The batch response containing
                multiple pivot reports.

        """
        # Create or coerce a protobuf request object.
        request = analytics_data_api.BatchRunPivotReportsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_run_pivot_reports,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_metadata(
        self,
        request: Union[analytics_data_api.GetMetadataRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> analytics_data_api.Metadata:
        r"""Returns metadata for dimensions and metrics available in
        reporting methods. Used to explore the dimensions and metrics.
        In this method, a Google Analytics GA4 Property Identifier is
        specified in the request, and the metadata response includes
        Custom dimensions and metrics as well as Universal metadata.

        For example if a custom metric with parameter name
        ``levels_unlocked`` is registered to a property, the Metadata
        response will contain ``customEvent:levels_unlocked``. Universal
        metadata are dimensions and metrics applicable to any property
        such as ``country`` and ``totalUsers``.


        .. code-block::

            from google.analytics import data_v1beta

            def sample_get_metadata():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1beta.GetMetadataRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_metadata(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1beta.types.GetMetadataRequest, dict]):
                The request object. Request for a property's dimension
                and metric metadata.
            name (:class:`str`):
                Required. The resource name of the metadata to retrieve.
                This name field is specified in the URL path and not URL
                parameters. Property is a numeric Google Analytics GA4
                Property identifier. To learn more, see `where to find
                your Property
                ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.

                Example: properties/1234/metadata

                Set the Property ID to 0 for dimensions and metrics
                common to all properties. In this special mode, this
                method will not return custom dimensions and metrics.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.analytics.data_v1beta.types.Metadata:
                The dimensions and metrics currently
                accepted in reporting methods.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = analytics_data_api.GetMetadataRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_metadata,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def run_realtime_report(
        self,
        request: Union[analytics_data_api.RunRealtimeReportRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> analytics_data_api.RunRealtimeReportResponse:
        r"""The Google Analytics Realtime API returns a
        customized report of realtime event data for your
        property. These reports show events and usage from the
        last 30 minutes.


        .. code-block::

            from google.analytics import data_v1beta

            def sample_run_realtime_report():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1beta.RunRealtimeReportRequest(
                )

                # Make the request
                response = client.run_realtime_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1beta.types.RunRealtimeReportRequest, dict]):
                The request object. The request to generate a realtime
                report.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.analytics.data_v1beta.types.RunRealtimeReportResponse:
                The response realtime report table
                corresponding to a request.

        """
        # Create or coerce a protobuf request object.
        request = analytics_data_api.RunRealtimeReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.run_realtime_report,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def check_compatibility(
        self,
        request: Union[analytics_data_api.CheckCompatibilityRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> analytics_data_api.CheckCompatibilityResponse:
        r"""This compatibility method lists dimensions and
        metrics that can be added to a report request and
        maintain compatibility. This method fails if the
        request's dimensions and metrics are incompatible.
        In Google Analytics, reports fail if they request
        incompatible dimensions and/or metrics; in that case,
        you will need to remove dimensions and/or metrics from
        the incompatible report until the report is compatible.
        The Realtime and Core reports have different
        compatibility rules. This method checks compatibility
        for Core reports.


        .. code-block::

            from google.analytics import data_v1beta

            def sample_check_compatibility():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1beta.CheckCompatibilityRequest(
                )

                # Make the request
                response = client.check_compatibility(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1beta.types.CheckCompatibilityRequest, dict]):
                The request object. The request for compatibility
                information for a report's dimensions and metrics. Check
                compatibility provides a preview of the compatibility of
                a report; fields shared with the `runReport` request
                should be the same values as in your `runReport`
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.analytics.data_v1beta.types.CheckCompatibilityResponse:
                The compatibility response with the
                compatibility of each dimension &
                metric.

        """
        # Create or coerce a protobuf request object.
        request = analytics_data_api.CheckCompatibilityRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.check_compatibility,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-analytics-data",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("BetaAnalyticsDataAsyncClient",)
