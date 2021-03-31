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

"""Google Analytics Data API sample application retrieving dimension and metrics
metadata.
"""
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import GetMetadataRequest
from google.analytics.data_v1beta.types import MetricType


def get_metadata_by_property_id(property_id="YOUR-GA4-PROPERTY-ID"):
    """Retrieves dimensions and metrics available for a Google Analytics 4
    property, including custom fields."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_get_metadata_by_property_id]
    request = GetMetadataRequest(
        name="properties/{property_id}/metadata".format(property_id=property_id)
    )
    response = client.get_metadata(request)
    # [END analyticsdata_get_metadata_by_property_id]

    print(
        "Dimensions and metrics available for Google Analytics 4 "
        "property {property_id} (including custom fields):".format(
            property_id=property_id
        )
    )
    print_get_metadata_response(response)


def get_common_metadata():
    """Retrieves dimensions and metrics available for all Google Analytics 4
    properties."""
    client = BetaAnalyticsDataClient()

    # [START analyticsdata_get_common_metadata]
    # Set the Property ID to 0 for dimensions and metrics common
    # to all properties. In this special mode, this method will
    # not return custom dimensions and metrics.
    property_id = 0
    request = GetMetadataRequest(
        name="properties/{property_id}/metadata".format(property_id=property_id)
    )
    response = client.get_metadata(request)
    # [END analyticsdata_get_common_metadata]

    print("Dimensions and metrics available for all Google Analytics 4 properties:")
    print_get_metadata_response(response)


def print_get_metadata_response(response):
    """Prints results of the getMetadata call."""
    # [START analyticsdata_print_get_metadata_response]
    for dimension in response.dimensions:
        print("DIMENSION")
        print(
            "{api_name} ({ui_name}): {description}".format(
                api_name=dimension.api_name,
                ui_name=dimension.ui_name,
                description=dimension.description,
            )
        )
        if dimension.custom_definition:
            print("This is a custom definition")
        if dimension.deprecated_api_names:
            print(
                "Deprecated API names: {deprecated_api_names}".format(
                    deprecated_api_names=dimension.deprecated_api_names
                )
            )
        print("")

    for metric in response.metrics:
        print("METRIC")
        print(
            "{api_name} ({ui_name}): {description}".format(
                api_name=metric.api_name,
                ui_name=metric.ui_name,
                description=metric.description,
            )
        )
        if metric.custom_definition:
            print("This is a custom definition")
        if metric.expression:
            print("Expression: {expression}".format(expression=metric.expression))
        print("Type: {metric_type}".format(metric_type=MetricType(metric.type_).name))
        if metric.deprecated_api_names:
            print(
                "Deprecated API names: {deprecated_api_names}".format(
                    deprecated_api_names=metric.deprecated_api_names
                )
            )
        print("")
    # [END analyticsdata_print_get_metadata_response]


if __name__ == "__main__":
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"
    get_metadata_by_property_id(property_id)
    get_common_metadata()
