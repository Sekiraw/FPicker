# SPDX-License-Identifier: Apache-2.0
# Author: Sekiraw

"""
fpicker module

A lightweight file and folder picker for Windows.

Functions:
- open(mode='file'): Opens a file or folder picker dialog. 
  - mode: 'file' (default) opens a file picker.
         'folder' opens a folder picker.

Example usage:
    import fpicker
    file_path = fpicker.open()
    folder_path = fpicker.open(mode='folder')
"""

def open(mode: str = 'file') -> str | None:
    """
    Open a file or folder picker dialog.
    
    Args:
        mode (str): 'file' to pick a file (default), 'folder' to pick a folder.

    Returns:
        str | None: The selected file/folder path, or None if cancelled.

    Example:
        file_path = fpicker.open()
        folder_path = fpicker.open(mode='folder')
    """
    ... # Actual implementation provided by the C extension

__all__ = ['open']