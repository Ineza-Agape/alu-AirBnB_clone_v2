#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers and configures Nginx to serve it.
"""

from fabric.api import put, run, env, sudo
from os.path import exists

env.hosts = ['54.89.109.87', '100.25.190.21']  # Add your web server IPs here


def do_deploy(archive_path):
    """Distributes an archive to the web servers and sets up Nginx."""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        
        # Upload the archive to the /tmp/ directory
        put(archive_path, '/tmp/')
        
        run('mkdir -p ' + path + no_ext + '/')
        run('tar -xzf /tmp/' + file_n + ' -C ' + path + no_ext + '/')
        run('rm /tmp/' + file_n)
        run('mv ' + path + no_ext + '/web_static/* ' + path + no_ext + '/')
        run('rm -rf ' + path + no_ext + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s ' + path + no_ext + '/ /data/web_static/current')

        configure_nginx()
        
        # Restart Nginx to apply the changes
        sudo('service nginx restart')
        
        return True
    except Exception as e:
        print(e)
        return False


def configure_nginx():
    """
    Configures Nginx to serve the web_static content under /hbnb_static/.
    """
    try:
        nginx_config = """
        server {
            listen 80;
            server_name _;

            location /hbnb_static/ {
                alias /data/web_static/current/;
                index index.html;
            }
        }
        """
        # Write the new configuration to the default site file
        sudo('echo "' + nginx_config + '" | tee /etc/nginx/sites-available/default')
    except Exception as e:
        print(e)
