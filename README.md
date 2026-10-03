# my_own_namespace.yandex_cloud_elk

Коллекция Ansible с собственным модулем `my_own_module` и ролью
`my_own_role`, которые создают текстовый файл на удалённом хосте
с заданным содержимым.

## Состав коллекции

| Компонент | Путь | Описание |
|---|---|---|
| Модуль | `plugins/modules/my_own_module.py` | Создаёт текстовый файл с заданным содержимым |
| Роль | `roles/my_own_role/` | Обёртка над модулем с параметрами по умолчанию |
| Playbook | `playbooks/role_playbook.yml` | Пример использования роли |

## Требования

- Ansible 2.9+
- Python 3 на управляющем и управляемом узлах
- Коллекция устанавливается как `my_own_namespace.yandex_cloud_elk`

## Установка

### Из локального архива

    ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz

### Из Git-репозитория

    ansible-galaxy collection install git+https://github.com/Ayrin24/my_own_collection.git

---

## Модуль `my_own_module`

Создаёт текстовый файл по указанному пути с указанным содержимым.
Модуль **идемпотентен**: если файл уже существует и его содержимое
совпадает с параметром `content`, изменений не производится
(`changed: false`).

### Параметры

| Параметр | Тип | Обязательный | Описание |
|---|---|---|---|
| `path` | `str` | да | Путь к файлу, который нужно создать |
| `content` | `str` | да | Содержимое, которое нужно записать в файл |

### Возвращаемые значения

| Значение | Тип | Описание |
|---|---|---|
| `path` | `str` | Путь к созданному файлу |
| `content` | `str` | Содержимое, записанное в файл |
| `changed` | `bool` | `true`, если файл был создан или изменён |

### Пример использования

    - name: Create a file with my_own_module
      my_own_namespace.yandex_cloud_elk.my_own_module:
        path: /tmp/example.txt
        content: "Hello, world!"

### Поведение в check-mode

Модуль поддерживает `--check`. В этом режиме он не изменяет файловую
систему, но возвращает `changed: true`, если файл отсутствует или его
содержимое отличается от `content`.

---

## Роль `my_own_role`

Обёртка над модулем `my_own_module`, которая позволяет задавать
параметры через переменные роли.

### Переменные (defaults)

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `my_own_module_path` | `/tmp/my_own_module_output.txt` | Путь к создаваемому файлу |
| `my_own_module_content` | `Hello from role!` | Содержимое файла |

### Пример использования

    ---
    - name: Use my_own_role from collection
      hosts: localhost
      gather_facts: false
      roles:
        - my_own_namespace.yandex_cloud_elk.my_own_role

Или с переопределением переменных:

    ---
    - name: Use my_own_role with custom parameters
      hosts: localhost
      gather_facts: false
      roles:
        - role: my_own_namespace.yandex_cloud_elk.my_own_role
          vars:
            my_own_module_path: /etc/motd
            my_own_module_content: "Welcome to the server"

### Идемпотентность

Роль наследует идемпотентность модуля: повторный запуск playbook
не изменит файл, если он уже создан с тем же содержимым.

---

## Пример playbook

Полный пример находится в `playbooks/role_playbook.yml`:

    ---
    - name: Use my_own_role from collection
      hosts: localhost
      gather_facts: false
      roles:
        - my_own_namespace.yandex_cloud_elk.my_own_role

Запуск:

    ansible-playbook playbooks/role_playbook.yml

---

## Структура коллекции

    my_own_namespace/yandex_cloud_elk/
    ├── galaxy.yml
    ├── README.md
    ├── playbooks/
    │   └── role_playbook.yml
    ├── plugins/
    │   └── modules/
    │       └── my_own_module.py
    ├── roles/
    │   └── my_own_role/
    │       ├── defaults/main.yml
    │       └── tasks/main.yml
    ├── docs/
    └── meta/

---

## Сборка архива

    ansible-galaxy collection build

На выходе появится файл `my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz`.

---

## Лицензия

GPL-3.0-or-later

## Автор

Ayrin24


Скриншоты выполнения работы:

<img width="1209" height="89" alt="5337154154650083289" src="https://github.com/user-attachments/assets/a114d913-6f5f-45a9-b30a-3d608f03d445" />

<img width="1017" height="355" alt="5337154154650083374" src="https://github.com/user-attachments/assets/b4b2e740-6efe-457c-be55-7c815d964f90" />

<img width="1041" height="162" alt="5337154154650083420" src="https://github.com/user-attachments/assets/41f3d1f7-b7d4-4b79-b0e5-4a5232868e4e" />

<img width="1023" height="405" alt="5337154154650083421" src="https://github.com/user-attachments/assets/8c057c16-31b4-430a-ae34-503b6f1123fa" />


