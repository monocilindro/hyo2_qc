import logging
logger = logging.getLogger(__name__)

from hyo2.qc.common.helper import Helper
from hyo2.qc.common.report import Report


scan_algos = {
    "BASE": 0,
    "FEATURE_SCAN_v7": 7,
    "FEATURE_SCAN_v8": 8,
}

specs_vers = {
    "BASE": 0,
    "2015": 1,
    "2016": 2,
    "2017": 3,
    "2018": 4,
    "2019": 5,
}

survey_areas = {
    "Great Lakes": 0,
    "Pacific Coast": 1,
    "Atlantic Coast": 2,
}

class BaseScan:

    def __init__(self, s57):

        self.type = scan_algos["BASE"]
        self.version = specs_vers["BASE"]

        # inputs
        self.s57 = s57
        # outputs
        self.flagged_features = [[], [], []]
        # report
        self.report = Report()

    def __repr__(self):
        msg = "  <BaseScan>\n"

        msg += "    <type: %s>\n" % Helper.first_match(scan_algos, self.type)
        msg += "    <s57: %s>\n" % bool(self.s57)
        msg += "    <flagged features: %s>\n" % len(self.flagged_features)

        return msg
