import logging
logger = logging.getLogger(__name__)

from hyo2.qc.common.helper import Helper
from hyo2.qc.common.report import Report


scan_algos = {
    "BASE": 0,
    "FEATURE_SCAN_v3": 3,
}

specs_vers = {
    "BASE": 0,
    "2014": 1,
    "2016": 2,
    "2018": 3,
}


class BaseScan:
    def __init__(self, s57, ss, progress=None):
        self.type = scan_algos["BASE"]
        self.version = specs_vers["BASE"]
        # inputs
        self.s57 = s57
        self.ss = ss
        # outputs
        self.flagged_features = [[], [], []]
        # report
        self.report = Report()
        # progress bar
        self.progress = progress

    def __repr__(self):
        msg = "  <BaseScan>\n"

        msg += "    <type: %s>\n" % Helper.first_match(scan_algos, self.type)
        msg += "    <s57: %s>\n" % bool(self.s57)
        msg += "    <ss: %s>\n" % bool(self.ss)
        msg += "    <flagged features: %s>\n" % len(self.flagged_features)

        return msg
