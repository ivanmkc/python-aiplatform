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

# [START aiplatform_list_model_evaluations_tabular_forecasting_sample]
from google.cloud import aiplatform


def list_model_evaluations_tabular_forecasting_sample(
    project: str,
    model_id: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.ModelServiceClient(client_options=client_options)
    parent = client.model_path(project=project, location=location, model=model_id)
    response = client.list_model_evaluations(parent=parent)
    for model_evaluation in response:
        print("model_evaluation:", model_evaluation)


# [END aiplatform_list_model_evaluations_tabular_forecasting_sample]