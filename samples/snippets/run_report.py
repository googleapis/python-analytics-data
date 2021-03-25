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

"""Google Analytics Data API sample quickstart application.

This application demonstrates the usage of the Analytics Data API using
service account credentials.
"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest


def run_report_simple(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a simple report on a Google Analytics 4 property."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_simple]
    # Runs a report of active users grouped by three dimensions.
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-09-01", end_date="2020-09-15")],
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_simple]

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)


def run_report_with_multiple_dimensions(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report using multiple dimensions on a Google Analytics 4 property."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_multiple_dimensions]
    # Runs a report of active users grouped by three dimensions.
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

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)


def run_report_with_multiple_metrics(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a simple report using multiple metrics on a Google Analytics 4 property."""
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

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)


if __name__ == "__main__":
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"

    run_report_simple(property_id)
    run_report_with_multiple_metrics(property_id)
    run_report_with_multiple_dimensions(property_id)
