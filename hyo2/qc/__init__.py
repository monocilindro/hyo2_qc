"""
Hydro-Package
QC
"""
import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

name = "QC"
__version__ = '3.3.0'
__author__ = 'gmasetti@ccom.unh.edu; tyanne.faulkes@noaa.gov; julia.wallace@noaa.gov; matthew.wilson@noaa.gov; ' \
             'brc@ccom.unh.edu'
__license__ = 'LGPLv3 license'
__copyright__ = 'Copyright 2021 University of New Hampshire, Center for Coastal and Ocean Mapping'


def hyo():
    return __doc__, __version__
