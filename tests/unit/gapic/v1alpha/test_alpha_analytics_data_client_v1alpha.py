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

"""Unit tests."""

import mock
import pytest

from google.analytics.data import v1alpha
from google.analytics.data.v1alpha.proto import analytics_data_api_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestAlphaAnalyticsDataClient(object):
    def test_run_report(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = analytics_data_api_pb2.RunReportResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        response = client.run_report()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_data_api_pb2.RunReportRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_run_report_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        with pytest.raises(CustomException):
            client.run_report()

    def test_run_pivot_report(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = analytics_data_api_pb2.RunPivotReportResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        response = client.run_pivot_report()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_data_api_pb2.RunPivotReportRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_run_pivot_report_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        with pytest.raises(CustomException):
            client.run_pivot_report()

    def test_batch_run_reports(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = analytics_data_api_pb2.BatchRunReportsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        response = client.batch_run_reports()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_data_api_pb2.BatchRunReportsRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_batch_run_reports_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        with pytest.raises(CustomException):
            client.batch_run_reports()

    def test_batch_run_pivot_reports(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = analytics_data_api_pb2.BatchRunPivotReportsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        response = client.batch_run_pivot_reports()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_data_api_pb2.BatchRunPivotReportsRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_batch_run_pivot_reports_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        with pytest.raises(CustomException):
            client.batch_run_pivot_reports()

    def test_get_metadata(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        expected_response = {"name": name_2}
        expected_response = analytics_data_api_pb2.Metadata(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        # Setup Request
        name = "name3373707"

        response = client.get_metadata(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_data_api_pb2.GetMetadataRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_metadata_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AlphaAnalyticsDataClient()

        # Setup request
        name = "name3373707"

        with pytest.raises(CustomException):
            client.get_metadata(name)
