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
#

def make_parent(parent: str) -> str:
    parent = parent

    return parent

def make_model(
    display_name: str,
    container_spec_image_uri: str,
    artifact_uri: str,
    input_tensor_name: str,
    output_tensor_name: str
) -> google.cloud.aiplatform_v1beta1.types.model.Model:

    # Container specification for deploying the model
    container_spec = {"image_uri": container_spec_image_uri, "command": [], "args": []}

    # The explainabilty method and corresponding parameters
    parameters = aiplatform.gapic.ExplanationParameters({"xrai_attribution": { "step_count": 1}})

    # The input tensor for feature attribution to the output
    # For single input model, y = f(x), this will be the serving input layer.
    input_metadata = aiplatform.gapic.ExplanationMetadata.InputMetadata({
        "input_tensor_name": input_tensor_name,
        # Input is image data
        "modality": "image",
    })

    # The output tensor to explain
    # For single output model, y = f(x), this will be the serving output layer.
    output_metadata = aiplatform.gapic.ExplanationMetadata.OutputMetadata({
        "output_tensor_name": output_tensor_name
    })

    # Assemble the explanation metadata
    metadata = aiplatform.gapic.ExplanationMetadata(
        inputs={'image': input_metadata},
        outputs={'prediction' : output_metadata}
    )

    # Assemble the explanation specification
    explanation_spec = aiplatform.gapic.ExplanationSpec(
        parameters=parameters,
        metadata=metadata
    )

    model = aiplatform.gapic.Model(display_name=display_name,
                                   # The Cloud Storage location of the custom model
                                   artifact_uri=artifact_uri,
                                   explanation_spec=explanation_spec,
                                   container_spec=container_spec
                                 )

    return model

