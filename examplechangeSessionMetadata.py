"""
---------------------------------------------------------------------------
OpenCap: changeSessionMetadata.py
---------------------------------------------------------------------------

Copyright 2022 Stanford University and the Authors

Author(s): Scott Uhlrich, Antoine Falisse

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy
of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


This script allows you to change the metadata of the session. E.g., to change
the pose estimator used when reprocessing data in the cloud. This is mostly for
developer use.
"""
import os
import sys
sys.path.append(os.path.abspath('./..'))

from utils import changeSessionMetadata

session_ids = ['77431277-3859-4a44-b58d-9cf1e4eed46a']

# Dictionary of metadata fields to change.
newMetadata = {'openSimModel':'FBLSmodel'} # dict of meta fields to change
# newMetadata= {'mass':83}

changeSessionMetadata(session_ids,newMetadata)