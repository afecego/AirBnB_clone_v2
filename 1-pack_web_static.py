#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack.
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        tgzName = "web_static_{}.tgz".format(date)
        local("tar -cvzf versions/{} web_static".format(tgzName))
        return tgzName
    except Exception:
        return None
