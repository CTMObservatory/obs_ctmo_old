#Import the library to parse the calibrations:
from lsst.obs.ctmo.ingest import CtmoCalibsParseTask
config.parse.retarget(CtmoCamCalibsParseTask)

#These are the columns that appear in calibregistry.sqlite3:
config.register.columns = {
    'ccd': 'int',
    "filter": "text",
    "calibDate": "text",
    "validStart": "text",
    "validEnd": "text",
}

config.register.detector = ["filter", "ccd"]


#If the values in the header aren't in the format you wish, you
#can use a translator
config.parse.translators = {'ccd': 'translate_ccd',
                            'filter': 'translate_filter',
                            'calibDate': 'translate_calibDate'}

#The combination of these columns must identify the entry uniquely:
config.register.unique = ['filter', 'ccd', 'calibDate']

#I'm not sure what 'visit' is used for, but there must be at least
#one common element between unique and visit.
config.register.visit = ["calibDate", "filter"]

#The tables contained within the registry:
# This is not in GOTO
config.register.tables = ['bias', 'dark', 'flat']
