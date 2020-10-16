from lsst.obs.ctmo.ingest import CTMOCameraParseTask

config.parse.retarget(CTMOCameraParseTask)

config.parse.translation = {
    "dataType": "IMAGETYP",  # checked
    "expTime": "EXPTIME",  # checked
    "frameId": "RUN-ID",
    "filter": "FILTER",  # checked
    "field": "OBJECT",  # checked
    "dateObs": "DATE-OBS",  # checked
    "taiObs": "DATE-OBS",  # checked
    "ccd": "INSTRUME",  # checked
    "visit": "VISIT",
    "ccdTemp": "CCD-TEMP",  # checked
}

config.parse.translators = {
    "dateObs": "translateDate",
    "taiObs": "translateDate",
    "visit": "translateVisit",
    "ccd": "translateCcd",
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
    "ccd": "1",
    "visit": "1",
    "frameId": "1",
    "ccdTemp": "0",
}

config.register.visit = ["visit", "ccd", "filter", "dateObs", "taiObs"]

config.register.unique = ["visit", "ccd"]
