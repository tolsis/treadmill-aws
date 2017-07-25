"""Treadmill Websocket APIs"""
from __future__ import absolute_import

import os
import logging
import pkgutil

from treadmill import authz
from treadmill import utils
from treadmill import plugin_manager


__path__ = pkgutil.extend_path(__path__, __name__)

_LOGGER = logging.getLogger(__name__)


def init(apis):
    """Module initialization."""
    handlers = []
    for apiname in apis:
        try:
            _LOGGER.info('Loading api: %s', apiname)
            wsapi_mod = plugin_manager.load('treadmill.websocket.api', apiname)
            handlers.extend(wsapi_mod.init())

        except ImportError as err:
            _LOGGER.warn('Unable to load %s api: %s', apiname, err)

    return handlers
