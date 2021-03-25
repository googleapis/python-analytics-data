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

"""Google Analytics Data API real time report sample application.
"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunRealtimeReportRequest


def sample_run_realtime_report(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a realtime report on a Google Analytics 4 property."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_realtime_report]
    request = RunRealtimeReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="activeUsers")],
    )
    response = client.run_realtime_report(request)
    # [END analyticsdata_run_realtime_report]

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)


if __name__ == "__main__":
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"
    sample_run_realtime_report(property_id)
