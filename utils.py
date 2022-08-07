'''Unrelated to game functions and stuff'''

import os
import sys
import threading
from sys import platform as _sys_platform


def platform():
	if "ANDROID_ARGUMENT" in os.environ:
		return "android"
	elif _sys_platform in ("linux", "linux2", "linux3"):
		return "linux"
	elif _sys_platform in ("win32", "cygwin", "msys"):
		return "win"
	elif _sys_platform == "darwin":
		return "mac"

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller, also works for android apps. """
	if platform() in ("linux", "win", "mac"):
		try:
			# PyInstaller creates a temp folder and stores path in _MEIPASS
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")
		return os.path.join(base_path, relative_path)

	elif platform() == "android":
		path = "/data/data/org.test.pgame/files/app/"
		return os.path.join(path, relative_path)

def debounce(wait_time):
    """
    Decorator that will debounce a function so that it is called after wait_time seconds
    If it is called multiple times, will wait for the last call to be debounced and run only this one.
    See the test_debounce.py file for examples
    """
	#  Copyright (c)  2020, salesforce.com, inc.
	#  All rights reserved.
	#  SPDX-License-Identifier: BSD-3-Clause
	#  For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
    def decorator(function):
        def debounced(*args, **kwargs):
            def call_function():
                debounced._timer = None
                return function(*args, **kwargs)

            if debounced._timer is not None:
                debounced._timer.cancel()

            debounced._timer = threading.Timer(wait_time, call_function)
            debounced._timer.start()

        debounced._timer = None
        return debounced

    return decorator
