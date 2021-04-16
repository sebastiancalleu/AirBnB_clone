#!/usr/bin/python3
""" script to deploy a file to servers """
from fabric.api import put, env, run
import datetime
from os import path

env.hosts = ['35.196.217.143', '3.85.208.251']


def do_deploy(archive_path):
    """ function to deploy """
    filename = archive_path.split("/")[1]
    filenamewe = filename.replace(".tgz", "")
    if path.exists(archive_path) is False:
        return(False)
    command1 = put('{}'.format(archive_path), '/tmp/')
    if command1.failed:
        return(False)
    command1_2 = run('mkdir -p /data/web_static/releases/{}/'.format(filenamewe))
    if command1_2.failed:
        return(False)
    command2 = run('tar zxvf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, filenamewe))
    if command2.failed:
        return(False)
    command3 = run('rm /tmp/{}'.format(filename))
    if command3.failed:
        return(False)
    command3_2 = run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(filenamewe, filenamewe))
    if command3_2.failed:
        return(False)
    command3_3 = run('rm -rf /data/web_static/releases/{}/web_static'.format(filenamewe))
    if command3_3.failed:
        return(False)
    command4 = run('rm -rf /data/web_static/current')
    if command4.failed:
        return(False)
    command5 = run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(filenamewe))
    if command5.failed:
        return(False)
    print("New version deployed!")
    return(True)
