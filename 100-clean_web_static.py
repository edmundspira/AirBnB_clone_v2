#!/usr/bin/python3
"""Fabric script to delete out-of-date archives"""

from fabric.api import env, local, lcd, cd, sudo

env.hosts = ['18.234.192.255', '54.164.58.89']
env.user = 'ubuntu'


def do_clean(number=0):
    """Deletes out-of-date archives"""

    # Convert number to int
    try:
        number = int(number)
    except ValueError as e:
        print("{} is not a valid integer: {}\nquitting...".format(number, e))
        return

    # Check that number is not negative
    if number < 0:
        print("number cannot be negative\nquitting...")
        return
    elif number == 0:
        number = 1

    # Keep the most recent number of archives
    number += 1

    # Delete old archives in versions folder
    with lcd("versions"):
        print("Deleting old archives in versions folder...")
        local("ls -t | tail -n +{} | xargs rm -rf".format(number))

    # Delete old archives in web servers
    with cd("/data/web_static/releases"):
        print("Deleting old archives in web servers...")
        sudo("ls -t | tail -n +{} | xargs rm -rf".format(number))

    print("\nClean-up complete!")
