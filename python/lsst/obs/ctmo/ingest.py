from lsst.pipe.tasks.ingest import ParseTask
from astropy.time import Time


def datetime2mjd(date_time):
    "Convert a datetime object into Modified Julian Date"
    YY = date_time.year
    MO = date_time.month
    DD = date_time.day
    HH = date_time.hour
    MI = date_time.minute
    SS = date_time.second

    if MO == 1 or MO == 2:
        mm = MO + 12
        yy = YY - 1
    else:
        mm = MO
        yy = YY

    dd = DD + (HH / 24.0 + MI / 24.0 / 60.0 + SS / 24.0 / 3600.0)

    A = int(365.25 * yy)
    B = int(yy / 400.0)
    C = int(yy / 100.0)
    D = int(30.59 * (mm - 2))

    mjd = A + B - C + D + dd - 678912

    return mjd


class CtmoParseTask(ParseTask):
    """[From https://github.com/lsst/obs_lsst/blob/f0c4ae506e8e0a85789aebdd970d7e704c9c6e24/
    python/lsst/obs/lsst/ingest.py#L54]:
    All translator methods receive the header metadata [here via "md"] and
    should return the appropriate value, or None if the value cannot be determined.
    """

    def translate_date(self, md):
        "Convert date format from yyyy-mm-ddThh:mm:ss to yyyy-mm-dd."

        date = md.get("DATE-OBS")
        t = Time(date).isot
        return t

    def translate_visit(self, md):
        "Convert string 'visit' from FITS header into integer"
        return int(md.get("RUN-ID"))

    def translate_ccd(self, md):
        "Convert string 'ccd' from FITS header into integer"
        # We only have 1 ccd
        return 1

    def translate_exptime(self, md):
        "Convert string 'expTime' from FITS header into float"
        return float(md.get("EXPTIME"))


class CtmoCalibsParseTask(ParseTask):

    def translate_ccd(self, md):
        "Convert string 'ccd' from FITS header into integer"
        # We only have 1 ccd
        return 1

    def translate_filter(self, md):
        if "i" in md["FILTER"].replace("SDSS", ""):
            return "i"
        return md["FILTER"]
    
    def translate_calibDate(self, md):
        date = md.get("DATE-OBS")
        t = Time(date).isot
        return t
