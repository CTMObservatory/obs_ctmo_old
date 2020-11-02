from lsst.obs.ctmo.ingest import CtmoCameraParseTask

config.parse.retarget(CtmoCameraParseTask)

config.parse.translation = {
    "dataType": "IMAGETYP",
    "expTime": "EXPTIME",
    "frameId": "RUN-ID",
    "filter": "FILTER",
    "field": "OBJECT",
    "dateObs": "DATE-OBS",
    "taiObs": "DATE-OBS",
    "ccd": "INSTRUME",
    "visit": "RUN-ID",
    "ccdTemp": "CCD-TEMP",
}

config.parse.translators = {
    "dateObs": "translate_date",
    "taiObs": "translate_date",
    "visit": "translate_visit",
    "ccd": "translate_ccd",
    "expTime": "translate_exptime",
}

config.register.columns = {
    "frameId": "text",
    "visit": "int",
    "ccd": "int",
    "filter": "text",
    "dataType": "text",
    "expTime": "double",
    "dateObs": "text",
    "taiObs": "text",
    "field": "text",
}

config.parse.defaults = {
    "filter": "Clear",
    "ccd": "42",
    "visit": "33",
    "ccdTemp": "0",
}

config.register.visit = ["visit", "ccd", "filter", "dateObs", "taiObs"]

config.register.unique = ["visit", "ccd"]
