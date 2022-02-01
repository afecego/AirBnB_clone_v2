#!/usr/bin/python3
"""
Deploying tgz file to our servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['23.21.15.186', '34.138.82.74']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        nameFile = archive_path.split("/")[-1]
        NFile_no_ext = nameFile.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, NFile_no_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.
            format(nameFile, path, NFile_no_ext))
        run('sudo rm /tmp/{}'.format(nameFile))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, NFile_no_ext))
        run('sudo rm -rf {}{}/web_static'.format(path, NFile_no_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.
            format(path, NFile_no_ext))
        return True
    except Exception:
        return False
