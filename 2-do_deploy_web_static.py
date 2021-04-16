#!/usr/bin/python3
""" script to deploy a file to servers """
from fabric.api import put, env, run
import datetime
from os import path

env.hosts = ['35.196.217.143', '3.85.208.251']


def do_deploy(archive_path):
    """ function to deploy """
    if path.exists(archive_path) is False:
        return(False)
    command1 = put(archive_path, '/tmp/')
    if command1.failed:
        return(False)
    command2 = run('tar zxvf /tmp/web_static_*.tgz -C /data/web_static/releases/')
    if command2.failed:
        return(False)
    command3 = run('rm /tmp/web_static_*.tgz')
    if command3.failed:
        return(False)
    command4 = run('rm /data/web_static/current')
    if command4.failed:
        return(False)
    command5 = run('ln -sf /data/web_static/releases/web_static/ /data/web_static/current')
    if command5.failed:
        return(False)
    command6 = run('service nginx reload')
    if command6.failed:
        return(False)
