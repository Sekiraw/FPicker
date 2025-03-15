# SPDX-License-Identifier: Apache-2.0
# Author: Sekiraw

import fpicker

# Select a folder (but still see files like a file picker)
folder_path = fpicker.open(mode="folder")
if folder_path:
    print("Selected folder:", folder_path)
