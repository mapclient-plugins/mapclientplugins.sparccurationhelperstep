
"""
MAP Client Plugin
"""

__version__ = '0.5.0'
__author__ = 'Kay Wang'
__stepname__ = 'Sparc Curation Helper'
__location__ = 'https://github.com/mapclient-plugins/mapclientplugins.sparccurationhelperstep'

# import class that derives itself from the step mountpoint.
from mapclientplugins.sparccurationhelperstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
