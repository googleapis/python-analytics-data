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


import google.api_core.grpc_helpers

from google.analytics.data.v1alpha.proto import analytics_data_api_pb2_grpc


class AlphaAnalyticsDataGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.analytics.data.v1alpha AlphaAnalyticsData API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        "https://www.googleapis.com/auth/analytics",
        "https://www.googleapis.com/auth/analytics.readonly",
    )

    def __init__(
        self, channel=None, credentials=None, address="analyticsdata.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive.",
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "alpha_analytics_data_stub": analytics_data_api_pb2_grpc.AlphaAnalyticsDataStub(
                channel
            ),
        }

    @classmethod
    def create_channel(
        cls, address="analyticsdata.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def run_report(self):
        """Return the gRPC stub for :meth:`AlphaAnalyticsDataClient.run_report`.

        Returns a customized report of your Google Analytics event data. Reports
        contain statistics derived from data collected by the Google Analytics
        tracking code. The data returned from the API is as a table with columns
        for the requested dimensions and metrics. Metrics are individual
        measurements of user activity on your property, such as active users or
        event count. Dimensions break down metrics across some common criteria,
        such as country or event name.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["alpha_analytics_data_stub"].RunReport

    @property
    def run_pivot_report(self):
        """Return the gRPC stub for :meth:`AlphaAnalyticsDataClient.run_pivot_report`.

        Returns a customized pivot report of your Google Analytics event data.
        Pivot reports are more advanced and expressive formats than regular
        reports. In a pivot report, dimensions are only visible if they are
        included in a pivot. Multiple pivots can be specified to further dissect
        your data.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["alpha_analytics_data_stub"].RunPivotReport

    @property
    def batch_run_reports(self):
        """Return the gRPC stub for :meth:`AlphaAnalyticsDataClient.batch_run_reports`.

        Returns multiple reports in a batch. All reports must be for the same
        Entity.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["alpha_analytics_data_stub"].BatchRunReports

    @property
    def batch_run_pivot_reports(self):
        """Return the gRPC stub for :meth:`AlphaAnalyticsDataClient.batch_run_pivot_reports`.

        Returns multiple pivot reports in a batch. All reports must be for the same
        Entity.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["alpha_analytics_data_stub"].BatchRunPivotReports

    @property
    def get_metadata(self):
        """Return the gRPC stub for :meth:`AlphaAnalyticsDataClient.get_metadata`.

        Returns metadata for dimensions and metrics available in reporting methods.
        Used to explore the dimensions and metrics. Dimensions and metrics will be
        mostly added over time, but renames and deletions may occur.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["alpha_analytics_data_stub"].GetMetadata
