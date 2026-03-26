import socket

from ddtrace.internal.settings.env import getenv


_hostname = getenv("DD_HOSTNAME", "")  # type: str


def get_hostname():
    # type: () -> str
    global _hostname
    if not _hostname:
        _hostname = socket.gethostname()
    return _hostname


def _reset():
    global _hostname
    _hostname = ""
