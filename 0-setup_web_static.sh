#!/usr/bin/env bash
<<<<<<< HEAD
# Sets up the servers for deployment of the web_static


#installing nginx if its not already installed
sudo apt-get update
sudo apt-get install -y nginx

#creating the folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#create fake HTML file
sudo echo "<html>
=======
# Script to set up web servers for deployment of web_static

# Update and install Nginx if not installed
sudo apt-get update
sudo apt-get -y install nginx

# Ensure Nginx is running
sudo service nginx start

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file to test the Nginx configuration
echo "<html>
>>>>>>> 1be626c89d9a90a9e20df9fcd4cb95ea2a36b90a
  <head>
  </head>
  <body>
    Holberton School
  </body>
<<<<<<< HEAD
</html>"|sudo tee /data/web_static/releases/test/index.html

# for the symbolic link
sudo ln -fs /data/web_static/releases/test/  /data/web_static/current

# giving ownership to the /data/ folder
sudo chown -R ubuntu:ubuntu /data/

# updating nginx configuration
nginx_config="server {
    listen 80;
    listen [::]:80;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}"

echo "$nginx_config" | sudo tee /etc/nginx/sites-available/default > /dev/null
sudo service nginx restart
=======
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, recreate if it exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart

# Exit successfully
exit 0
>>>>>>> 1be626c89d9a90a9e20df9fcd4cb95ea2a36b90a
