#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static
and move it to the servers
"""

from fabric.api import local, put, env, run, runs_once
from datetime import datetime
from os.path import exists

env.hosts = ['18.234.192.255', '54.164.58.89']
env.user = 'ubuntu'
env.key_filename = '/home/cheezaram/.ssh/alx_id_rsa'


@runs_once
def do_pack():
    """Creates a compressed archive of the web_static folder"""

    local("mkdir -p versions")
    currentTime = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(currentTime)
    print("\nPackaging new version of web_static: {}".format(path))
    local("tar -cvzf {} web_static".format(path))

    if not exists(path):
        print("\nfailed to package {}\n".format(path))
        return None

    print("\nNew version packaged: {}\n".format(path))
    return path


def do_deploy(archive_path):
    """Deploys the web static to the server"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        folder_name = archive_name.split(".")[0]
        releaseVersion = "/data/web_static/releases/{}/".format(folder_name)
        symLink = "/data/web_static/current"

        print("\nDeploying new version from: {}...".format(folder_name))
        put(archive_path, "/tmp/{}".format(archive_name))
        run("mkdir -p {}".format(releaseVersion))
        run("tar -xzf /tmp/{} -C {} --strip-components=1".format(
            archive_name, releaseVersion))
        run("rm /tmp/{}".format(archive_name))
        run("rm -f {}".format(symLink))
        run("ln -s {} {}".format(releaseVersion, symLink))
        print("\nNew version deployed as: {}".format(releaseVersion))
        return True
    except Exception as e:
        print("\nfailed to deploy version {}: {}\n".format(releaseVersion, e))
        return False


def deploy():
    """Fully deploys the staic web page"""
    archivePath = do_pack()
    return do_deploy(archivePath) if archivePath else False
