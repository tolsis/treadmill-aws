"""Treadmill module."""


import os
import pkgutil


__path__ = pkgutil.extend_path(__path__, __name__)


def __root_join(*path):
    """Joins path with location of the current file."""
    mydir = os.path.dirname(os.path.realpath(__file__))
    return os.path.realpath(os.path.join(mydir, *path))


# Global pointing to root of the source distribution.
#
# TODO: how will it work if packaged as single zip file?
TREADMILL = __root_join('..', '..', '..')

if os.name == 'nt':
    _TREADMILL_SCRIPT = 'treadmill.cmd'
else:
    _TREADMILL_SCRIPT = 'treadmill'

TREADMILL_BIN = os.path.join(TREADMILL, 'bin', _TREADMILL_SCRIPT)

TREADMILL_LDAP = os.environ.get('TREADMILL_LDAP')
