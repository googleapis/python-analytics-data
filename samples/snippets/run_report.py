#!/usr/bin/env python

# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Analytics Data API sample application demonstrating the creation
of a basic report.
"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import MetricType
from google.analytics.data_v1beta.types import RunReportRequest


def run_sample():
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"
    run_report_simple(property_id)
    run_report_with_multiple_metrics(property_id)
    run_report_with_multiple_dimensions(property_id)


def run_report_simple(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report of active users grouped by country."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_simple]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-09-01", end_date="2020-09-15")],
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_simple]
    print_run_report_response(response)


def run_report_with_multiple_dimensions(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report of active users grouped by three dimensions."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_multiple_dimensions]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[
            Dimension(name="country"),
            Dimension(name="region"),
            Dimension(name="city"),
        ],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_multiple_dimensions]
    print_run_report_response(response)


def run_report_with_multiple_metrics(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report of active users, new users and total revenue grouped by
    date dimension."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_multiple_metrics]
    # Runs a report of active users grouped by three dimensions.
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="newUsers"),
            Metric(name="totalRevenue"),
        ],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_multiple_metrics]
    print_run_report_response(response)


def print_run_report_response(response):
    """Prints results of a runReport call."""
    # [START analyticsdata_print_run_report_response_header]
    print(f"{response.row_count} rows received")
    for dimensionHeader in response.dimension_headers:
        print(f"Dimension header name: {dimensionHeader.name}")
    for metricHeader in response.metric_headers:
        metric_type = MetricType(metricHeader.type_).name
        print(f"Metric header name: {metricHeader.name} ({metric_type})")
    # [END analyticsdata_print_run_report_response_header]

    # [START analyticsdata_print_run_report_response_rows]
    print("Report result:")
    for row in response.rows:
        for dimension_value in row.dimension_values:
            print(dimension_value.value)

        for metric_value in row.metric_values:
            print(metric_value.value)
    # [END analyticsdata_print_run_report_response_rows]


if __name__ == "__main__":
    run_sample()
