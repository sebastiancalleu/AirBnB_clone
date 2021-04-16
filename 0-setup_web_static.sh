#!/usr/bin/env bash
# script to install and setup nginx to deploy
if ! command -v nginx &> /dev/null;
then
    sudo apt-get -y update
    sudo apt-get install -y nginx
    sudo service nginx start
fi
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
if [ -d /data/web_static/current ]
then
	rm -rf /data/web_static/current
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
#if ! grep -q "location /hbnb_static" /etc/nginx/sites-available/default
#then
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t} " /etc/nginx/sites-available/default
#fi
sudo service nginx restart
