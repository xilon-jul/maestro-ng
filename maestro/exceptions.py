# Copyright (C) 2013-2014 SignalFuse, Inc.
#
# Docker container orchestration utility.

import sys

# This hack is unfortunate, but required to get proper exception tracebacks
# that work both in Python 2.x and Python 3.x (since we can't write the raise
# ... from syntax in Python 2.x)
if sys.version_info[0] == 2:
    exec("""
def raise_with_tb(info=None):
    info = info or sys.exc_info()
    raise info[0], info[1], info[2]
""")
else:
    def raise_with_tb(info):
        info = info or sys.exc_info()
        raise info[1].with_traceback(info[2])


class MaestroException(Exception):
    """Base class for Maestro exceptions."""
    pass


class DependencyException(MaestroException):
    """Dependency resolution error."""
    pass


class ParameterException(MaestroException):
    """Invalid parameter passed to Maestro."""
    pass


class EnvironmentConfigurationException(MaestroException):
    """Error in the Maestro environment description file."""
    pass


class OrchestrationException(MaestroException):
    """Error during the execution of the orchestration score."""
    pass


class InvalidPortSpecException(MaestroException):
    """Error thrown when a port spec is in an invalid format."""
    pass


class InvalidLifecycleCheckConfigurationException(MaestroException):
    """Error thrown when a lifecycle check isn't configured properly."""
    pass


class InvalidRestartPolicyConfigurationException(MaestroException):
    """Error thrown when a restart policy isn't configured properly."""
    pass


class InvalidVolumeConfigurationException(MaestroException):
    """Error thrown when a volume binding isn't configured properly."""
