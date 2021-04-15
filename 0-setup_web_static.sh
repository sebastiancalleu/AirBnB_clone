#!/usr/bin/env bash
# script to install and setup nginx to deploy
apt list --installed 2>/dev/null | grep -q nginx || apt-get -y update
apt list --installed 2>/dev/null | grep -q nginx || apt-get -y install nginx
mkdir -p /data /data/web_static /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
if ! grep -q "location /hbnb_static" /etc/nginx/sites-available/default
then
    sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t} " /etc/nginx/sites-available/default
fi
service nginx restart
