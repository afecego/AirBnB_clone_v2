#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack."""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    created = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = "web_static_{}.tgz".format(created)

    try:
        if os.path.isdir("versions") is False:
            run("mkdir -p versions")

        end = local("tar -czvf versions/{}.tar /web_static".format(file_name))
        return (end)

    except Exception:
        return (None)
