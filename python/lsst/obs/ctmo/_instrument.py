"""Butler instrument description for CTMO.
"""

import os

from lsst.afw.cameraGeom import makeCameraFromPath, CameraConfig
from lsst.obs.base import Instrument
from lsst.obs.ctmo.ctmoFilters import CTMO_FILTER_DEFINITIONS
from lsst.daf.butler.core.utils import getFullTypeName
from lsst.utils import getPackageDir

__all__ = "CTMO"


class CTMO(Instrument):
    filterDefinitions = CTMO_FILTER_DEFINITIONS

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Tell it where the config file are:
        packageDir = getPackageDir("obs_ctmo")
        self.configPaths = [os.path.join(packageDir, "config")]

    @classmethod
    def getName(cls):
        return "Cristina Torres Memorial Observatory"

    def getCamera(self):
        "Grab camera information from camera/camera.py file."
        path = os.path.join(getPackageDir("obs_vista"), "camera")
        config = CameraConfig()
        config.load(os.path.join(path, "camera.py"))
        return makeCameraFromPath(
            cameraConfig=config,
            ampInfoPath=path,
            shortNameFunc=lambda name: name.replace(" ", "_"),
        )

    def getRawFormatter(self, dataId):
        from .rawFormatter import CtmoRawFormatter

        return CtmoRawFormatter

    def makeDataIdTranslatorFactory(self):
        "Needed to register instrument"
        pass

    def register(self, registry):
        """This populates the database with instrument and detector-specific
        information, and is implemented with:
        butler register-instrument DATA_REPO lsst.obs.ctmo.CTMO"""

        # Register the instrument:
        obsMax = 2 ** 5  # NeCam only ever took 32 images!
        registry.insertDimensionData(
            "instrument",
            {
                "name": self.getName(),
                "detector_max": 1,
                "visit_max": obsMax,
                "exposure_max": obsMax,
                "class_name": getFullTypeName(self),
            },
        )

        # Register the detector(s):
        registry.insertDimensionData(
            "detector",
            {
                "instrument": self.getName(),
                "id": 1,
                "full_name": "01",
                "name_in_raft": None,
                "raft": None,
                "purpose": None,
            },
        )

        # Registers the filter(s):
        self._registerFilters(registry)
