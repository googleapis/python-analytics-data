# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.analytics.data_v1alpha import gapic_version as package_version

__version__ = package_version.__version__


from .services.alpha_analytics_data import (
    AlphaAnalyticsDataAsyncClient,
    AlphaAnalyticsDataClient,
)
from .types.analytics_data_api import (
    AudienceDimension,
    AudienceDimensionValue,
    AudienceList,
    AudienceListMetadata,
    AudienceRow,
    CreateAudienceListRequest,
    GetAudienceListRequest,
    ListAudienceListsRequest,
    ListAudienceListsResponse,
    QueryAudienceListRequest,
    QueryAudienceListResponse,
    RunFunnelReportRequest,
    RunFunnelReportResponse,
)
from .types.data import (
    BetweenFilter,
    DateRange,
    Dimension,
    DimensionExpression,
    DimensionHeader,
    DimensionValue,
    EventCriteriaScoping,
    EventExclusionDuration,
    EventSegment,
    EventSegmentConditionGroup,
    EventSegmentCriteria,
    EventSegmentExclusion,
    Filter,
    FilterExpression,
    FilterExpressionList,
    Funnel,
    FunnelBreakdown,
    FunnelEventFilter,
    FunnelFieldFilter,
    FunnelFilterExpression,
    FunnelFilterExpressionList,
    FunnelNextAction,
    FunnelParameterFilter,
    FunnelParameterFilterExpression,
    FunnelParameterFilterExpressionList,
    FunnelResponseMetadata,
    FunnelStep,
    FunnelSubReport,
    InListFilter,
    MetricHeader,
    MetricType,
    MetricValue,
    NumericFilter,
    NumericValue,
    PropertyQuota,
    QuotaStatus,
    Row,
    SamplingMetadata,
    Segment,
    SegmentEventFilter,
    SegmentFilter,
    SegmentFilterExpression,
    SegmentFilterExpressionList,
    SegmentFilterScoping,
    SegmentParameterFilter,
    SegmentParameterFilterExpression,
    SegmentParameterFilterExpressionList,
    SegmentParameterFilterScoping,
    SessionCriteriaScoping,
    SessionExclusionDuration,
    SessionSegment,
    SessionSegmentConditionGroup,
    SessionSegmentCriteria,
    SessionSegmentExclusion,
    StringFilter,
    UserCriteriaScoping,
    UserExclusionDuration,
    UserSegment,
    UserSegmentConditionGroup,
    UserSegmentCriteria,
    UserSegmentExclusion,
    UserSegmentSequenceGroup,
    UserSequenceStep,
)

__all__ = (
    "AlphaAnalyticsDataAsyncClient",
    "AlphaAnalyticsDataClient",
    "AudienceDimension",
    "AudienceDimensionValue",
    "AudienceList",
    "AudienceListMetadata",
    "AudienceRow",
    "BetweenFilter",
    "CreateAudienceListRequest",
    "DateRange",
    "Dimension",
    "DimensionExpression",
    "DimensionHeader",
    "DimensionValue",
    "EventCriteriaScoping",
    "EventExclusionDuration",
    "EventSegment",
    "EventSegmentConditionGroup",
    "EventSegmentCriteria",
    "EventSegmentExclusion",
    "Filter",
    "FilterExpression",
    "FilterExpressionList",
    "Funnel",
    "FunnelBreakdown",
    "FunnelEventFilter",
    "FunnelFieldFilter",
    "FunnelFilterExpression",
    "FunnelFilterExpressionList",
    "FunnelNextAction",
    "FunnelParameterFilter",
    "FunnelParameterFilterExpression",
    "FunnelParameterFilterExpressionList",
    "FunnelResponseMetadata",
    "FunnelStep",
    "FunnelSubReport",
    "GetAudienceListRequest",
    "InListFilter",
    "ListAudienceListsRequest",
    "ListAudienceListsResponse",
    "MetricHeader",
    "MetricType",
    "MetricValue",
    "NumericFilter",
    "NumericValue",
    "PropertyQuota",
    "QueryAudienceListRequest",
    "QueryAudienceListResponse",
    "QuotaStatus",
    "Row",
    "RunFunnelReportRequest",
    "RunFunnelReportResponse",
    "SamplingMetadata",
    "Segment",
    "SegmentEventFilter",
    "SegmentFilter",
    "SegmentFilterExpression",
    "SegmentFilterExpressionList",
    "SegmentFilterScoping",
    "SegmentParameterFilter",
    "SegmentParameterFilterExpression",
    "SegmentParameterFilterExpressionList",
    "SegmentParameterFilterScoping",
    "SessionCriteriaScoping",
    "SessionExclusionDuration",
    "SessionSegment",
    "SessionSegmentConditionGroup",
    "SessionSegmentCriteria",
    "SessionSegmentExclusion",
    "StringFilter",
    "UserCriteriaScoping",
    "UserExclusionDuration",
    "UserSegment",
    "UserSegmentConditionGroup",
    "UserSegmentCriteria",
    "UserSegmentExclusion",
    "UserSegmentSequenceGroup",
    "UserSequenceStep",
)
