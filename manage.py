#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
<<<<<<< HEAD

=======
>>>>>>> 13f530bebb75fa9b6b6a3f778aa47d0c7a4c9cc9
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
>>>>>>> 13f530bebb75fa9b6b6a3f778aa47d0c7a4c9cc9
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 13f530bebb75fa9b6b6a3f778aa47d0c7a4c9cc9
    main()
