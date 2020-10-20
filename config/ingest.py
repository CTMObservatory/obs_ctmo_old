from lsst.obs.ctmo.ingest import CtmoCameraParseTask

config.parse.retarget(CtmoCameraParseTask)

config.parse.translation = {
    "dataType": "IMAGETYP",  # checked
    "expTime": "EXPTIME",  # checked
    "frameId": "RUN-ID",
    "filter": "FILTER",  # checked
    "field": "OBJECT",  # checked
    "dateObs": "DATE-OBS",  # checked
    "taiObs": "DATE-OBS",  # checked
    "ccd": "INSTRUME",  # checked
    "visit": "RUN-ID",
    "ccdTemp": "CCD-TEMP",  # checked
}

config.parse.translators = {
    "dateObs": "translateDate",
    "taiObs": "translateDate",
    "visit": "translateVisit",
    "ccd": "translateCcd",
    "expTime": "translateExpTime",
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
