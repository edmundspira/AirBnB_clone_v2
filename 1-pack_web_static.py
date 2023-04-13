#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static
"""

from fabric.api import local
from datetime import datetime
from os.path import exists


def do_pack():
    """Compress the web_static folder"""

    local("mkdir -p versions")
    currentTime = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(currentTime)
    print("Packaging new version of web_static: {}".format(path))
    local("tar -cvzf {} web_static".format(path))

    if exists(path):
        print("New version packaged: {}".format(path))
        return path
