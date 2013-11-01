# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

SERVICES = {
    'apache2': {
        'running-msg': 'Apache2 is running',
    },
    'ssh': {
        'running-msg': 'ssh start/running',
    },
    'mysql': {
        'running-msg': 'mysql start/running',
    },
    'postgresql-9.1': {
        'running-msg': '9.1/main',
        'service-id': 'postgresql',
    },
}


def service_is_running(service):
    if not service in SERVICES:
        raise ValueError('Unknown service: {0}.'.format(service))
    srv = SERVICES[service]
    status_msg = Popen(['service', srv.get('service-id', service), 'status'], stdout=PIPE).stdout.read()
    return srv['running-msg'] in status_msg
