#!/usr/bin/env python
from cms_helper import runner

from tests import test_settings


# import settings from test_settings.py file into a dict
HELPER_SETTINGS = {
    setting: getattr(test_settings, setting)
    for setting in dir(test_settings)
    if not setting.startswith("__")
}


def run():
    runner.cms('{{ cookiecutter.app_name }}')


if __name__ == "__main__":
    run()
