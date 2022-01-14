#!/usr/bin/python3

"""
creates and distributes an archive to your web servers

"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['35.243.152.136', '54.196.195.128']


def do_pack():
    """function"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")

        fileName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fileName))

        return fileName

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
        run('mkdir -p {}{}/'.format(path, NFile_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(nameFile, path, NFile_no_ext))
        run('rm /tmp/{}'.format(nameFile))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, NFile_no_ext))
        run('rm -rf {}{}/web_static'.format(path, NFile_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, NFile_no_ext))
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
