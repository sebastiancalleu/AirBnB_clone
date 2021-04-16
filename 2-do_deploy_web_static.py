#!/usr/bin/python3
""" script to deploy a file to servers """
from fabric.api import put, env, run, local
from os import path
import datetime
import os

env.hosts = ['35.196.217.143', '3.85.208.251']

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
    if path.isfile(archive_path):
        try:
            filename = archive_path.split("/")[1]
            filenamewe = filename.replace(".tgz", "")
            put('{}'.format(archive_path), '/tmp/')
            run('mkdir -p /data/web_static/releases/{}'.format(filenamewe))
            run('tar -zxf /tmp/{} -C /data/web_static/releases/{}'
                .format(filename, filenamewe))
            run('rm /tmp/{}'.format(filename))
            route1 = ("/data/web_static/releases/{}/web_static/*"
                      .format(filenamewe))
            route2 = ("/data/web_static/releases/{}/"
                      .format(filenamewe))
            run('mv {} {}'
                .format(route1, route2))
            run('rm -rf /data/web_static/releases/{}/web_static'
                .format(filenamewe))
            run('rm -rf /data/web_static/current')
            run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
                .format(filenamewe))
            print("New version deployed!")
            return(True)
        except:
            return(False)
    else:
        return(False)
