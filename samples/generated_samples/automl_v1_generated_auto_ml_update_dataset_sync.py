# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateDataset
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-automl


# [START automl_v1_generated_AutoMl_UpdateDataset_sync]
from google.cloud import automl_v1


def sample_update_dataset():
    # Create a client
    client = automl_v1.AutoMlClient()

    # Initialize request argument(s)
    dataset = automl_v1.Dataset()
    dataset.translation_dataset_metadata.source_language_code = "source_language_code_value"
    dataset.translation_dataset_metadata.target_language_code = "target_language_code_value"

    request = automl_v1.UpdateDatasetRequest(
        dataset=dataset,
    )

    # Make the request
    response = client.update_dataset(request=request)

    # Handle the response
    print(response)

# [END automl_v1_generated_AutoMl_UpdateDataset_sync]