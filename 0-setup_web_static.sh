#!/usr/bin/env bash
# script to install and setup nginx to deploy
if ! command -v nginx &> /dev/null;
then
    sudo apt-get -y update
    sudo apt-get install -y nginx
    sudo service nginx start
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
#if ! grep -q "location /hbnb_static" /etc/nginx/sites-available/default
#then
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\tautoindex off;\n\t} " /etc/nginx/sites-available/default
#fi
sudo service nginx restart
