# Copyright 2020 Google Inc. All Rights Reserved.
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

import os

import run_report_filters

TEST_PROPERTY_ID = os.getenv("GA_TEST_PROPERTY_ID")

def test_run_report_with_dimension_filter(capsys):
    run_report_filters.run_report_with_dimension_filter(TEST_PROPERTY_ID)
    out, _ = capsys.readouterr()
    assert "Report result" in out


def test_run_report_with_multiple_dimension_filters(capsys):
    run_report_filters.run_report_with_multiple_dimension_filters(TEST_PROPERTY_ID)
    out, _ = capsys.readouterr()
    assert "Report result" in out


def test_run_report_with_dimension_exclude_filter(capsys):
    run_report_filters.run_report_with_dimension_exclude_filter(TEST_PROPERTY_ID)
    out, _ = capsys.readouterr()
    assert "Report result" in out


def run_report_with_dimension_in_list_filter(capsys):
    run_report_filters.run_report_with_dimension_in_list_filter(TEST_PROPERTY_ID)
    out, _ = capsys.readouterr()
    assert "Report result" in out


def run_run_report_with_dimension_and_metric_filters(capsys):
    run_report_filters.run_report_with_dimension_and_metric_filters(TEST_PROPERTY_ID)
    out, _ = capsys.readouterr()
    assert "Report result" in out

