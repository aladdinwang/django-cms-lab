#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # utf-8 supported
    reload(sys)
    sys.setdefaultencoding("utf-8")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmslab.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
