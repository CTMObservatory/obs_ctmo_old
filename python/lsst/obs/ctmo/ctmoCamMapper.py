from lsst.obs.base import CameraMapper
from lsst.daf.persistence import Policy
import lsst.afw.image.utils as afwImageUtils
import lsst.afw.image as afwImage
from lsst.geom import degrees
from lsst.afw.coord import Observatory
from lsst.obs.base import MakeRawVisitInfo
import os
import logging

__all__ = ["CtmoCamMapper"]


class MakeCtmoRawVisitInfo(MakeRawVisitInfo):
    "Make a VisitInfo from the FITS header of a CTMO image"

    # longitude, latitude, elevation
    observatory = Observatory(-97.568956 * degrees, 25.995789 * degrees, 12)
    
    def setArgDict(self, md, argDict):
        """Set an argument dict for makeVisitInfo and pop associated metadata
        @param[in,out] md metadata, as an lsst.daf.base.PropertyList or PropertySet
        @param[in,out] argdict a dict of arguments

        While a Make<>RawVisitInfo file is mandatory for processCcd.py to run,
        it isn't mandatory for it to actually do anything.
        Hence this one simply contains a pass statement.

        However, it's recommended that you at least include the exposure time
        from the image header and observatory information
        (for the latter, remember to edit and uncomment the "observatory"
        variable above.)
        """
        argDict["exposureTime"] = self.popFloat(md, "EXPTIME")
        argDict["observatory"] = self.observatory


class CtmoCamMapper(CameraMapper):
    packageName = "obs_ctmo"

    # A rawVisitInfoClass is required by processCcd.py
    MakeRawVisitInfoClass = MakeCtmoRawVisitInfo

    def __init__(self, inputPolicy=None, **kwargs):
        policyFile = Policy.defaultPolicyFile(
            self.packageName, "CtmoMapper.yaml", "policy"
        )
        policy = Policy(policyFile)
        # ...and add it to the mapper:
        super(CtmoCamMapper, self).__init__(
            policy, os.path.dirname(policyFile), **kwargs
        )

        # Define your filter set
        # Create a dict of filters:
        self.filters = {}

        # Define your set of filters; you can have as many filters as you like...
        afwImageUtils.defineFilter(name="Clear", lambdaEff=535.5, alias=["Clear"])

        # ...add them to your filter dict...
        self.filters["Clear"] = afwImage.Filter("Clear").getCanonicalName()

        # ...and set your default filter.
        self.defaultFilterName = "Clear"

    def _computeCcdExposureId(self, dataId):
        """Every exposure needs a unique ID.
        Here, I construct a unique ID by adding ccd and visit.
        processCcd.py will fail with a NotImplementedError() without this."""

        pathId = self._transformId(dataId)
        visit = pathId["visit"]
        ccd = pathId["ccd"]
        visit = int(visit)
        ccd = int(ccd)

        return visit + ccd

    def bypass_ccdExposureId(self, datasetType, pythonType, location, dataId):
        """You need to tell the stack that it needs to refer to the above
        _computeCcdExposureId function.
        processCcd.py will fail with an AttributeError without this.
        """
        return self._computeCcdExposureId(dataId)

    def bypass_ccdExposureId_bits(self, datasetType, pythonType, location, dataId):
        """You need to tell the stack how many bits to use for the ExposureId.
        Here I say that the ccd ID takes up to 6 bits (2**6=64),
        and I can have up to 16,777,216 (=2**24) visits in my survey.
        processCcd.py will fail with an AttributeError without this.
        """
        return 24 + 6

    def _extractDetectorName(self, dataId):
        """
        Every detector needs a name.
        Here, I simply use the ccd ID number extracted from the header and
        recorded via the ingest process.
        processCcd.py will fail with a NotImplementedError() without this.
        """
        return int("%(ccd)d" % dataId)
