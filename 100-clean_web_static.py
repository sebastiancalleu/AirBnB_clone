#!/usr/bin/python3
""" clean the releases """
from fabric.api import local, run, env
import datetime
import os


def do_clean(number=0):
    """ function to clean the releases """
    if int(number) == 0:
        keepfiles = 2
    else:
        keepfiles = int(number) + 1
    local("ls -t versions/ | tail -n +{} | xargs -I _ rm versions/_")
    run("ls -t /data/web_static/releases/ | tail -n +{} | xargs -I _ rm /data/web_static/releases/_".format(keepfiles))
