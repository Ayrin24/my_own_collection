#!/usr/bin/python

# Copyright: (c) 2024, Ayrin24
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create a text file with given content

version_added: "1.0.0"

description:
    - This module creates a text file on the remote host.
    - Path is defined by C(path) parameter.
    - Content is defined by C(content) parameter.

options:
    path:
        description: Path to the file to create.
        required: true
        type: str
    content:
        description: Content to write into the file.
        required: true
        type: str

author:
    - Ayrin24 (@Ayrin24)
'''

EXAMPLES = r'''
- name: Create a file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/example.txt
    content: "Hello, world!"
'''

RETURN = r'''
path:
    description: Path to the file created.
    type: str
    returned: always
    sample: /tmp/example.txt
content:
    description: Content written to the file.
    type: str
    returned: always
    sample: "Hello, world!"
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        path='',
        content='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    # В check-mode только сообщаем, что было бы изменено
    if module.check_mode:
        if not os.path.exists(path) or open(path).read() != content:
            result['changed'] = True
        module.exit_json(**result)

    # Если файл уже существует с таким содержимым — ничего не делаем
    if os.path.exists(path):
        with open(path, 'r') as f:
            existing = f.read()
        if existing == content:
            module.exit_json(**result)

    # Создаём/перезаписываем файл
    try:
        with open(path, 'w') as f:
            f.write(content)
        result['changed'] = True
    except Exception as e:
        module.fail_json(msg=f'Failed to write file: {e}', **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
