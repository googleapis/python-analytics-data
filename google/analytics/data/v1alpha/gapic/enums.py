# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class MetricAggregation(enum.IntEnum):
    """
    Represents aggregation of metrics.

    Attributes:
      METRIC_AGGREGATION_UNSPECIFIED (int): Unspecified operator.
      TOTAL (int): SUM operator.
      MINIMUM (int): Minimum operator.
      MAXIMUM (int): Maximum operator.
      COUNT (int): Count operator.
    """

    METRIC_AGGREGATION_UNSPECIFIED = 0
    TOTAL = 1
    MINIMUM = 5
    MAXIMUM = 6
    COUNT = 4


class MetricType(enum.IntEnum):
    """
    A metric's value type.

    Attributes:
      METRIC_TYPE_UNSPECIFIED (int): Unspecified type.
      TYPE_INTEGER (int): Integer type.
      TYPE_FLOAT (int): Floating point type.
      TYPE_SECONDS (int): A duration of seconds; a special floating point type.
      TYPE_CURRENCY (int): An amount of money; a special floating point type.
    """

    METRIC_TYPE_UNSPECIFIED = 0
    TYPE_INTEGER = 1
    TYPE_FLOAT = 2
    TYPE_SECONDS = 4
    TYPE_CURRENCY = 9


class CohortsRange(object):
    class Granularity(enum.IntEnum):
        """
        Reporting granularity for the cohorts.

        Attributes:
          GRANULARITY_UNSPECIFIED (int): Unspecified.
          DAILY (int): Daily
          WEEKLY (int): Weekly
          MONTHLY (int): Monthly
        """

        GRANULARITY_UNSPECIFIED = 0
        DAILY = 1
        WEEKLY = 2
        MONTHLY = 3


class Filter(object):
    class StringFilter(object):
        class MatchType(enum.IntEnum):
            """
            The match type of a string filter

            Attributes:
              MATCH_TYPE_UNSPECIFIED (int): Unspecified
              EXACT (int): Exact match of the string value.
              BEGINS_WITH (int): Begins with the string value.
              ENDS_WITH (int): Ends with the string value.
              CONTAINS (int): Contains the string value.
              FULL_REGEXP (int): Full regular expression match with the string value.
              PARTIAL_REGEXP (int): Partial regular expression match with the string value.
            """

            MATCH_TYPE_UNSPECIFIED = 0
            EXACT = 1
            BEGINS_WITH = 2
            ENDS_WITH = 3
            CONTAINS = 4
            FULL_REGEXP = 5
            PARTIAL_REGEXP = 6

    class NumericFilter(object):
        class Operation(enum.IntEnum):
            """
            The operation applied to a numeric filter

            Attributes:
              OPERATION_UNSPECIFIED (int): Unspecified.
              EQUAL (int): Equal
              LESS_THAN (int): Less than
              LESS_THAN_OR_EQUAL (int): Less than or equal
              GREATER_THAN (int): Greater than
              GREATER_THAN_OR_EQUAL (int): Greater than or equal
            """

            OPERATION_UNSPECIFIED = 0
            EQUAL = 1
            LESS_THAN = 2
            LESS_THAN_OR_EQUAL = 3
            GREATER_THAN = 4
            GREATER_THAN_OR_EQUAL = 5


class OrderBy(object):
    class DimensionOrderBy(object):
        class OrderType(enum.IntEnum):
            """
            Rule to order the string dimension values by.

            Attributes:
              ORDER_TYPE_UNSPECIFIED (int): Unspecified.
              ALPHANUMERIC (int): Alphanumeric sort by Unicode code point. For example, "2" < "A" < "X" <
              "b" < "z".
              CASE_INSENSITIVE_ALPHANUMERIC (int): Case insensitive alphanumeric sort by lower case Unicode code point.
              For example, "2" < "A" < "b" < "X" < "z".
              NUMERIC (int): Dimension values are converted to numbers before sorting. For
              example in NUMERIC sort, "25" < "100", and in ``ALPHANUMERIC`` sort,
              "100" < "25". Non-numeric dimension values all have equal ordering value
              below all numeric values.
            """

            ORDER_TYPE_UNSPECIFIED = 0
            ALPHANUMERIC = 1
            CASE_INSENSITIVE_ALPHANUMERIC = 2
            NUMERIC = 3
