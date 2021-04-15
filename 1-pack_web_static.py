#!/usr/bin/python3
""" script to package the web_static folder """
from fabric.api import local
import datetime
import os

def do_pack():
    """ function to make the package """
    str1 = (str(datetime.datetime.now()).split("."))[0]
    str1 = str1.replace("-", "").replace(":", "").replace(" ", "")
    command1 = local("mkdir -p versions")
    if command1.failed:
        return(None)
    path = "versions/web_static_{}.tgz".format(str1)
    print("Packing web_static to {}".format(path))
    command2 = local("tar -cvzf {} web_static".format(path))
    if command2.failed:
        return(None)
    print("web_static packed: {} -> {}Bytes".format(path, os.path.getsize(path)))
    return("versions/web_static_{}.tgz".format(str1))