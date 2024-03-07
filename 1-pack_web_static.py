#!/usr/bin/python3
"""generates a .tgz file from the contens of web_static using FABRIC"""
from fabric.api import *
import datetime


def do_pack():
"""generates a .tgz file from the contens of web_static using FABRIC"""
from fabric.api import *
import datetime
def do_pack():
    """
    generarates .tgz archive from web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
