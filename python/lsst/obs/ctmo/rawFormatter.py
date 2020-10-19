from lsst.obs.base import FitsRawFormatterBase
from ._instrument import CTMO
from .ctmoFilters import CTMO_FILTER_DEFINITIONS

# Comment-out the following line if you put .translators/ctmo.py in the
# astro_metadata_translator repository:
from .translators.ctmo import CtmoTranslator

# ...and uncomment the following:
# from astro_metadata_translator import CtmoTranslator


class CtmoRawFormatter(FitsRawFormatterBase):
    "Gen3 Butler formatter for NeCam raw data"
    translatorClass = CtmoTranslator
    filterDefinitions = CTMO_FILTER_DEFINITIONS

    def getDetector(self, id):
        return CTMO().getCamera()[id]
