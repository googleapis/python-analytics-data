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


def run_report_with_pagination(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a simple report on a Google Analytics 4 property."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_pagination_page1]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        date_ranges=[DateRange(start_date="365daysAgo", end_date="yesterday")],
        dimensions=[
            Dimension(name="firstUserSource"),
            Dimension(name="firstUserMedium"),
            Dimension(name="firstUserCampaignName"),
        ],
        metrics=[
            Metric(name="sessions"),
            Metric(name="conversions"),
            Metric(name="totalRevenue"),
        ],
        limit=100000,
        offset=0,
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_pagination_page1]

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)

    # Run the same report with a different offset value to retrieve the second
    # page of a response.
    # [START analyticsdata_run_report_with_pagination_page2]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        date_ranges=[DateRange(start_date="365daysAgo", end_date="yesterday")],
        dimensions=[
            Dimension(name="firstUserSource"),
            Dimension(name="firstUserMedium"),
            Dimension(name="firstUserCampaignName"),
        ],
        metrics=[
            Metric(name="sessions"),
            Metric(name="conversions"),
            Metric(name="totalRevenue"),
        ],
        limit=100000,
        offset=100000,
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_pagination_page2]

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)


if __name__ == "__main__":
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"
    run_report_with_pagination(property_id)
