# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import json
import os

from awses_test_vectors.manifests.keys import KeysManifest


def load_keys_from_uri(parent_dir, keys_uri):
    # type: (str, str) -> KeysManifest
    """"""
    if not keys_uri.startswith("file://"):
        raise ValueError("Only file URIs are supported at this time.")

    with open(os.path.join(parent_dir, keys_uri[len("file://") :])) as keys_file:
        raw_manifest = json.load(keys_file)
        return KeysManifest.from_manifest_spec(raw_manifest)
