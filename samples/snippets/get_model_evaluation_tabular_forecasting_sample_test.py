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

import os


import get_model_evaluation_tabular_forecasting_sample

PROJECT_ID = "ucaip-sample-tests"  # os.getenv("BUILD_SPECIFIC_GCLOUD_PROJECT")
MODEL_ID = "8531330622239539200"  # COVID model
EVALUATION_ID = "5651454056920760520"


def test_ucaip_generated_get_model_evaluation_tabular_forecasting_sample(capsys):
    get_model_evaluation_tabular_forecasting_sample.get_model_evaluation_tabular_forecasting_sample(
        project=PROJECT_ID, model_id=MODEL_ID, evaluation_id=EVALUATION_ID
    )
    out, _ = capsys.readouterr()
    assert "metrics_schema_uri" in out
