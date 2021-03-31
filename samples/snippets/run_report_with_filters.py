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
dimension and metric filters in a report.
"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from google.analytics.data_v1beta.types import FilterExpression
from google.analytics.data_v1beta.types import FilterExpressionList
from google.analytics.data_v1beta.types import Filter
from google.analytics.data_v1beta.types import NumericValue
from run_report import print_run_report_response


def run_report_with_dimension_filter(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report using a dimension filter. The call returns a time series
    report of `eventCount` when `eventName` is `first_open` for each date."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_dimension_filter]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="date")],
        metrics=[Metric(name="eventCount")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
        dimension_filter=FilterExpression(
            filter=Filter(
                field_name="eventName",
                string_filter=Filter.StringFilter(value="first_open"),
            )
        ),
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_dimension_filter]
    print_run_report_response(response)


def run_report_with_multiple_dimension_filters(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report using multiple dimension filters joined as `and_group`
    expression. The filter selects for when both `browser` is `Chrome` and
    `countryId` is `US`."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_multiple_dimension_filters]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="browser")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
        dimension_filter=FilterExpression(
            and_group=FilterExpressionList(
                expressions=[
                    FilterExpression(
                        filter=Filter(
                            field_name="browser",
                            string_filter=Filter.StringFilter(value="Chrome"),
                        )
                    ),
                    FilterExpression(
                        filter=Filter(
                            field_name="countryId",
                            string_filter=Filter.StringFilter(value="US"),
                        )
                    ),
                ]
            )
        ),
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_multiple_dimension_filters]
    print_run_report_response(response)


def run_report_with_dimension_exclude_filter(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report using a filter with `not_expression`. The dimension filter
    selects for when `pageTitle` is not `My Homepage`."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_dimension_exclude_filter]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="pageTitle")],
        metrics=[Metric(name="sessions")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
        dimension_filter=FilterExpression(
            not_expression=FilterExpression(
                filter=Filter(
                    field_name="pageTitle",
                    string_filter=Filter.StringFilter(value="My Homepage"),
                )
            )
        ),
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_dimension_exclude_filter]
    print_run_report_response(response)


def run_report_with_dimension_in_list_filter(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report using a dimension filter with `in_list_filter` expression.
    The filter selects for when `eventName` is set to one of three event names
    specified in the query."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_dimension_in_list_filter]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="eventName")],
        metrics=[Metric(name="sessions")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
        dimension_filter=FilterExpression(
            filter=Filter(
                field_name="eventName",
                in_list_filter=Filter.InListFilter(
                    values=[
                        "purchase",
                        "in_app_purchase",
                        "app_store_subscription_renew",
                    ]
                ),
            )
        ),
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_dimension_in_list_filter]
    print_run_report_response(response)


def run_report_with_dimension_and_metric_filters(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report using both metric and dimension filters. A dimension filter
    limits the report to include only users who made an in-app purchase using
    Android platform. A metric filter specifies that only users with session
    counts larger than 1,000 should be included."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_run_report_with_dimension_and_metric_filters]
    request = RunReportRequest(
        property="properties/" + str(property_id),
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
        metric_filter=FilterExpression(
            filter=Filter(
                field_name="sessions",
                numeric_filter=Filter.NumericFilter(
                    operation=Filter.NumericFilter.Operation.GREATER_THAN,
                    value=NumericValue(int64_value=1000),
                ),
            )
        ),
        dimension_filter=FilterExpression(
            and_group=FilterExpressionList(
                expressions=[
                    FilterExpression(
                        filter=Filter(
                            field_name="platform",
                            string_filter=Filter.StringFilter(
                                match_type=Filter.StringFilter.MatchType.EXACT,
                                value="Android",
                            ),
                        )
                    ),
                    FilterExpression(
                        filter=Filter(
                            field_name="eventName",
                            string_filter=Filter.StringFilter(
                                match_type=Filter.StringFilter.MatchType.EXACT,
                                value="in_app_purchase",
                            ),
                        )
                    ),
                ]
            )
        ),
    )
    response = client.run_report(request)
    # [END analyticsdata_run_report_with_dimension_and_metric_filters]
    print_run_report_response(response)


if __name__ == "__main__":
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"

    run_report_with_dimension_filter(property_id)
    run_report_with_multiple_dimension_filters(property_id)
    run_report_with_dimension_exclude_filter(property_id)
    run_report_with_dimension_in_list_filter(property_id)
    run_report_with_dimension_and_metric_filters(property_id)
