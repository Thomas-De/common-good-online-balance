from fabric.api import *
from fabvenv import virtualenv


def staging():
    env.hosts = ['deploy_hosts_user@example.com']
    env.path = '/var/www/vhosts/example.com/staging.example.com'
    env.push_branch = 'master'
    env.push_remote = 'origin'
    env.virtualenv_path = '/var/www/vhosts/example.com/stagingenv/'


def production():
    env.hosts = ['deploy_hosts_user@example.com']
    env.path = '/var/www/vhosts/example.com/httpdocs'
    env.push_branch = 'master'
    env.push_remote = 'origin'
    env.virtualenv_path = '/var/www/vhosts/example.com/ecg_balancingenv/'


def update():
    with cd(env.path):
        run("git pull %(push_remote)s %(push_branch)s" % env)


def pip():
    update()
    with cd(env.path):
        with virtualenv(env.virtualenv_path):
            run("pip install -Ur requirements.txt ")


def deploy():
    update()
    with cd(env.path):
        with virtualenv(env.virtualenv_path):
            run("python manage.py syncdb")
            run("python manage.py migrate")
            run("python manage.py collectstatic")
            run("supervisorctl reload staging.example.com")


def syncdb():
    with cd(env.path):
        run("cat ecg_balancing_dump.sql | mysql -uecg_balancing ecg_balancing")