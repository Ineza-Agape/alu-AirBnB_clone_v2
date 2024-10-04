#!/usr/bin/python3
"""
A Fabric script to distribute
an archive to web servers using the function do_deploy.
"""

from fabric.api import env, run, put, local, sudo
from os.path import exists
from datetime import datetime
env.hosts = ['54.160.49.83', '3.90.189.37']  # Add your web server IPs here


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        (str): Archive path if successfully generated, None otherwise.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate timestamp for the archive name
        timestr = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create the .tgz archive
        archive_path = "versions/web_static_{}.tgz".format(timestr)
        local("tar -cvzf {} web_static/".format(archive_path))

        return archive_path
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to web servers and perform deployment steps.

    Args:
        archive_path (str): Path to the archive file.

    Returns:
        bool: True if all operations are successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, '/tmp/')

        # Create the target directory where the archive will be unpacked
        run('mkdir -p {}{}/'.format(path, no_ext))

        # Unpack the archive in the release folder
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))

        # Remove the archive from /tmp/
        run('rm /tmp/{}'.format(file_n))

        # Move files from web_static to the release folder
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))

        # Remove the now-empty web_static folder
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        # Delete the old symbolic link (current)
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link pointing to the new release
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        # Restart Nginx to apply the changes
        sudo('service nginx restart')

        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers.

    Returns:
        bool: True if all steps are successful, False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def setup_nginx():
    """
    Set up Nginx to serve the content of web_static.
    """
    try:
        # Ensure Nginx is installed
        sudo('apt-get -y update')
        sudo('apt-get -y install nginx')

        # Create the directory for deployment if it doesn't exist
        sudo('mkdir -p /data/web_static/releases/test/')
        sudo('mkdir -p /data/web_static/shared/')

        # Create a test HTML file in the test release folder
        sudo('echo "Hello AirBnB!" | tee /data/web_static/releases/test/index.html')

        # Create symbolic link
        sudo('ln -sf /data/web_static/releases/test/ /data/web_static/current')

        # Set proper ownership
        sudo('chown -R ubuntu:ubuntu /data/')

        # Configure Nginx to serve the web_static content
        nginx_config = """
        server {
            listen 80;
            server_name your_server_ip;

            location /hbnb_static/ {
                alias /data/web_static/current/;
                index index.html;
            }
        }
        """
        sudo('echo "{}" | tee /etc/nginx/sites-available/default'.format(nginx_config))
        sudo('service nginx restart')
    except Exception as e:
        print(e)

