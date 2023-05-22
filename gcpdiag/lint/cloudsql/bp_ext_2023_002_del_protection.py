# Copyright 2023 Google LLC
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
"""Cloud SQL should be configured with Deletion Protection

Protect your CloudSQL instance and backups from accidental deletion
"""

from gcpdiag import lint, models
from gcpdiag.queries import apis, cloudsql


def run_rule(context: models.Context, report: lint.LintReportRuleInterface):
  if not apis.is_enabled(context.project_id, 'sqladmin'):
    report.add_skipped(None, 'sqladmin is disabled')
    return

  instances = cloudsql.get_instances(context)

  if not instances:
    report.add_skipped(None, 'no CloudSQL instances found')
    return

  for instance in instances:
    if not instance.has_del_protection:
      report.add_failed(instance)
    else:
      report.add_ok(instance)
