# Copyright 2020 Google LLC
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

"""This script is used to synthesize generated parts of this library."""
import os

import synthtool as s
import synthtool.gcp as gcp
from synthtool.languages import python

gapic = gcp.GAPICBazel()
common = gcp.CommonTemplates()

versions = ["v1alpha", "v1beta"]

# The targets are named inconsistently, so bazel target cannot be
# constructed just from the string
# TODO: fix bazel targets so both use either 'google-analytics' or 'analytics'
bazel_targets = [
    "//google/analytics/data/v1alpha:google-analytics-data-v1alpha-py",
    "//google/analytics/data/v1beta:analytics-data-v1beta-py",
]

# ----------------------------------------------------------------------------
# Generate analytics data GAPIC layer
# ----------------------------------------------------------------------------
for version, bazel_target in zip(versions, bazel_targets):
    library = gapic.py_library(
        service="analyticsdata",
        version=version,
        bazel_target=bazel_target,
    )

    s.move(
        library,
        excludes=[
            "setup.py",
            "README.rst",
            "docs/index.rst",
            f"scripts/fixup_data_{version}_keywords.py",
        ],
    )

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(cov_level=99, microgenerator=True)
s.move(
    templated_files, excludes=[".coveragerc"]
)  # the microgenerator has a good coveragerc file

# fix coverage target
s.replace(
    "noxfile.py",
    """(\s+)["']--cov=google.cloud["'],""",
    """"--cov=google.analytics",""",
)

# Fix regex in docstring that sphinx thinks is a link
s.replace(
    "google/**/data.py",
    '''"\^\[a-zA-Z0-9_\]\$"''',
    """``^[a-zA-Z0-9_]$``""",
)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
