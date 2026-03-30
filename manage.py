#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

    if len(sys.argv) == 2 and sys.argv[1] == "runserver":
        sys.argv.append("8050")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django nao esta instalado. Ative o ambiente virtual e instale as dependencias."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
