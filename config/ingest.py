from lsst.obs.ctmo.ingest import CtmoParseTask

config.parse.retarget(CtmoParseTask)

config.parse.translation = {
    "dataType": "IMAGETYP",
    "expTime": "EXPTIME",
    "filter": "FILTER",
    "field": "OBJECT",
    "run": "RUN-ID",
    "mjd": "JD",
    "visit": "RUN-ID",
}

config.parse.translators = {
    "dateObs": "translate_date",
    "taiObs": "translate_date",
    "visit": "translate_visit",
    # "mjd": "translate_jd",
    # "survey": "translate_survey",
    "ccd": "translate_ccd",
}

config.register.visit = ["visit", "run", "ccd", "filter", "dateObs", "taiObs"]

config.register.unique = ["run", "ccd", "filter"]

config.register.columns = {
    "run": "int",
    "visit": "int",
    "ccd": "int",
    "filter": "text",
    "dataType": "text",
    "expTime": "double",
    "dateObs": "text",
    "taiObs": "text",
    "mjd": "int",
    "field": "text",
    #"survey": "text",
}

config.parse.defaults = {"ccd": "1"}
