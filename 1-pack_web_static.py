#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *
def do_pack():
    """ generarates .tgz archive from web_static folder """
    local("mkdir -p versions")
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    r = local("tar -cvzf versions/web_static_{}.tgz ./web_static".
              format(now), capture=True)
    if r.succeeded:
        return ("versions/web_static_{}.tgz".format(now))
    else:
        return
