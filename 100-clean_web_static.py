#!/usr/bin/python3

"""
Deployment 3
"""

from fabric.api import local, hosts, put, run, env, lcd, cd
from os.path import isdir, exists
import datetime

env.hosts = ['23.21.15.186', '34.138.82.74']

env.user = "ubuntu"

date_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def do_pack():
    """ Compress to tgz """
    try:
        if isdir('versions') is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date_now)
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except Exception:
        return None


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
        run('rm /tmp/{}'.format(nameFile))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, NFile_no_ext))
        run('sudo rm -rf {}{}/web_static'.format(path, NFile_no_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.
            format(path, NFile_no_ext))
        return True
    except Exception:
        return False


def deploy():
    """ Deployment 3 """
    new_filename = do_pack()
    if new_filename is None:
        return False
    x = do_deploy(new_filename)
    return x


def do_clean(number=0):
    """Deletes out-of-date archives."""
    erase = int(number) if int(number) >= 2 else 1
    cmd = ('ls -tr | grep web_static | '
           'head -n -{} | xargs rm -rf'.format(erase))

    with lcd('./versions'):
        local(cmd)
    with cd('/data/web_static/releases/'):
        run(cmd)
