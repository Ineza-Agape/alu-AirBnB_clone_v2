#!/usr/bin/env python3
"""
Fabric script to generate a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    - The archive will be stored in the `versions/` folder.
    - The name of the archive will be based on the current date and time.
    - All files in the web_static folder will be added to the archive.

    Returns:
        str: The path to the created archive if successful, None otherwise.
    """

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Get the current time for the archive name
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(time_stamp)

    # Create the .tgz archive
    print(f"Packing web_static to {archive_name}")
    command = "tar -cvzf {} web_static".format(archive_name)

    result = local(command)

    # Check if the archive was successfully created
    if result.succeeded:
        return archive_name
    else:
        return None
