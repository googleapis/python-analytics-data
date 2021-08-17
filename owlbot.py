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

common = gcp.CommonTemplates()

default_version = "v1beta"

for library in s.get_staging_dirs(default_version):
    s.move(
        library,
        excludes=[
            "setup.py",
            "README.rst",
            "docs/index.rst",
            f"scripts/fixup_data_{library.name}_keywords.py",
        ],
    )

s.remove_staging_dirs()

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(cov_level=99, microgenerator=True)
python.py_samples(skip_readmes=True)
s.move(
    templated_files, excludes=[
        ".coveragerc"
    ]
)  # the microgenerator has a good coveragerc file

# fix coverage target
s.replace(
    "noxfile.py",
    """(\s+)["']--cov=google.cloud["'],""",
    """"--cov=google.analytics",""",
)

# Wrap regex in docstring that sphinx thinks is a link with ``
s.replace(
    "google/**/data.py",
    '''"\^\[a-zA-Z0-9_\]\$"''',
    """``^[a-zA-Z0-9_]$``""",
)

# Block pushing non-cloud libraries to Cloud RAD
s.replace(
    ".kokoro/docs/common.cfg",
    r'value: "docs-staging-v2"',
    r'value: "docs-staging-v2-staging"'
)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
