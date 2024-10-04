#!/usr/bin/env python3
from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")
    
    # Get the current date and time for the archive name
    now = datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    archive_path = "versions/{}".format(archive_name)

    # Create the tar.gz archive
    print("Packing web_static to {}".format(archive_path))
    result = c.local("tar -cvzf {} web_static".format(archive_path))

    # Check if the command was successful
    if result.failed:
        return None

    return archive_path
