# Copyright 2021 Google LLC
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

# Lint as: python3
"""Stub API calls used in crm.py for testing.

Instead of doing real API calls, we return test JSON data.
"""

import json
import pathlib

# pylint: disable=unused-argument

PROJECT_JSON = pathlib.Path(__file__).parents[2] \
    / 'test-data/gke1/json-dumps/project.json'


class CrmApiStub:
  """Mock object to simulate container api calls."""

  def projects(self):
    return self

  def get(self, name):
    del name
    return self

  def execute(self, num_retries=0):
    with open(PROJECT_JSON) as json_file:
      return json.load(json_file)


def get_api_stub(service_name: str, version: str):
  if service_name == 'cloudresourcemanager':
    return CrmApiStub()
  else:
    raise ValueError('unsupported service: %s' % service_name)