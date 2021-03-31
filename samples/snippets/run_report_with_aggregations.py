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

"""Google Analytics Data API sample application demonstrating the usage of
metric aggregations in a report.
"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import MetricAggregation
from google.analytics.data_v1beta.types import RunReportRequest

from run_report import print_run_report_response


def run_report_with_aggregations(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report which includes total, maximum and minimum values for
    each metric."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_aggregations]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="sessions")],
        date_ranges=[DateRange(start_date="yesterday", end_date="today")],
        metric_aggregations=[
            MetricAggregation.TOTAL,
            MetricAggregation.MAXIMUM,
            MetricAggregation.MINIMUM,
        ],
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_aggregations]
    print_run_report_response(response)


if __name__ == "__main__":
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"
    run_report_with_aggregations(property_id)
