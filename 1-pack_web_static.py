from fabric.api import local
import os
from datetime import datetime

def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""

    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Define the name of the archive
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    # Use tar to create the archive
    try:
        print(f"Packing web_static to {archive_name}")
        local(f"tar -cvzf {archive_name} web_static")
        return archive_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
