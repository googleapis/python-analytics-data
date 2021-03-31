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

"""Google Analytics Data API sample application demonstrating the creation of
a pivot report.
"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunPivotReportRequest
from google.analytics.data_v1beta.types import OrderBy
from google.analytics.data_v1beta.types import Pivot
from run_report import print_run_report_response


def run_pivot_report(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a pivot query to build a report of session counts by country,
    pivoted by the browser dimension.."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_pivot_report]
    request = RunPivotReportRequest(
        property="properties/" + str(property_id),
        date_ranges=[
            DateRange(start_date="2021-01-01", end_date="2021-01-30"),
        ],
        pivots=[
            Pivot(
                field_names=["country"],
                limit=250,
                order_bys=[
                    OrderBy(
                        dimension=OrderBy.DimensionOrderBy(dimension_name="country")
                    )
                ],
            ),
            Pivot(
                field_names=["browser"],
                offset=3,
                limit=3,
                order_bys=[
                    OrderBy(
                        metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True
                    )
                ],
            ),
        ],
        metrics=[Metric(name="sessions")],
        dimensions=[
            Dimension(name="country"),
            Dimension(name="browser"),
        ],
    )
    response = client.run_pivot_report(request)
    # [END analyticsdata_run_pivot_report]
    print_run_report_response(response)


if __name__ == "__main__":
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"
    run_pivot_report(property_id)
