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

"""Google Analytics Data API sample application.

This application demonstrates the usage of dimension and metric filters in the
Analytics Data API using service account credentials.

Before you start the application, please review the comments starting with
"TODO(developer)" and update the code to use correct values.

Usage:
  pip3 install --upgrade google-analytics-data
  python3 runReport_filter.py
"""
# [START google_analytics_data_sample]
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from google.analytics.data_v1beta.types import FilterExpression
from google.analytics.data_v1beta.types import FilterExpressionList
from google.analytics.data_v1beta.types import Filter
from google.analytics.data_v1beta.types import NumericValue


def sample_run_report(property_id='YOUR-GA4-PROPERTY-ID'):
  """Runs a simple report on a Google Analytics 4 property."""
  # TODO(developer): Uncomment this variable and replace with your
  #  Google Analytics 4 property ID before running the sample.
  # property_id = 'YOUR-GA4-PROPERTY-ID'

  client = BetaAnalyticsDataClient()

  # [START google_analytics_data_run_report]
  # Runs a report of active users count by city. A dimension filter limits the
  # report to include only users who made an in-app purchase using Android
  # platform. A metric filter specifies that only users with session counts
  # larger than 1,000 should be included.
  request = RunReportRequest(property='properties/' + str(property_id),
                             dimensions=[Dimension(name='city')],
                             metrics=[Metric(name='activeUsers')],
                             date_ranges=[DateRange(start_date='2020-03-31',
                                                    end_date='today')],
                             metric_filter=FilterExpression(
                                 filter=Filter(
                                     field_name='sessions',
                                     numeric_filter=Filter.NumericFilter(
                                         operation=Filter.NumericFilter.Operation.GREATER_THAN,
                                         value=NumericValue(int64_value=1000)
                                     )
                                 )),
                             dimension_filter=FilterExpression(
                                 and_group=FilterExpressionList(expressions=[
                                     FilterExpression(filter=
                                     Filter(
                                         field_name='platform',
                                         string_filter=Filter.StringFilter(
                                             match_type=Filter.StringFilter.MatchType.EXACT,
                                             value='Android'
                                         )
                                     )
                                     ),
                                     FilterExpression(filter=
                                     Filter(
                                         field_name='eventName',
                                         string_filter=Filter.StringFilter(
                                             match_type=Filter.StringFilter.MatchType.EXACT,
                                             value="in_app_purchase"
                                         )
                                     )
                                     )
                                 ])
                             ))
  response = client.run_report(request)
  # [END google_analytics_data_run_report]

  print("Report result:")
  for row in response.rows:
    print(row.dimension_values[0].value, row.metric_values[0].value)


# [END google_analytics_data_sample]

def main():
  sample_run_report()


if __name__ == "__main__":
  main()
