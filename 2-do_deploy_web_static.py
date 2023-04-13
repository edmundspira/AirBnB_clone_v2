#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static
and move it to the servers
"""

from fabric.api import put, env, run
from os.path import exists

env.hosts = ['18.234.192.255', '54.164.58.89']
env.user = 'ubuntu'
env.key_filename = '/home/cheezaram/.ssh/alx_id_rsa'


def do_deploy(archive_path):
    """Deploys the web static to the server"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        folder_name = archive_name.split(".")[0]
        releaseVersion = "/data/web_static/releases/{}/".format(folder_name)
        symLink = "/data/web_static/current"

        print("Deploying new version from {}...".format(folder_name))
        put(archive_path, "/tmp/{}".format(archive_name))
        run("mkdir -p {}".format(releaseVersion))
        run("tar -xzf /tmp/{} -C {} --strip-components=1".format(
            archive_name, releaseVersion))
        run("rm /tmp/{}".format(archive_name))
        run("rm -f {}".format(symLink))
        run("ln -s {} {}".format(releaseVersion, symLink))
        print("New version deployed -> {}".format(releaseVersion))
        return True
    except Exception:
        print("Failed to deploy new version -> {}".format(releaseVersion))
        return False
