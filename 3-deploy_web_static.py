#!/usr/bin/python3
""" script to make a complete deploy """
import datetime
import os
from fabric.api import put, env, run, local
from os import path


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
    print("web_static packed: {} -> {}Bytes"
          .format(path, os.path.getsize(path)))
    return("versions/web_static_{}.tgz".format(str1))


def do_deploy(archive_path):
    """ function to deploy """
    if path.exists(archive_path):
        filename = archive_path.split("/")[1]
        filenamewe = filename.replace(".tgz", "")
        put('{}'.format(archive_path), '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(filenamewe))
        run('tar zxvf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, filenamewe))
        run('rm /tmp/{}'.format(filename))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(filenamewe, filenamewe))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(filenamewe))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(filenamewe))
        print("New version deployed!")
        return(True)
    else:
        return(False)

def deploy():
    path = do_pack()
    if path is None:
        return False
    return(do_deploy(path))