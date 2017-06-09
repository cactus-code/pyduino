import itertools
import logging
import serial
import time
import platform
from serial.tools import list_ports
if platform.system() == 'Windows':
    import _winreg as winreg
else:
    import glob
    
log = logging.getLogger(__name__)

def get_windows_ports():
    """
    Gets the list of possible COM ports on the computer.
    Uses winreg module.
    """

def build_cmd_str(cmd, args=None):
    """
    Builds a command string that can be sent to the Arduino.
    """
    if args:
        args = '%'.join(map(str, args))
    else:
        args = ''
    return "@{cmd}%{args}$!".format(cmd, args)

def find_port(baud, timeout):
    
    
class Arduino(object):
    def __init__(self, baud=9600, port=None, timeout=2, sr=None):
    
