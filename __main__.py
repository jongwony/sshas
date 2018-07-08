import os
import re
import argparse
import subprocess


def get_path(*path, home=False):
    script_dir = os.path.expanduser('~') if home else os.path.abspath('.')
    return os.path.join(script_dir, *path)

parser = argparse.ArgumentParser()
parser.add_argument('opt', help='list add mod del cb(clipboard)')
args = parser.parse_args()

op = args.opt

ADD_TEMPLATE = '''
Host {name}
    HostName        {user}
    User            {host}
    IdentityFile    {pem}
    Port            {port}
'''

if op == 'list':
    subprocess.Popen("sed -n 'p' ~/.ssh/config | less -p '^Host .*$'", shell=True).communicate()

elif op == 'add':
    connect_args = {
        'name' : input('Host: '),
        'host' : input('HostName(IP): '),
        'port' : input('Port[22]: ') or 22,
        'user' : input('User: '),
        'pem' : input('Pem: '),
    }
    with open(get_path('.ssh', 'config', home=True), 'a') as f:
        f.write(ADD_TEMPLATE.format(**connect_args))

elif op == 'mod':
    pass
elif op == 'del':
    pass
elif op == 'cb':
    cb = subprocess.check_output(['pbpaste']).decode().strip()
    print(cb)
    pem = re.search(r'''-i\s*(['"])(.*?)\1''', cb)
    port = re.search(r'''-P\s*(\d+?)''', cb)
    connect_str = re.search(r'\b(\w+)(?::.*)?@(.*)\b', cb)
    host = connect_str.group(2)
    print(connect_str.groups())


    connect_args = {
        'name': input('Host[{}]: '.format(connect_str.group(2))) or host,
        'host': host,
        'port': port.group(1) if port else 22,
        'user': connect_str.group(1),
        'pem': get_path(pem.group(2)) if pem else None,
    }

    with open(get_path('.ssh', 'config', home=True)) as f:
        data = f.readlines()
    print(data)

    print(ADD_TEMPLATE.format(**connect_args))
else:
    raise NotImplementedError
