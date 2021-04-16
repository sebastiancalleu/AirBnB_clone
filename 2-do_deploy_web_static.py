#!/usr/bin/python3
""" script to deploy a file to servers """
from fabric.api import put, env, run
from os import path

env.hosts = ['35.196.217.143', '3.85.208.251']


def do_deploy(archive_path):
    """ function to deploy """
    if path.exists(archive_path):
        filename = archive_path.split("/")[1]
        filenamewe = filename.replace(".tgz", "")
        put('{}'.format(archive_path), '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(filenamewe))
        run('tar zxvf /tmp/{} -C /data/web_static/releases/{}'
            .format(filename, filenamewe))
        run('rm /tmp/{}'.format(filename))
        route1 = ("/data/web_static/releases/{}/web_static/*"
                  .format(filenamewe))
        route2 = ("/data/web_static/releases/{}"
                  .format(filenamewe))
        run('mv {} {}'
            .format(route1, route2))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(filenamewe))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filenamewe))
        return(True)
    else:
        return(False)
