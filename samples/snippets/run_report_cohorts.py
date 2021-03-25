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
"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from google.analytics.data_v1beta.types import CohortsRange
from google.analytics.data_v1beta.types import CohortSpec
from google.analytics.data_v1beta.types import Cohort


def run_report_with_cohorts(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a simple report on a Google Analytics 4 property."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_cohorts]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="cohort"), Dimension(name="cohortNthWeek")],
        metrics=[
            Metric(name="cohortActiveUsers"),
            Metric(
                name="cohortRetentionRate",
                expression="cohortActiveUsers/cohortTotalUsers",
            ),
        ],
        cohorts_spec=CohortSpec(
            cohorts=[
                Cohort(
                    dimension="firstSessionDate",
                    name="cohort",
                    date_range=DateRange(
                        start_date="2021-01-03", end_date="2021-01-09"
                    ),
                )
            ]
        ),
        cohorts_range=CohortsRange(
            start_offset=0, end_offset=4, granularity=CohortsRange.Granularity.WEEKLY
        ),
    )

    response = client.run_report(request)
    # [END analyticsdata_run_report_with_cohorts]

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)


if __name__ == "__main__":
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"
    run_report_with_cohorts(property_id)
